import os

def main():
    with open('assets/index-D9v2kLm8.js', 'r', encoding='utf-8') as f:
        text = f.read()

    idx1 = text.find('const f=z.useRef(null);')
    idx2 = text.find('function km(e){')

    assert idx1 != -1, "idx1 not found"
    assert idx2 != -1, "idx2 not found"

    replacement = """const [activeIdx, setActiveIdx] = z.useState(1);
const [isCenterHovered, setCenterHovered] = z.useState(!1);
const activeRef = z.useRef(activeIdx);
activeRef.current = activeIdx;
const hoveredRef = z.useRef(isCenterHovered);
hoveredRef.current = isCenterHovered;

z.useEffect(() => {
  const onKey = ev => {
    if (ev.key === 'ArrowLeft') setActiveIdx(i => (i - 1 + 3) % 3);
    else if (ev.key === 'ArrowRight') setActiveIdx(i => (i + 1) % 3);
  };
  window.addEventListener('keydown', onKey);
  return () => window.removeEventListener('keydown', onKey);
}, []);

z.useEffect(() => {
  if (t) {
    const idx = e.findIndex(p => p.slug === t);
    if (idx !== -1) setActiveIdx(idx);
  }
}, [t, e]);

z.useEffect(() => {
  const centerSlug = e[activeIdx]?.slug;
  for (const [slug, fig] of Object.entries(u.current)) {
    if (slug === centerSlug && isCenterHovered && !i) {
      fig == null || fig.hover(!0);
    } else {
      fig == null || fig.hover(!1);
    }
  }
}, [activeIdx, isCenterHovered, i, e]);

z.useEffect(() => {
  if (isCenterHovered) {
    n(e[activeIdx]?.slug ?? null);
  } else {
    n(null);
  }
}, [isCenterHovered, activeIdx]);

const applyCarousel = () => {
  if (!d || d.length !== 3) return;
  const ce = document.querySelector('.ov-head')?.getBoundingClientRect();
  const side = ce ? Math.max(340, ce.right + 24) : 340;
  const rightMargin = 40;
  const availW = Math.max(400, window.innerWidth - side - rightMargin);
  const spread = Math.round(availW * 0.33);

  e.forEach((item, idx) => {
    const slug = item.slug;
    const fig = document.querySelector(`.works-layer__fig[data-slug="${slug}"]`);
    const spot = document.querySelector(`.works-layer__spot[data-slug="${slug}"]`);
    const lbl = spot ? spot.querySelector('.works-layer__label') : null;
    const slot = (idx - activeRef.current + 3) % 3;

    if (slot === 0) {
      const scale = hoveredRef.current ? 1.36 : 1.0;
      if (fig) {
        fig.style.transform = `translate3d(0px, 0px, 0px) scale(${scale})`;
        fig.style.opacity = '1';
        fig.style.zIndex = '25';
        fig.style.pointerEvents = 'none';
      }
      if (lbl) {
        lbl.style.transform = hoveredRef.current ? 'translate3d(0px, 45px, 0px) scale(1.08)' : 'translate3d(0px, 0px, 0px) scale(1)';
        lbl.style.opacity = '1';
        lbl.style.zIndex = '25';
      }
      if (spot) {
        spot.style.transform = `translate3d(0px, 0px, 0px) scale(${scale})`;
        spot.style.opacity = '1';
        spot.style.zIndex = '25';
        spot.style.pointerEvents = 'auto';
        spot.style.cursor = 'pointer';
      }
    } else if (slot === 1) {
      if (fig) {
        fig.style.transform = `translate3d(${spread}px, 0px, 0px) scale(0.72)`;
        fig.style.opacity = hoveredRef.current ? '0' : '0.45';
        fig.style.zIndex = '5';
        fig.style.pointerEvents = 'none';
      }
      if (lbl) {
        lbl.style.transform = 'translate3d(0px, 0px, 0px) scale(0.92)';
        lbl.style.opacity = hoveredRef.current ? '0' : '0.7';
        lbl.style.zIndex = '5';
      }
      if (spot) {
        spot.style.transform = `translate3d(${spread}px, 0px, 0px) scale(0.72)`;
        spot.style.opacity = hoveredRef.current ? '0' : '0.45';
        spot.style.zIndex = '10';
        spot.style.pointerEvents = hoveredRef.current ? 'none' : 'auto';
        spot.style.cursor = 'pointer';
      }
    } else if (slot === 2) {
      if (fig) {
        fig.style.transform = `translate3d(-${spread}px, 0px, 0px) scale(0.72)`;
        fig.style.opacity = hoveredRef.current ? '0' : '0.45';
        fig.style.zIndex = '5';
        fig.style.pointerEvents = 'none';
      }
      if (lbl) {
        lbl.style.transform = 'translate3d(0px, 0px, 0px) scale(0.92)';
        lbl.style.opacity = hoveredRef.current ? '0' : '0.7';
        lbl.style.zIndex = '5';
      }
      if (spot) {
        spot.style.transform = `translate3d(-${spread}px, 0px, 0px) scale(0.72)`;
        spot.style.opacity = hoveredRef.current ? '0' : '0.45';
        spot.style.zIndex = '10';
        spot.style.pointerEvents = hoveredRef.current ? 'none' : 'auto';
        spot.style.cursor = 'pointer';
      }
    }
  });
};

z.useEffect(() => {
  applyCarousel();
}, [activeIdx, isCenterHovered, d]);

z.useEffect(() => {
  const onResize = () => applyCarousel();
  window.addEventListener('resize', onResize);
  return () => window.removeEventListener('resize', onResize);
}, []);

z.useEffect(() => { i && c.current(); }, [i]);

const m = x => ({ left: `${x.x}px`, top: `${x.y}px`, width: `${x.w}px`, height: `${x.h}px` }),
      v = z.useRef(null),
      N = {
        onPointerDown: x => { x.pointerType !== 'mouse' && (v.current = { x: x.clientX, y: x.clientY, moved: !1 }, x.currentTarget.setPointerCapture(x.pointerId)); },
        onPointerMove: x => {
          var $; const _ = v.current;
          if (x.pointerType !== 'mouse' && (! _ || (Math.hypot(x.clientX - _.x, x.clientY - _.y) > 8 && (_.moved = !0), ! _.moved))) return;
          const C = x.currentTarget.dataset.slug, P = x.currentTarget.getBoundingClientRect(), R = I => Math.min(1, Math.max(0, I));
          ($ = u.current[C]) == null || $.point(R((x.clientX - P.left) / P.width), R((P.bottom - x.clientY) / P.height));
        },
        onPointerUp: x => {
          var C; const _ = v.current;
          _ && (_.moved && ((C = u.current[x.currentTarget.dataset.slug]) == null || C.leave()), v.current = _.moved ? { cancelClick: !0 } : null);
        },
        onClick: x => {
          var _; (_ = v.current) != null && _.cancelClick && (x.preventDefault(), v.current = null);
        }
      };

return y.jsxs('div', {
  className: `works-layer${w && !i ? ' works-layer--shown' : ''}${i ? ' works-layer--leaving' : ''}${o ? ' works-layer--dimmed' : ''}`,
  children: [
    y.jsx('div', {
      className: 'works-layer__backdrop',
      onClick: r,
      onPointerEnter: () => setCenterHovered(!1),
      'aria-hidden': 'true'
    }),
    y.jsx('canvas', { ref: a, className: 'works-layer__ink', 'aria-hidden': 'true' }),
    y.jsx('div', { ref: s, className: 'works-layer__figs' }),
    d.map((x, idx) => {
      const slot = (idx - activeIdx + 3) % 3;
      return y.jsx(z.Fragment, {
        children: y.jsx('a', {
          className: `works-layer__spot${t === x.slug ? ' is-hot' : ''}`,
          href: `#work/${x.slug}`,
          style: m({ x: Math.min(x.box.x, x.label.x), y: x.box.y, w: Math.max(x.box.w, x.label.w), h: x.label.y + x.label.h - x.box.y }),
          'data-slug': x.slug,
          ...N,
          onPointerEnter: _ => {
            if (_.pointerType === 'mouse') {
              if (slot === 0) {
                setCenterHovered(!0);
              } else {
                const fig = document.querySelector(`.works-layer__fig[data-slug="${x.slug}"]`);
                if (fig) fig.style.opacity = '0.75';
                _.currentTarget.style.opacity = '0.75';
              }
            }
          },
          onPointerLeave: _ => {
            if (_.pointerType === 'mouse') {
              if (slot === 0) {
                setCenterHovered(!1);
                var C; (C = u.current[x.slug]) == null || C.leave();
              } else {
                const fig = document.querySelector(`.works-layer__fig[data-slug="${x.slug}"]`);
                if (fig) fig.style.opacity = isCenterHovered ? '0' : '0.45';
                _.currentTarget.style.opacity = isCenterHovered ? '0' : '0.45';
              }
            }
          },
          onClick: _ => {
            if (slot === 1) {
              _.preventDefault();
              _.stopPropagation();
              setActiveIdx((activeIdx + 1) % 3);
            } else if (slot === 2) {
              _.preventDefault();
              _.stopPropagation();
              setActiveIdx((activeIdx - 1 + 3) % 3);
            }
          },
          onFocus: () => n(x.slug),
          onBlur: () => n(null),
          children: y.jsx('span', {
            className: 'works-layer__label',
            style: { left: `${x.label.x - Math.min(x.box.x, x.label.x)}px`, top: `${x.label.y - x.box.y}px`, width: `${x.label.w}px` },
            children: x.text
          })
        })
      }, x.slug);
    }),
    y.jsxs('div', {
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
    })
  ]
});
}
const vm = [[.390, .730, .320], [.615, .240, .440], [.840, .730, .340]],
      Nu = [[[.28, .18], [.72, .38], [.3, .83]], [[.7, .17], [.3, .38], [.68, .84]]],
      Yl = (e, t, n) => !n && e > t * 1.1;
function wm(e, t, n, r, l) {
  if (Yl(e, t, l) && r === 3) return vm.map(([g, w, k]) => ({ cx: e * g, cy: t * w, size: Math.min(520, e * k, t * .48) }));
  const o = al(`works-layout/${fs}`), i = ld + od + 12, a = l ? 18 : 44,
        s = { x0: a, y0: n ? n.bottom + 24 : a, x1: e - a, y1: t - (l ? 60 : 80) },
        u = s.x1 - s.x0, c = s.y1 - s.y0,
        p = r === 3 ? Nu[Math.floor(o() * Nu.length)] : Array.from({ length: r }, (g, w) => [(w + .5) / r, w % 2 ? .3 : .7]),
        d = Math.min(240, u * .55, c * .24);
  return Array.from({ length: r }, (g, w) => {
    const [k, T] = p[w], h = d * (.85 + o() * .3),
          f = Math.min(s.x1 - h / 2, Math.max(s.x0 + h / 2, s.x0 + u * k)),
          m = Math.min(s.y1 - h / 2 - i, Math.max(s.y0 + h / 2, s.y0 + c * T));
    return { cx: f, cy: m, size: h };
  });
}
function wm2(e, t, n, r, l, figs) {
  if (!(Yl(e, t, l) && r === 3)) return wm(e, t, n, r, l);
  const side = n ? Math.max(340, n.right + 24) : 340;
  const rightMargin = 40;
  const availW = Math.max(400, e - side - rightMargin);
  const cx_center = Math.round(side + availW * 0.5);
  const cy_mid = Math.round(t * 0.50) - 20;
  const sz = Math.round(Math.min(420, availW * 0.35, (t - 120) * 0.52));
  return [
    { cx: cx_center, cy: cy_mid + 20, size: sz },
    { cx: cx_center, cy: cy_mid + 4, size: sz },
    { cx: cx_center, cy: cy_mid - 16, size: sz }
  ];
}
"""

    new_text = text[:idx1] + replacement + text[idx2:]

    # New cache-busted filename for JS
    new_js_name = "assets/index-C4r0u5eL.js"
    with open(new_js_name, 'w', encoding='utf-8') as out:
        out.write(new_text)
    print(f"Wrote {new_js_name}, size: {len(new_text)}")

    # Update index-D9v2kLm8.js and index-BwGDr2zK.js as well
    with open("assets/index-D9v2kLm8.js", 'w', encoding='utf-8') as out:
        out.write(new_text)
    with open("assets/index-BwGDr2zK.js", 'w', encoding='utf-8') as out:
        out.write(new_text)

    # Update CSS
    with open("assets/index-Bc-C0UOT.css", 'r', encoding='utf-8') as f:
        css = f.read()

    css_additions = """
/* 3D Carousel Navigation */
.works-layer__controls {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 14px;
  z-index: 30;
  transition: opacity 0.25s var(--ease);
}
.carousel-arrow {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.08em;
  color: var(--dim);
  background: var(--warm-card);
  border: 1px solid rgba(31, 35, 30, 0.12);
  padding: 4px 12px;
  border-radius: 4px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
  transition: all 0.2s var(--ease);
  cursor: pointer;
  user-select: none;
}
.carousel-arrow:hover {
  color: var(--terracotta);
  border-color: var(--terracotta);
  box-shadow: 0 2px 10px rgba(217, 75, 50, 0.18);
  transform: translateY(-1px);
}
.carousel-dot {
  height: 6px;
  border-radius: 3px;
  border: none;
  padding: 0;
  cursor: pointer;
  transition: all 0.25s var(--ease);
}
.carousel-dot.is-active {
  width: 18px;
  background: var(--terracotta);
}
.carousel-dot:not(.is-active) {
  width: 6px;
  background: var(--hair);
}
.carousel-dot:not(.is-active):hover {
  background: var(--dim);
}
"""
    if ".carousel-arrow" not in css:
        css += css_additions

    new_css_name = "assets/index-C4r0u5eL.css"
    with open(new_css_name, 'w', encoding='utf-8') as out:
        out.write(css)
    with open("assets/index-E5x7Qp1N.css", 'w', encoding='utf-8') as out:
        out.write(css)
    with open("assets/index-Bc-C0UOT.css", 'w', encoding='utf-8') as out:
        out.write(css)
    print(f"Wrote {new_css_name}, size: {len(css)}")

    # Update index.html
    with open("index.html", 'r', encoding='utf-8') as f:
        html = f.read()

    import re
    html = re.sub(r'src="/assets/index-[^"]+\.js"', 'src="/assets/index-C4r0u5eL.js"', html)
    html = re.sub(r'href="/assets/index-[^"]+\.css"', 'href="/assets/index-C4r0u5eL.css"', html)

    with open("index.html", 'w', encoding='utf-8') as out:
        out.write(html)
    print("Updated index.html with new bundle hashes.")

if __name__ == "__main__":
    main()
