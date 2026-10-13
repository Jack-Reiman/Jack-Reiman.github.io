with open('assets/index-Cav4xqQL.js', 'r', encoding='utf-8') as f:
    s = f.read()

# Let's inspect Xe exploded bounds and boxes():
# In Xe:
# applyExplode(1); for(let w=0;w<=8;w++)u(-30+60*w/8,10),e.box(x);
# On the project page, the mouse tilt can reach:
# b.t = 35 * w (from -35 to +35 deg), h.t = -15 * T (from -15 to +15 deg).
# When the cycloidal gearbox explodes along its axis at az=142, el=24,
# its parts translate towards negative x (to the left!).
# Let's make sure boxes() covers the FULL explosion and rotation reach:
old_xe_boxes = 'boxes(){applyExplode(0),u(0,0);const n=e.box(),x=n.clone();applyExplode(1);for(let w=0;w<=8;w++)u(-30+60*w/8,10),e.box(x);applyExplode(0),u(0,0);return{rest:n,all:x}}'
new_xe_boxes = 'boxes(){applyExplode(0),u(0,0);const n=e.box(),x=n.clone();applyExplode(1);for(let w=0;w<=8;w++)for(let pitch=-15;pitch<=15;pitch+=15){u(-40+80*w/8,pitch);e.box(x);}applyExplode(0),u(0,0);return{rest:n,all:x}}'

assert old_xe_boxes in s, 'old_xe_boxes not found'
s = s.replace(old_xe_boxes, new_xe_boxes)

# Now, in lt():
# When p.span is calculated:
# old: p.span=new $(new M(l(p.all.min.x,R.x),l(p.all.min.y,R.y),p.all.min.z),new M(l(p.all.max.x,R.x),l(p.all.max.y,R.y),p.all.max.z));
# Let's give span 15% extra breathing margin on all sides so nothing ever clips the canvas boundary:
old_span = 'p.span=new $(new M(l(p.all.min.x,R.x),l(p.all.min.y,R.y),p.all.min.z),new M(l(p.all.max.x,R.x),l(p.all.max.y,R.y),p.all.max.z));'
new_span = 'const padSpan=(mn,mx,c)=>c+(mn-c)*1.18,padSpanMax=(mn,mx,c)=>c+(mx-c)*1.18;p.span=new $(new M(padSpan(l(p.all.min.x,R.x),0,R.x),padSpan(l(p.all.min.y,R.y),0,R.y),p.all.min.z),new M(padSpanMax(0,l(p.all.max.x,R.x),R.x),padSpanMax(0,l(p.all.max.y,R.y),R.y),p.all.max.z));'

assert old_span in s, 'old_span not found'
s = s.replace(old_span, new_span)

with open('assets/index-Cav4xqQL.js', 'w', encoding='utf-8') as f:
    f.write(s)

print('Updated index-Cav4xqQL.js span and boxes calculation successfully')
