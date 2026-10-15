import os
import bpy
import bmesh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IN_FILE = os.path.join(SCRIPT_DIR, "worlds-robot.glb")
OUT_FILE = os.path.join(SCRIPT_DIR, "worlds-robot-optimized.glb")
MAX_HOLE_AREA = 0.0005  # Adjust if unit scale is inches vs meters/mm

print(f"Loading {IN_FILE}...")
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=IN_FILE)

mesh_objs = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']
total = len(mesh_objs)
print(f"Found {total} mesh objects. Starting direct bmesh cleanup (no mode-switching)...")

for i, obj in enumerate(mesh_objs):
    if (i + 1) % 100 == 0 or i == total - 1:
        print(f"Processing mesh {i+1}/{total} ({obj.name})...")
    try:
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        
        # 1. Merge split CAD vertices
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0001)
        
        # 2. Delete small inner wall faces (hole tunnels)
        small_faces = [f for f in bm.faces if f.calc_area() < MAX_HOLE_AREA]
        if small_faces:
            bmesh.ops.delete(bm, geom=small_faces, context='FACES')
        
        # 3. Fill resulting boundary loops & dissolve flat faces
        boundary_edges = [e for e in bm.edges if e.is_boundary]
        if boundary_edges:
            bmesh.ops.holes_fill(bm, edges=boundary_edges, sides=8)
        bmesh.ops.dissolve_limit(bm, angle_limit=0.01, verts=bm.verts, edges=bm.edges)
        
        bm.to_mesh(obj.data)
        bm.free()
        obj.data.update()
    except Exception as e:
        print(f"Warning on object {obj.name}: {e}")

print(f"Exporting cleaned GLB to {OUT_FILE}...")
bpy.ops.export_scene.gltf(filepath=OUT_FILE, export_format='GLB')
print("Blender optimization finished successfully!")
