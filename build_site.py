import os, json, re, shutil

base_dir = r"c:\Users\Jack\Documents\portfolio"
ref_dir = os.path.join(base_dir, "reference_site")
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(os.path.join(assets_dir, "brand"), exist_ok=True)
os.makedirs(os.path.join(assets_dir, "projects"), exist_ok=True)
os.makedirs(os.path.join(assets_dir, "resume"), exist_ok=True)

# 1. Copy over static modules and CSS
shutil.copyfile(os.path.join(ref_dir, "assets", "index-Bc-C0UOT.css"), os.path.join(assets_dir, "index-Bc-C0UOT.css"))
shutil.copyfile(os.path.join(ref_dir, "assets", "meshopt_decoder.module-Bxwljyvj.js"), os.path.join(assets_dir, "meshopt_decoder.module-Bxwljyvj.js"))

# Copy placeholder glb models so 3D canvases work right now
sample_glb = os.path.join(ref_dir, "assets", "projects", "monitor-stand-lines.glb")
for glb_name in [
    "omni-wheel-lines.glb", "cycloidal-gearbox-lines.glb", "controller-lines.glb",
    "omni-wheel.glb", "cycloidal-gearbox.glb", "controller.glb"
]:
    dst = os.path.join(assets_dir, "projects", glb_name)
    if not os.path.exists(dst):
        shutil.copyfile(sample_glb, dst)

# 2. Build index.html
html_content = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" type="image/svg+xml" href="/assets/brand/jr-mark.svg" />
    <meta
      name="description"
      content="Jack Reiman. Mechanical Engineering student at the University of Washington. Specializing in mechanism design, CAD workflows, and rapid manufacturing."
    />
    <title>Jack Reiman</title>
    <meta name="theme-color" content="#f3f0e8" />

    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Jack Reiman" />
    <meta property="og:url" content="https://jackreiman.com/" />
    <meta property="og:title" content="Jack Reiman" />
    <meta property="og:description" content="Mechanical Engineering student at the University of Washington." />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Jack Reiman" />
    <meta name="twitter:description" content="Mechanical Engineering student at the University of Washington." />
    <script type="module" crossorigin src="/assets/index-BwGDr2zK.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-Bc-C0UOT.css">
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
"""
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)
print("Wrote index.html")

# 3. Process index-Cav4xqQL.js (3D figures)
with open(os.path.join(ref_dir, "assets", "index-Cav4xqQL.js"), "r", encoding="utf-8") as f:
    cav_js = f.read()

# Update URLs to point to Jack's glb models
cav_js = cav_js.replace("/assets/projects/frc-987-lines.glb", "/assets/projects/omni-wheel-lines.glb")
cav_js = cav_js.replace("/assets/projects/monitor-stand-lines.glb", "/assets/projects/cycloidal-gearbox-lines.glb")
cav_js = cav_js.replace("/assets/projects/rival-2025c-lines.glb", "/assets/projects/controller-lines.glb")

# Update ze mapping
# Original: ze={"frc-987-offseason":Ze,"low-profile-monitor-stand":Qe,"rival-robotics-2024":rt}
old_ze = 'ze={"frc-987-offseason":Ze,"low-profile-monitor-stand":Qe,"rival-robotics-2024":rt}'
new_ze = 'ze={"omni-wheel":Ze,"cycloidal-gearbox":Qe,"custom-leverless-controller":rt,"frc-987-offseason":Ze,"low-profile-monitor-stand":Qe,"rival-robotics-2024":rt}'
if old_ze in cav_js:
    cav_js = cav_js.replace(old_ze, new_ze)
    print("Replaced ze mapping successfully")
else:
    print("Warning: old_ze not found directly")

with open(os.path.join(assets_dir, "index-Cav4xqQL.js"), "w", encoding="utf-8") as f:
    f.write(cav_js)
print("Wrote index-Cav4xqQL.js")

# 4. Process index-BwGDr2zK.js (Main React app)
with open(os.path.join(ref_dir, "assets", "index-BwGDr2zK.js"), "r", encoding="utf-8") as f:
    main_js = f.read()

# Prepare new projects JSON string
jack_projects = [
  {
    "slug": "omni-wheel",
    "index": 1,
    "title": "Toray Carbon Fiber Omni Wheel",
    "discipline": "Robotics & Composites",
    "year": "2025 \u2013 Present",
    "date": "ARUW R&D",
    "tags": ["RoboMaster", "SolidWorks", "ANSYS FEA", "Toray Carbon Fiber", "OMAX Waterjet", "SLA Tooling"],
    "lede": "Lightweight competition omni wheel pairing Toray 3900 prepreg carbon fiber plates with an aluminum core to slash rotational inertia under extreme shock loads.",
    "preview": "/assets/projects/omni-wheel-wireframe.png",
    "hero": "/assets/projects/omni-wheel-hero.png",
    "plant": "conifer",
    "model": "/assets/projects/omni-wheel-lines.glb",
    "summary": "An advanced competition omni wheel engineered for Advanced Robotics at UW (ARUW). Built to survive severe shock loads while drastically reducing rotational inertia, the design pairs CNC-routed Toray 3900 prepreg carbon fiber rim plates with a waterjet-cut 6061 aluminum hub core, custom polyurethane rollers, and SLA-printed master mold tooling.",
    "facts": [
      {"label": "Role", "value": "Lead Mechanical Designer / R&D"},
      {"label": "Team", "value": "Advanced Robotics @ UW (ARUW)"},
      {"label": "Software", "value": "SolidWorks, ANSYS Mechanical, KeyShot"},
      {"label": "Manufacturing", "value": "OMAX Waterjet, CNC Routing, Formlabs SLA, Prepreg Layup"}
    ],
    "overview": [
      "Competition robots experience severe shock loads and violent direction shifts from driving off elevated ramps and making instantaneous starts and stops. Commercial off-the-shelf wheels were either too fragile or carried excessive rim mass that penalized acceleration.",
      "I engineered a composite-metal hybrid wheel that places mass where it does structural work and removes it where it penalizes inertia. By pairing Toray 3900 prepreg carbon fiber outer rim plates with a 6061-T6 structural aluminum hub, we achieved high torsional rigidity with a dramatic reduction in rotational inertia."
    ],
    "goals": [
      "Survive repeated drop loads and shock impacts from arena ramps",
      "Minimize rotational inertia to maximize drivetrain responsiveness",
      "Eliminate roller scrubbing and axial diameter mismatch",
      "Validate composite stress states in ANSYS before manufacturing",
      "Standardize hole wizard and hardware libraries for the wider team"
    ],
    "process": [
      {
        "heading": "Hybrid Architecture & Structural CAD",
        "body": [
          "The wheel architecture relies on CNC-routed Toray 3900 prepreg carbon fiber rim plates sandwiching a lightweight structural aluminum central hub.",
          "SolidWorks master sketches defined roller contact circles, pin clearances, and spoke load paths so rim diameter changes updated all tooling parametrically."
        ]
      },
      {
        "heading": "Finite Element Validation (ANSYS)",
        "body": [
          "I used ANSYS Mechanical to simulate extreme landing impact load cases and multi-axis drop scenarios before cutting any prepreg stock.",
          "Composite laminate failure criteria and von Mises stress plots confirmed a Factor of Safety (FOS) > 2.0 across all critical bearing mount ears and rim fasteners."
        ]
      },
      {
        "heading": "Custom Tooling & Polyurethane Rollers",
        "body": [
          "Off-the-shelf rollers suffered from scrubbing and inconsistent outer diameters that induced chassis vibration.",
          "I designed custom polyurethane rollers and multi-cavity silicone molds using high-precision Formlabs Form 3 SLA master models, achieving zero axial slop and perfect diameter matching."
        ]
      },
      {
        "heading": "Fabrication & Assembly",
        "body": [
          "The central mounting hub was waterjet-machined out of structural aluminum on a campus OMAX waterjet.",
          "Carbon fiber plates were CNC-routed and post-processed in the UW composite shop, then assembled with stainless shoulder hardware and low-friction sealed bearings."
        ]
      }
    ],
    "techStack": [
      {"label": "CAD", "value": "SolidWorks"},
      {"label": "Simulation", "value": "ANSYS Mechanical (FEA)"},
      {"label": "Materials", "value": "Toray 3900 Prepreg Carbon Fiber, 6061-T6 Al, Polyurethane"},
      {"label": "Fabrication", "value": "OMAX Waterjet, CNC Mill, Formlabs Form 3 SLA"}
    ]
  },
  {
    "slug": "cycloidal-gearbox",
    "index": 2,
    "title": "19:1 Low-Backlash Cycloidal Gearbox",
    "discipline": "Mechanism Design",
    "year": "2025 \u2013 Present",
    "date": "ARUW R&D",
    "tags": ["SolidWorks", "Formlabs Tough 2000 SLA", "KeyShot", "Tolerancing & DFM", "DJI M3508"],
    "lede": "Custom 19:1 cycloidal speed reducer engineered for DJI M3508 motors to eliminate planetary backlash in high-speed robot turret yaw control.",
    "preview": "/assets/projects/cycloidal-gearbox-wireframe.png",
    "hero": "/assets/projects/cycloidal-gearbox-hero.jpg",
    "plant": "cedar",
    "model": "/assets/projects/cycloidal-gearbox-lines.glb",
    "summary": "Stock planetary gearboxes on our DJI M3508 brushless motors suffered from excessive backlash and were too tall to package inside the robot's turret yaw envelope. I designed a custom 19:1 low-backlash cycloidal speed reducer with dual eccentric drive shafts and 3D-printed rapid SLA prototypes using Formlabs Tough 2000 resin to validate tolerances prior to production.",
    "facts": [
      {"label": "Role", "value": "Mechanism & Gear Designer"},
      {"label": "Team", "value": "Advanced Robotics @ UW (ARUW)"},
      {"label": "Software", "value": "SolidWorks, KeyShot"},
      {"label": "Prototyping", "value": "Formlabs Form 3 SLA (Tough 2000 Resin)"}
    ],
    "overview": [
      "Turret yaw control on RoboMaster competition robots demands tight angular tracking. Even small amounts of gearbox backlash get amplified over the barrel length, degrading aiming stability at high speed.",
      "The stock planetary gearboxes from DJI were tall, bulky, and suffered from 15+ arcminutes of backlash. I replaced them with a custom 19:1 cycloidal gearbox featuring a low-profile flat output plate and dual out-of-phase cycloidal discs."
    ],
    "goals": [
      "Achieve 19:1 reduction in a package less than half the stock planetary height",
      "Minimize angular backlash for precision turret pointing",
      "Cancel radial eccentric vibration forces using dual discs 180\u00b0 apart",
      "Iterate tolerances rapidly using functional SLA resin prototypes"
    ],
    "process": [
      {
        "heading": "Epitrochoidal Profile & Kinematic Design",
        "body": [
          "The cycloidal disc tooth profiles were derived analytically and plotted parametrically in SolidWorks to ensure continuous multi-tooth contact under load.",
          "Two cycloidal discs operating 180\u00b0 out-of-phase on dual eccentric lobes completely cancel dynamic imbalance and divide tooth shear loads."
        ]
      },
      {
        "heading": "Rapid Functional SLA Prototyping",
        "body": [
          "To validate bearing press-fits, pin engagement, and tooth rolling clearances before expensive metal CNC machining, I printed all internal components on a Formlabs Form 3 using Tough 2000 engineering resin.",
          "Testing the 3D-printed resin assemblies under motor drive allowed rapid tuning of profile offset tolerances down to +/- 0.025 mm for smooth, bind-free output."
        ]
      },
      {
        "heading": "Packaging & Flat Output Integration",
        "body": [
          "Unlike tall planetary stacks, this gearbox integrates needle roller pins and an output flange directly into the chassis turret mount.",
          "The flat profile moved the gimbal's center of gravity downward, improving robot stability during aggressive acceleration."
        ]
      }
    ],
    "techStack": [
      {"label": "Software", "value": "SolidWorks, KeyShot"},
      {"label": "Add Mfg", "value": "Formlabs Form 3 SLA (Tough 2000 Resin)"},
      {"label": "Actuation", "value": "DJI M3508 Brushless Motor"},
      {"label": "Disciplines", "value": "Cycloidal Kinematics, DFM, Precision Tolerancing"}
    ]
  },
  {
    "slug": "custom-leverless-controller",
    "index": 3,
    "title": "Custom Leverless Competition Controller",
    "discipline": "Hardware & Ergonomics",
    "year": "Nov 2025",
    "date": "Personal Project",
    "tags": ["SolidWorks", "FDM Additive Mfg", "Raspberry Pi Pico", "C++ Firmware", "Soldering"],
    "lede": "Custom low-profile, tournament-legal all-button competition controller modeled from scratch in SolidWorks with hand-fitted ergonomic keycaps.",
    "preview": "/assets/projects/controller-hero.jpg",
    "hero": "/assets/projects/controller-alt.jpg",
    "plant": "fern",
    "model": "/assets/projects/controller-lines.glb",
    "summary": "Designed and fabricated a custom low-profile all-button arcade controller for competitive Super Smash Bros. Melee from scratch. The ergonomic clamshell enclosure and custom keycap profiles were sculpted in SolidWorks to match my hand anatomy, reducing finger travel and latency during tournament play.",
    "facts": [
      {"label": "Role", "value": "Industrial Design, CAD & Electronics"},
      {"label": "Project Type", "value": "Solo Personal Project"},
      {"label": "Software", "value": "SolidWorks, KeyShot"},
      {"label": "Hardware", "value": "Raspberry Pi Pico, Kailh Hotswap, Gateron Yellows"}
    ],
    "overview": [
      "Traditional controllers cause significant hand strain and tendon fatigue during high-APM competitive play. Commercial all-button box controllers are often flat, clunky slabs with generic button spacings that don't match natural hand ergonomics.",
      "I designed a custom controller from scratch in SolidWorks. By modeling around the natural rest arcs of fingers and designing custom low-profile keycaps, finger travel is minimized and inputs register with minimal physical effort."
    ],
    "goals": [
      "Sculpt an ergonomic button layout tailored to natural hand rest positions",
      "Model custom low-travel keycaps that prevent accidental edge catches",
      "Engineer a rigid two-piece FDM printed clamshell with hidden fasteners",
      "Hand-wire modular hotswap switch sockets for easy maintenance"
    ],
    "process": [
      {
        "heading": "Ergonomic Layout & CAD Sculpting",
        "body": [
          "I measured resting finger spreads and modeled the layout on radial arcs rather than a rigid grid, placing primary thumb and pinky modifiers within effortless reach.",
          "The enclosure was designed as a snap-and-fasten two-piece housing in SolidWorks with integrated internal ribbing for table-top rigidity."
        ]
      },
      {
        "heading": "Additive Manufacturing & Keycaps",
        "body": [
          "Both the housing halves and the concave keycaps were 3D printed via FDM with tight tolerances to ensure zero keycap rattle and consistent bottom-out feel.",
          "Keycap walls were optimized for smooth vertical actuation through switch-plate cutouts."
        ]
      },
      {
        "heading": "Hand-Wired Electronics & Embedded Firmware",
        "body": [
          "Individual Kailh hotswap sockets were hand-wired with linear Gateron Yellow mechanical switches to a Raspberry Pi Pico microcontroller.",
          "The board was flashed with low-latency open-source firmware configured for competition legality and sub-1ms polling."
        ]
      }
    ],
    "techStack": [
      {"label": "CAD", "value": "SolidWorks"},
      {"label": "Manufacturing", "value": "FDM 3D Printing, Hand Soldering"},
      {"label": "Electronics", "value": "Raspberry Pi Pico, Kailh Hotswap, Gateron Yellow"},
      {"label": "Firmware", "value": "Open Source Low-Latency C++"}
    ]
  }
]

jack_pm_str = "const Pm=" + json.dumps(jack_projects, ensure_ascii=False) + ";"

# Replace Pm
pos_pm_start = main_js.find('const Pm=[')
pos_pm_end = main_js.find(';', pos_pm_start)
main_js = main_js[:pos_pm_start] + jack_pm_str + main_js[pos_pm_end+1:]
print("Replaced Pm array successfully")

# Replace Brand Icon
main_js = main_js.replace('/assets/brand/anura.svg', '/assets/brand/jr-mark.svg')

# Replace Place / Clock
main_js = main_js.replace('place:e="Las Vegas, NV"', 'place:e="Seattle, WA"')

# Replace Name
main_js = main_js.replace('"Daniel Kaliko"', '"Jack Reiman"')
main_js = main_js.replace('`Daniel Kaliko`', '`Jack Reiman`')

# Replace Bio & Location
main_js = main_js.replace(
    'Studying engineering at the University of Nevada, Reno.',
    'Mechanical Engineering student at the University of Washington (GPA: 3.51).'
)
main_js = main_js.replace(
    'Based in Las Vegas, Nevada.',
    'Based in Seattle, Washington.'
)

# Replace About paragraph
old_about = '["Competed and mentored with"," ",y.jsx("a",{className:"link",href:"https://www.team987.com/",target:"_blank",rel:"noopener noreferrer",children:"FRC Team 987"}),"."]'
new_about = '["R&D Team Member at Advanced Robotics @ UW (ARUW), engineering composite omni wheels and low-backlash cycloidal drivetrains."]'
main_js = main_js.replace(old_about, new_about)

# Remove old portfolio link or point to UW / LinkedIn
old_prev = 'y.jsxs("p",{children:["Previous portfolio:"," ",y.jsx("a",{href:fm,className:"link",children:"old.danielkaliko.com\\xa0\\u2192"})]})'
new_prev = 'y.jsxs("p",{children:["Robotics R&D:"," ",y.jsx("a",{href:"https://aruw.org/",target:"_blank",rel:"noopener noreferrer",className:"link",children:"Advanced Robotics @ UW\\xa0\\u2197"})]})'
main_js = main_js.replace(old_prev, new_prev)

# Replace Contact Section
# Email component: pm()
# Replace Jp().then(...) with immediate email
old_pm = 'function pm(){const[e,t]=z.useState("");return z.useEffect(()=>{let n=!0;return Jp().then(r=>{n&&t(r)}).catch(()=>{}),()=>{n=!1}},[]),e?y.jsx("a",{className:"link",href:`mailto:${e}`,children:e}):y.jsx("span",{className:"quiet",children:"\u2026"})}'
new_pm = 'function pm(){return y.jsx("a",{className:"link",href:"mailto:reimanja@uw.edu",children:"reimanja@uw.edu"})}'
main_js = main_js.replace(old_pm, new_pm)

# Replace github link
main_js = main_js.replace('https://github.com/okkdaniel', 'https://github.com/jackreiman')
main_js = main_js.replace('"@okkdaniel"', '"@jackreiman"')

# Replace linkedin link
main_js = main_js.replace('https://www.linkedin.com/in/daniel-kaliko/', 'https://www.linkedin.com/in/jack-reiman/')
main_js = main_js.replace('"/in/daniel-kaliko"', '"/in/jack-reiman"')

# Replace resume path
main_js = main_js.replace('/assets/resume/resume.pdf', '/assets/resume/Jack_Reiman_Resume.pdf')

with open(os.path.join(assets_dir, "index-BwGDr2zK.js"), "w", encoding="utf-8") as f:
    f.write(main_js)
print("Wrote index-BwGDr2zK.js")
