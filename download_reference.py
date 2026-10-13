import urllib.request, os, re

os.makedirs('reference_site/assets/projects', exist_ok=True)
os.makedirs('reference_site/assets/brand', exist_ok=True)

# List of all assets
assets = [
    '/',
    '/assets/index-BwGDr2zK.js',
    '/assets/index-Bc-C0UOT.css',
    '/assets/index-Cav4xqQL.js',
    '/assets/meshopt_decoder.module-Bxwljyvj.js',
    '/assets/brand/anura.svg',
    '/assets/projects/frc-987-offseason.png',
    '/assets/projects/frc-987-offseason-wireframe.png',
    '/assets/projects/frc-987-offseason.glb',
    '/assets/projects/frc-987-lines.glb',
    '/assets/projects/monitor-stand-render.png',
    '/assets/projects/monitor-stand-wireframe.png',
    '/assets/projects/monitor-stand.glb',
    '/assets/projects/monitor-stand-lines.glb',
    '/assets/projects/rival-robotics-2024.png',
    '/assets/projects/rival-robotics-2024-wireframe.png',
    '/assets/projects/rival-2025c-lines.glb',
    '/og.jpg'
]

for a in assets:
    url = 'https://www.danielkaliko.com' + a
    dest = 'reference_site' + ('/index.html' if a == '/' else a)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if not os.path.exists(dest):
        try:
            print(f"Downloading {url} -> {dest}")
            urllib.request.urlretrieve(url, dest)
            print(f"Done: {os.path.getsize(dest)} bytes")
        except Exception as e:
            print(f"Failed {url}: {e}")
