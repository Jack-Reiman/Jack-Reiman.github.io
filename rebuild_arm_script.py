import DracoPy, struct, json, os, numpy as np

print("Rebuilding worlds-robot-lines.glb with strict arm isolation...")

with open('assets/projects/worlds-robot.glb', 'rb') as f:
    data = f.read()

chunk_len, _ = struct.unpack('<II', data[12:20])
gltf = json.loads(data[20:20+chunk_len].decode('utf-8'))
bin_data = data[20+chunk_len+8:]

# Remove Draco extensions declaration
if 'extensionsUsed' in gltf and 'KHR_draco_mesh_compression' in gltf['extensionsUsed']:
    gltf['extensionsUsed'].remove('KHR_draco_mesh_compression')
if 'extensionsRequired' in gltf and 'KHR_draco_mesh_compression' in gltf['extensionsRequired']:
    gltf['extensionsRequired'].remove('KHR_draco_mesh_compression')

new_bin = bytearray()
new_buffer_views = []
accessors = gltf['accessors']

def add_buffer_data(raw_bytes, target=None):
    pad = (4 - (len(new_bin) % 4)) % 4
    new_bin.extend(b'\x00' * pad)
    offset = len(new_bin)
    new_bin.extend(raw_bytes)
    bv = {'buffer': 0, 'byteOffset': offset, 'byteLength': len(raw_bytes)}
    if target:
        bv['target'] = target
    bv_idx = len(new_buffer_views)
    new_buffer_views.append(bv)
    return bv_idx

# Decompress all primitives
for m in gltf.get('meshes', []):
    for p in m.get('primitives', []):
        ext = p.get('extensions', {}).pop('KHR_draco_mesh_compression', None)
        if not ext:
            continue
        bv = gltf['bufferViews'][ext['bufferView']]
        offset = bv.get('byteOffset', 0)
        length = bv['byteLength']
        compressed = bin_data[offset:offset+length]
        dmesh = DracoPy.decode_buffer_to_mesh(compressed)
        
        # Indices
        faces = np.array(dmesh.faces, dtype=np.uint32)
        idx_accessor_idx = p['indices']
        idx_acc = accessors[idx_accessor_idx]
        max_idx = int(faces.max()) if faces.size > 0 else 0
        if max_idx < 65536:
            indices_bytes = faces.astype(np.uint16).tobytes()
            idx_acc['componentType'] = 5123
        else:
            indices_bytes = faces.tobytes()
            idx_acc['componentType'] = 5125
        idx_bv = add_buffer_data(indices_bytes, target=34963)
        idx_acc['bufferView'] = idx_bv
        idx_acc['byteOffset'] = 0
        idx_acc['count'] = faces.size
        
        # Positions
        pts = np.array(dmesh.points, dtype=np.float32)
        pos_accessor_idx = p['attributes']['POSITION']
        pos_acc = accessors[pos_accessor_idx]
        pos_bv = add_buffer_data(pts.tobytes(), target=34962)
        pos_acc['bufferView'] = pos_bv
        pos_acc['byteOffset'] = 0
        pos_acc['count'] = len(pts)
        pos_acc['min'] = pts.min(axis=0).tolist()
        pos_acc['max'] = pts.max(axis=0).tolist()
        
        # Normals
        if 'NORMAL' in p['attributes'] and len(dmesh.normals) > 0:
            norms = np.array(dmesh.normals, dtype=np.float32)
            norm_accessor_idx = p['attributes']['NORMAL']
            norm_acc = accessors[norm_accessor_idx]
            norm_bv = add_buffer_data(norms.tobytes(), target=34962)
            norm_acc['bufferView'] = norm_bv
            norm_acc['byteOffset'] = 0
            norm_acc['count'] = len(norms)
        
        if 'extensions' in p and not p['extensions']:
            del p['extensions']

gltf['bufferViews'] = new_buffer_views
gltf['buffers'] = [{'byteLength': len(new_bin)}]

# STRICT ARM PART SELECTION:
# ONLY parts connected directly to the two C-channel bars (Solid530 and Solid608):
# - Solid530 & its hardware: 531..540, 583, 616
# - Solid608 & its hardware: 584..594, 617
# - Right 36T gear assembly & fasteners locked to 530: 631..646
# - Left 36T gear assembly & fasteners locked to 608: 1187..1199
arm_names = {
    'Solid530', 'Solid531', 'Solid532', 'Solid533', 'Solid534', 'Solid535', 'Solid536', 'Solid537', 'Solid538', 'Solid539', 'Solid540',
    'Solid583', 'Solid616',
    'Solid631', 'Solid632', 'Solid633', 'Solid634', 'Solid635', 'Solid636', 'Solid637', 'Solid638', 'Solid639', 'Solid640', 'Solid641', 'Solid642', 'Solid643', 'Solid644', 'Solid645', 'Solid646',
    'Solid608', 'Solid584', 'Solid585', 'Solid586', 'Solid587', 'Solid588', 'Solid589', 'Solid590', 'Solid591', 'Solid592', 'Solid593', 'Solid594',
    'Solid617',
    # Left 36T gear assembly & fasteners locked to 608: 1187..1199
    'Solid1187', 'Solid1188', 'Solid1189', 'Solid1190', 'Solid1191', 'Solid1192', 'Solid1193', 'Solid1194', 'Solid1195', 'Solid1196', 'Solid1197', 'Solid1198', 'Solid1199',
    # Diagonal 1x channels (cross braces) connecting the two arm C-channels, plus their screws/nuts/spacers:
    'Solid595', 'Solid596', 'Solid597', 'Solid598', 'Solid599', 'Solid600', 'Solid601', 'Solid602', 'Solid603', 'Solid604', 'Solid605', 'Solid606', 'Solid607'
}

nodes = gltf['nodes']
arm_node_indices = []
body_node_indices = []

for idx, n in enumerate(nodes):
    name = n.get('name', '')
    if name in arm_names:
        arm_node_indices.append(idx)
    else:
        body_node_indices.append(idx)

print(f"Isolated strictly: {len(arm_node_indices)} arm parts, {len(body_node_indices)} stationary body parts.")

# Pivot is the center of the 36T gear (Solid632):
py = 0.350917
pz = 0.145495

arm_contents_idx = len(nodes)
nodes.append({
    'name': 'arm_contents',
    'translation': [0, -py, -pz],
    'children': arm_node_indices
})

arm_pivot_idx = len(nodes)
nodes.append({
    'name': 'arm',
    'translation': [0, py, pz],
    'children': [arm_contents_idx]
})

body_root_idx = len(nodes)
nodes.append({
    'name': 'body',
    'children': body_node_indices
})

robot_root_idx = len(nodes)
nodes.append({
    'name': 'robot_root',
    'children': [body_root_idx, arm_pivot_idx]
})

gltf['scenes'][0]['nodes'] = [robot_root_idx]

# Save GLB
new_json_bytes = json.dumps(gltf, separators=(',', ':')).encode('utf-8')
pad = (4 - (len(new_json_bytes) % 4)) % 4
new_json_bytes += b' ' * pad

bin_pad = (4 - (len(new_bin) % 4)) % 4
new_bin.extend(b'\x00' * bin_pad)

bin_chunk_hdr = struct.pack('<II', len(new_bin), 0x004E4942)
total_len = 12 + 8 + len(new_json_bytes) + 8 + len(new_bin)
header = struct.pack('<4sII', b'glTF', 2, total_len)
json_chunk_hdr = struct.pack('<II', len(new_json_bytes), 0x4E4F534A)

out_path = 'assets/projects/worlds-robot-lines.glb'
with open(out_path, 'wb') as f:
    f.write(header)
    f.write(json_chunk_hdr)
    f.write(new_json_bytes)
    f.write(bin_chunk_hdr)
    f.write(new_bin)

print(f"Done! Clean GLB written to {out_path} ({os.path.getsize(out_path)} bytes)")
