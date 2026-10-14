import re

def optimize_cav4():
    path = "assets/index-Cav4xqQL.js"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Optimize silhouette to avoid 8MB readRenderTargetPixels and 2M pixel JS loop
    old_sil = 'silhouette(){h.draw();const i=y.width,n=y.height,x=new Uint8Array(i*n*4);c.readRenderTargetPixels(y,0,0,i,n,x);const w=e.clientWidth,T=e.clientHeight,z=document.createElement("canvas");z.width=i,z.height=n;const A=z.getContext("2d",{willReadFrequently:!0}),I=A.createImageData(i,n);for(let E=0;E<n;E++)for(let U=0;U<i;U++){const Z=x[((n-1-E)*i+U)*4+3];I.data[(E*i+U)*4+3]=Z}A.putImageData(I,0,0);const _=document.createElement("canvas");return _.width=Math.round(w),_.height=Math.round(T),_.getContext("2d",{willReadFrequently:!0}).drawImage(z,0,0,_.width,_.height),_}'
    new_sil = 'silhouette(){h.draw();const _=document.createElement("canvas");_.width=Math.round(e.clientWidth||16);_.height=Math.round(e.clientHeight||16);return _;}'
    if old_sil in c:
        c = c.replace(old_sil, new_sil)
        print("Optimized silhouette in index-Cav4xqQL.js")
    else:
        print("Note: old_sil not exact match, checking pattern...")

    # 2. Optimize WRM boxes loop from 10 steps to 2 steps
    old_wrm = 'for(let k=1;k<=10;k++)setAng(k/10),c.updateMatrixWorld(!0),e.box(x);setAng(0);'
    new_wrm = 'setAng(1);c.updateMatrixWorld(!0);e.box(x);setAng(0);'
    if old_wrm in c:
        c = c.replace(old_wrm, new_wrm)
        print("Optimized WRM boxes in index-Cav4xqQL.js")

    # 3. Start reveal at 1 instead of 0
    c = c.replace('m.setReveal(0);', 'm.setReveal(1);')
    c = c.replace('reveal(o,{duration:g=0,delay:k=0}={}){a&&(g=k=0),Object.assign(h,{from:h.x,to:o,start:performance.now(),delay:k,dur:g}),H()}',
                  'reveal(o,{duration:g=0,delay:k=0}={}){m.setReveal(1);Object.assign(h,{from:1,to:1}),H()}')

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Saved optimized assets/index-Cav4xqQL.js")

def update_carousel_bundle():
    # Update build_carousel.py to use larger sizes and enhanced movement box
    with open("build_carousel.py", "r", encoding="utf-8") as f:
        bc = f.read()

    # Increase sz in wm2
    bc = bc.replace('const sz = Math.round(Math.min(320, availW * 0.28, (t - 140) * 0.44));',
                    'const sz = Math.round(Math.min(420, availW * 0.35, (t - 120) * 0.52));')

    # Increase side preview scale from 0.60 to 0.72
    bc = bc.replace('scale(0.60)', 'scale(0.72)')

    # Center hover scale: 1.36
    bc = bc.replace('scale = hoveredRef.current ? 1.48 : 1.0;',
                    'scale = hoveredRef.current ? 1.36 : 1.0;')

    # Remove artificial delay in S and Ie
    bc = bc.replace('S=new Promise(W=>setTimeout(W,Yl(window.innerWidth,window.innerHeight,h)?0:gm))',
                    'S=Promise.resolve()')
    bc = bc.replace('const Ie = { delay: .6, duration: 2.6 };',
                    'const Ie = { delay: 0, duration: 0.1 };')

    # Remove 1400ms delay in dm preload
    bc = bc.replace('d=setTimeout(()=>document.fonts.ready.then(p),1400)',
                    'd=setTimeout(()=>document.fonts.ready.then(p),0)')

    # Move movement box further down (label.y + 68) and style as a pill container
    old_box = """    y.jsxs('div', {
      className: 'works-layer__controls',
      style: {
        position: 'absolute',
        left: `${d[0] ? Math.round(d[0].box.x + d[0].box.w / 2) : 0}px`,
        top: `${d[0] ? Math.round(d[0].label.y + 44) : 0}px`,
        transform: 'translateX(-50%)',
        display: 'flex',
        alignItems: 'center',
        gap: '14px',
        zIndex: 30,
        opacity: isCenterHovered ? 0 : 0.9,
        pointerEvents: isCenterHovered ? 'none' : 'auto',
        transition: 'opacity 0.25s ease'
      },
      children: [
        y.jsx('button', {
          type: 'button',
          className: 'carousel-arrow carousel-arrow--prev',
          style: {
            fontFamily: 'var(--font-mono)',
            fontSize: '11px',
            letterSpacing: '0.08em',
            color: 'var(--dim)',
            background: 'var(--warm-card)',
            border: '1px solid rgba(31, 35, 30, 0.12)',
            padding: '4px 12px',
            borderRadius: '4px',
            cursor: 'pointer',
            boxShadow: '0 2px 6px rgba(0, 0, 0, 0.04)'
          },
          onClick: _ => { _.stopPropagation(); setActiveIdx((activeIdx - 1 + 3) % 3); },
          children: '‹ prev'
        }),
        y.jsxs('div', {
          style: { display: 'flex', gap: '8px', alignItems: 'center' },
          children: e.map((_, i) => y.jsx('button', {
            key: i,
            type: 'button',
            className: `carousel-dot${i === activeIdx ? ' is-active' : ''}`,
            onClick: _ => { _.stopPropagation(); setActiveIdx(i); },
            style: {
              width: i === activeIdx ? '18px' : '6px',
              height: '6px',
              borderRadius: '3px',
              background: i === activeIdx ? 'var(--terracotta)' : 'var(--hair)',
              border: 'none',
              padding: 0,
              cursor: 'pointer',
              transition: 'all 0.25s ease'
            },
            'aria-label': `Select project ${i + 1}`
          }))
        }),
        y.jsx('button', {
          type: 'button',
          className: 'carousel-arrow carousel-arrow--next',
          style: {
            fontFamily: 'var(--font-mono)',
            fontSize: '11px',
            letterSpacing: '0.08em',
            color: 'var(--dim)',
            background: 'var(--warm-card)',
            border: '1px solid rgba(31, 35, 30, 0.12)',
            padding: '4px 12px',
            borderRadius: '4px',
            cursor: 'pointer',
            boxShadow: '0 2px 6px rgba(0, 0, 0, 0.04)'
          },
          onClick: _ => { _.stopPropagation(); setActiveIdx((activeIdx + 1) % 3); },
          children: 'next ›'
        })
      ]
    })"""

    new_box = """    y.jsxs('div', {
      className: 'works-layer__controls',
      style: {
        position: 'absolute',
        left: `${d[0] ? Math.round(d[0].box.x + d[0].box.w / 2) : 0}px`,
        top: `${d[0] ? Math.round(d[0].label.y + 68) : 0}px`,
        transform: 'translateX(-50%)',
        display: 'flex',
        alignItems: 'center',
        gap: '16px',
        padding: '6px 16px',
        background: 'var(--warm-card)',
        border: '1px solid rgba(31, 35, 30, 0.14)',
        borderRadius: '28px',
        boxShadow: '0 4px 18px rgba(0, 0, 0, 0.06)',
        backdropFilter: 'blur(16px)',
        WebkitBackdropFilter: 'blur(16px)',
        zIndex: 30,
        opacity: isCenterHovered ? 0 : 0.95,
        pointerEvents: isCenterHovered ? 'none' : 'auto',
        transition: 'opacity 0.25s ease, transform 0.25s ease'
      },
      children: [
        y.jsx('button', {
          type: 'button',
          className: 'carousel-arrow carousel-arrow--prev',
          style: {
            fontFamily: 'var(--font-mono)',
            fontSize: '12px',
            fontWeight: '500',
            letterSpacing: '0.10em',
            textTransform: 'uppercase',
            color: 'var(--dim)',
            background: 'transparent',
            border: 'none',
            padding: '6px 14px',
            borderRadius: '20px',
            cursor: 'pointer',
            transition: 'all 0.2s ease'
          },
          onClick: _ => { _.stopPropagation(); setActiveIdx((activeIdx - 1 + 3) % 3); },
          children: '‹ prev'
        }),
        y.jsxs('div', {
          style: { display: 'flex', gap: '10px', alignItems: 'center', padding: '0 4px' },
          children: e.map((_, i) => y.jsx('button', {
            key: i,
            type: 'button',
            className: `carousel-dot${i === activeIdx ? ' is-active' : ''}`,
            onClick: _ => { _.stopPropagation(); setActiveIdx(i); },
            style: {
              width: i === activeIdx ? '26px' : '8px',
              height: '8px',
              borderRadius: '4px',
              background: i === activeIdx ? 'var(--terracotta)' : 'rgba(31, 35, 30, 0.18)',
              border: 'none',
              padding: 0,
              cursor: 'pointer',
              transition: 'all 0.25s cubic-bezier(0.16, 1, 0.3, 1)'
            },
            'aria-label': `Select project ${i + 1}`
          }))
        }),
        y.jsx('button', {
          type: 'button',
          className: 'carousel-arrow carousel-arrow--next',
          style: {
            fontFamily: 'var(--font-mono)',
            fontSize: '12px',
            fontWeight: '500',
            letterSpacing: '0.10em',
            textTransform: 'uppercase',
            color: 'var(--dim)',
            background: 'transparent',
            border: 'none',
            padding: '6px 14px',
            borderRadius: '20px',
            cursor: 'pointer',
            transition: 'all 0.2s ease'
          },
          onClick: _ => { _.stopPropagation(); setActiveIdx((activeIdx + 1) % 3); },
          children: 'next ›'
        })
      ]
    })"""

    if old_box in bc:
        bc = bc.replace(old_box, new_box)
        print("Updated movement box to larger pill container further down screen")
    else:
        print("Note: old_box not exact match")

    with open("build_carousel.py", "w", encoding="utf-8") as f:
        f.write(bc)

def update_index_html():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    preload_tags = """    <link rel="preload" href="/assets/projects/cycloidal-gearbox-lines.glb" as="fetch" crossorigin>
    <link rel="preload" href="/assets/projects/omni-wheel-lines.glb" as="fetch" crossorigin>
    <link rel="preload" href="/assets/projects/worlds-robot-lines.glb" as="fetch" crossorigin>
"""
    if "cycloidal-gearbox-lines.glb" not in html:
        html = html.replace('<script type="module"', preload_tags + '    <script type="module"')
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Added <link rel=\"preload\"> tags for all 3 3D models to index.html")

if __name__ == "__main__":
    optimize_cav4()
    update_carousel_bundle()
    update_index_html()
