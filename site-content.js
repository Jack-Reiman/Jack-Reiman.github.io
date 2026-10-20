/**
 * ==============================================================================
 * PORTFOLIO CONTENT & METADATA CONFIGURATION
 * ==============================================================================
 * 
 * Welcome! This file contains all user-facing text, profile details, bio,
 * contact links, and project metadata across the entire portfolio site.
 * 
 * ------------------------------------------------------------------------------
 * HOW TO EDIT THIS FILE:
 * ------------------------------------------------------------------------------
 * • Local Editing:
 *     Open this file in VS Code, Sublime Text, Notepad, or any code editor.
 *     Modify any text inside quotation marks "..." or backticks `...`.
 *     Save the file and refresh your browser (F5 or Ctrl+R) — your changes
 *     appear immediately without any build or compile step!
 * 
 * • Editing Directly on GitHub:
 *     1. Navigate to this file (`site-content.js`) in your repository.
 *     2. Press the '.' (period) key to launch GitHub's web editor, or click the
 *        pencil icon ("Edit this file").
 *     3. Edit your content, then commit changes.
 *     4. When deployed, your live site reflects the changes immediately.
 * 
 * ------------------------------------------------------------------------------
 * CONFIGURATION SECTIONS:
 * ------------------------------------------------------------------------------
 * 1. profile  : Your name, professional title, location (shown in the clock), etc.
 * 2. about    : Array of bullet paragraphs displayed inside the About drawer.
 * 3. contact  : Links shown inside the Contact drawer (email, phone, LinkedIn, résumé).
 * 4. projects : Catalog of projects with title, lede, tags, facts table, and gallery.
 *               Note: To preserve interactive 3D CAD models and animations, keep
 *               the `slug` identifiers ("omni-wheel", "cycloidal-gearbox", "worlds-robot").
 * ==============================================================================
 */

window.SITE_CONTENT = {
  // --- Profile & Header Metadata ---
  profile: {
    name: "Jack Reiman",
    title: "Mechanical Engineering Student",
    tagline: "Specializing in mechanism design, CAD workflows, and rapid manufacturing.",
    location: "Seattle, WA",
    university: "University of Washington",
    siteUrl: "https://jackreiman.com/"
  },

  // --- About Drawer Paragraphs ---
  // Each string in this array renders as a distinct paragraph inside the About drawer.
  about: [
    "Mechanical Engineering student at the University of Washington.",
    "Based in Seattle, Washington.",
    "R&D Team Member at Advanced Robotics @ UW (ARUW).",
    "VEX Worlds Division Champion (2025) Team Lead.",
    "Focusing on mechanism design, rapid prototyping, and CAD modeling."
  ],

  // --- Contact Links Drawer ---
  // Each item in this list renders as a labeled link inside the Contact drawer.
  // Set external: true to open the link in a new browser tab.
  contact: [
    {
      label: "email",
      text: "reimanja@uw.edu",
      href: "mailto:reimanja@uw.edu",
      external: false
    },
    {
      label: "phone",
      text: "(509) 306-9852",
      href: "tel:5093069852",
      external: false
    },
    {
      label: "linkedin",
      text: "/in/jack-reiman",
      href: "https://www.linkedin.com/in/jack-reiman/",
      external: true
    },
    {
      label: "résumé",
      text: "pdf ↗",
      href: "/assets/resume/Jack_Reiman_Resume.pdf",
      external: true
    }
  ],

  // --- Projects Catalog ---
  // Array of project showcase entries. Order is determined by the `index` property.
  projects: [
    {
      slug: "omni-wheel",
      index: 1,
      title: "Composite Omni Wheel",
      shortTitle: "Omni Wheel",
      discipline: "Robotics & Composites",
      year: "2026",
      date: "2026",
      tags: ["RoboMaster", "SolidWorks", "ANSYS FEA", "Carbon Fiber", "Waterjet"],
      lede: "Lightweight competition omni wheel pairing Toray 3900 prepreg carbon fiber plates with an aluminum core to slash rotational inertia under extreme shock loads.",
      preview: "/assets/projects/omni-wheel-wireframe.png",
      hero: "/assets/projects/omni-wheel-hero.png",
      plant: "conifer",
      model: "/assets/projects/omni-wheel-lines.glb",
      facts: [
        { label: "Role", value: "Lead Mechanical Designer / R&D" },
        { label: "Team", value: "Advanced Robotics @ UW (ARUW)" },
        { label: "Software", value: "SolidWorks, ANSYS Mechanical, KeyShot" },
        { label: "Manufacturing", value: "OMAX Waterjet, CNC Routing, Form 3 SLA" }
      ],
      gallery: [
        {
          src: "/assets/projects/omni-wheel-hero.png",
          caption: "Full Assembly Render — Dual Toray 3900 prepreg carbon fiber plates clamping polyurethane rollers with 6061-T6 aluminum hub",
          featured: true
        },
        {
          src: "/assets/projects/omni-wheel-ansys.png",
          caption: "ANSYS Mechanical FEA — Von Mises stress distribution under peak dynamic drop impact loads (FOS > 2.0)",
          featured: false
        },
        {
          src: "/assets/projects/omni-wheel-cad-iso.png",
          caption: "CAD Architecture — Exploded view detailing custom roller retention, sealed bearings, and stainless shoulder bolts",
          featured: true
        },
        {
          src: "/assets/projects/omni-wheel-cad-bracket.png",
          caption: "Hub Pocket Detail — Precision CNC pocketing for weight reduction and torsional stiffness",
          featured: false
        }
      ]
    },
    {
      slug: "cycloidal-gearbox",
      index: 2,
      title: "DJI M3508 Cycloidal Gearbox",
      shortTitle: "Cycloidal Gearbox",
      discipline: "Mechanism Design",
      year: "2026",
      date: "2026",
      tags: ["SolidWorks", "Formlabs Tough 2000 SLA", "KeyShot", "Tolerancing & DFM", "DJI M3508"],
      lede: "Custom 19:1 cycloidal speed reducer engineered for DJI M3508 motors to eliminate planetary backlash in high-speed robot turret yaw control.",
      preview: "/assets/projects/cycloidal-gearbox-wireframe.png",
      hero: "/assets/projects/cycloidal-gearbox-hero.jpg",
      plant: "cedar",
      model: "/assets/projects/cycloidal-gearbox-lines.glb",
      facts: [
        { label: "Role", value: "Mechanism & Gear Designer" },
        { label: "Team", value: "Advanced Robotics @ UW (ARUW)" },
        { label: "Software", value: "SolidWorks, KeyShot" },
        { label: "Prototyping", value: "Formlabs Form 3 SLA (Tough 2000 Resin)" }
      ],
      gallery: [
        {
          src: "/assets/projects/cycloidal-gearbox-hero.jpg",
          caption: "KeyShot Turret Assembly — Compact 19:1 speed reducer packaged directly onto the DJI M3508 brushless motor",
          featured: true
        },
        {
          src: "/assets/projects/cycloidal-gearbox-wireframe.png",
          caption: "Exploded Mechanism CAD — Dual 180° out-of-phase cycloidal discs, eccentric bearing shafts, and needle roller pins",
          featured: true
        },
        {
          src: "/assets/projects/cycloidal-gearbox-prototype.jpg",
          caption: "Functional SLA Prototype — Formlabs Form 3 print in Tough 2000 engineering resin validating rolling tolerances",
          featured: false
        },
        {
          src: "/assets/projects/cycloidal-gearbox-exploded.png",
          caption: "Engineering Blueprints — Comprehensive GD&T fabrication drawing sheets and critical bearing fits",
          featured: false
        }
      ]
    },
    {
      slug: "worlds-robot",
      index: 3,
      title: "VEX Worlds 2025 Division Champion Robot",
      shortTitle: "Worlds Robot",
      discipline: "Robotics & Mechanism Design",
      year: "2024-2025",
      date: "Team 61002G",
      tags: ["Fusion 360", "Laser Cutting", "Polycarbonate", "Pneumatics", "PID / Odometry"],
      lede: "High-speed competitive robot engineered for rapid mobile-goal clamp cycles, high-clearance wall climbing, and sub-second ring intake indexing.",
      preview: "/assets/projects/worlds-robot-arm.jpg",
      hero: "/assets/projects/worlds-robot-arm.jpg",
      plant: "fern",
      model: "/assets/projects/worlds-robot-lines.glb",
      facts: [
        { label: "Achievement", value: "2025 VEX Worlds Division Champion" },
        { label: "Team", value: "Team 61002G Lead CAD / Mech Design" },
        { label: "Software", value: "Fusion 360, SolidWorks" },
        { label: "Manufacturing", value: "Laser Cutting, CNC Polycarbonate, 3D Printing" }
      ],
      gallery: [
        {
          src: "/assets/projects/worlds-robot-arm.jpg",
          caption: "Team 61002G Competition Robot — Division Champion chassis with elastic-assisted 4-bar climber mechanism",
          featured: true
        },
        {
          src: "/assets/projects/worlds-robot-hero.jpg",
          caption: "High-Throughput Intake — Curved heat-formed polycarbonate guides and high-velocity roller chain indexing",
          featured: false
        },
        {
          src: "/assets/projects/worlds-robot-clamp.jpg",
          caption: "Pneumatic Clamping — Over-center dual-acting cylinder latch for instant zero-play mobile goal capture",
          featured: false
        },
        {
          src: "/assets/projects/worlds-robot-intake.jpg",
          caption: "Championship Superstructure — Millimeter-accurate packaging maximizing speed, reliability, and autonomous scoring",
          featured: true
        }
      ]
    }
  ]
};
