with open('assets/index-Cav4xqQL.js', 'r', encoding='utf-8') as f:
    s_cav = f.read()

# 1. In Xe.boxes(): only do the full exploded envelope on the project page so the home page canvas size stays compact!
old_xe_boxes = 'boxes(){applyExplode(0),u(0,0);const n=e.box(),x=n.clone();applyExplode(1);for(let w=0;w<=8;w++)for(let pitch=-15;pitch<=15;pitch+=15){u(-40+80*w/8,pitch);e.box(x);}applyExplode(0),u(0,0);return{rest:n,all:x}}'
new_xe_boxes = 'boxes(){applyExplode(0),u(0,0);const n=e.box(),x=n.clone();if(isProjectPage()){applyExplode(1);for(let w=0;w<=8;w++)for(let pitch=-15;pitch<=15;pitch+=15){u(-40+80*w/8,pitch);e.box(x);}applyExplode(0),u(0,0);}else{applyExplode(1);for(let w=0;w<=8;w++)u(-30+60*w/8,10),e.box(x);applyExplode(0),u(0,0);}return{rest:n,all:x}}'

assert old_xe_boxes in s_cav, 'old_xe_boxes not found'
s_cav = s_cav.replace(old_xe_boxes, new_xe_boxes)

# 2. In lt span calculation: use 1.30 on project page and 1.08 on home page:
old_span = 'l=(o,g)=>g+(o-g)*1.35;'
new_span = 'const isProjPage=()=>window.location.hash.indexOf("#work/")!==-1;l=(o,g)=>g+(o-g)*(isProjPage()?1.30:1.06);'

assert old_span in s_cav, 'old_span not found'
s_cav = s_cav.replace(old_span, new_span)

with open('assets/index-Cav4xqQL.js', 'w', encoding='utf-8') as f:
    f.write(s_cav)

print('Updated index-Cav4xqQL.js successfully')

# 3. In index-BwGDr2zK.js:
with open('assets/index-BwGDr2zK.js', 'r', encoding='utf-8') as f:
    s_main = f.read()

# Update wm2 to place the models closer to the edges while maintaining equal margins and equilateral balance:
# Margin on right and left: m = 24
# Free width W = e - side - m
# cx_left = side + W * 0.20
# cx_mid = side + W * 0.50
# cx_right = side + W * 0.80
# cy_top = m + H * 0.23
# cy_bot_base = m + H * 0.69
wm2_code = '''function wm2(e,t,n,r,l,figs){
if(!(Yl(e,t,l)&&r===3))return wm(e,t,n,r,l);
const side=n?Math.max(pi,n.right)+20:32,m=24,W=e-side-m,H=t-m*2;
const cx_left=side+W*0.20,cx_mid=side+W*0.50,cx_right=side+W*0.80;
const cy_top=m+H*0.23;
const cy_bot_base=m+H*0.69;
const sz=Math.min(500,W*0.35,H*0.48);
return[
{cx:cx_left,cy:cy_bot_base+42,size:sz},
{cx:cx_mid,cy:cy_top,size:sz*1.02},
{cx:cx_right,cy:cy_bot_base-22,size:sz}
];}
'''

idx1 = s_main.find('function wm2(')
idx2 = s_main.find('function km(e){')
assert idx1 != -1 and idx2 != -1
s_main = s_main[:idx1] + wm2_code + s_main[idx2:]

with open('assets/index-BwGDr2zK.js', 'w', encoding='utf-8') as f:
    f.write(s_main)

print('Updated index-BwGDr2zK.js successfully')
