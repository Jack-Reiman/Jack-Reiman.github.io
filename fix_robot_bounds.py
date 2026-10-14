import re

def main():
    # 1. Update index-Cav4xqQL.js: set WRC scale to 0.75
    with open("assets/index-Cav4xqQL.js", "r", encoding="utf-8") as f:
        cav = f.read()

    cav = cav.replace('scale:0.98', 'scale:0.75')
    with open("assets/index-Cav4xqQL.js", "w", encoding="utf-8") as f:
        f.write(cav)
    print("Updated WRC scale in assets/index-Cav4xqQL.js")

    # 2. Update apply_latest_carousel.py
    with open("apply_latest_carousel.py", "r", encoding="utf-8") as f:
        alc = f.read()

    alc = alc.replace("const scale = hoveredRef.current ? 1.36 : 1.0;",
                      "const maxScale = slug === 'worlds-robot' ? 1.15 : 1.36; const scale = hoveredRef.current ? maxScale : 1.0;")

    old_wm2 = """function wm2(e, t, n, r, l, figs) {
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
}"""

    new_wm2 = """function wm2(e, t, n, r, l, figs) {
  if (!(Yl(e, t, l) && r === 3)) return wm(e, t, n, r, l);
  const side = n ? Math.max(340, n.right + 24) : 340;
  const rightMargin = 40;
  const availW = Math.max(400, e - side - rightMargin);
  const cx_center = Math.round(side + availW * 0.5);
  const cy_mid = Math.round(t * 0.50) - 10;
  const sz = Math.round(Math.min(420, availW * 0.35, (t - 120) * 0.50));
  return [
    { cx: cx_center, cy: cy_mid + 20, size: sz },
    { cx: cx_center, cy: cy_mid + 4, size: sz },
    { cx: cx_center, cy: cy_mid + 30, size: Math.round(sz * 0.78) }
  ];
}"""

    if old_wm2 in alc:
        alc = alc.replace(old_wm2, new_wm2)
        print("Updated wm2 in apply_latest_carousel.py")
    else:
        print("Note: old_wm2 not exact match in apply_latest_carousel.py")

    # New cache-buster tag
    new_tag = "K7mQ2pX9"
    alc = alc.replace('bundle_tag = "V8kL9mZ2"', f'bundle_tag = "{new_tag}"')

    with open("apply_latest_carousel.py", "w", encoding="utf-8") as f:
        f.write(alc)

    print(f"Prepared apply_latest_carousel.py with tag {new_tag}")

if __name__ == "__main__":
    main()
