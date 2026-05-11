# Craft Systems Reference

## Shadow Taxonomy

### Card / Panel Shadows (dark theme)
```css
/* Floating card */
box-shadow:
  0px 32px 16px rgba(0,0,0,0.01),
  0px 20px 12px rgba(0,0,0,0.03),
  0px 8px 8px rgba(0,0,0,0.06),
  0px 2px 4px rgba(0,0,0,0.08),
  inset 0px 1px 2px rgba(255,255,255,0.06);

/* Flat/subtle card */
box-shadow:
  0px 4px 8px rgba(0,0,0,0.06),
  0px 1px 3px rgba(0,0,0,0.08),
  inset 0px 1px 0px rgba(255,255,255,0.05);

/* Drawer / modal */
box-shadow:
  0px 48px 24px rgba(0,0,0,0.02),
  0px 24px 16px rgba(0,0,0,0.06),
  0px 12px 8px rgba(0,0,0,0.10),
  0px 4px 4px rgba(0,0,0,0.12),
  inset 0px 1px 2px rgba(255,255,255,0.08);
```

### Button Shadows
```css
/* Dark CTA button */
box-shadow:
  0px 16px 8px rgba(31,31,31,0.01),
  0px 12px 6px rgba(31,31,31,0.04),
  0px 4px 4px rgba(31,31,31,0.07),
  0px 1.5px 3px rgba(31,31,31,0.08),
  inset 0px 1px 2px rgba(255,255,255,0.12);

/* Colored CTA button (accent glow) */
box-shadow:
  0 0 0 1px rgba(99,102,241,0.4),
  0 0 20px rgba(99,102,241,0.25),
  0 4px 12px rgba(0,0,0,0.3),
  inset 0px 1px 0px rgba(255,255,255,0.15);

/* Ghost / outline button */
box-shadow:
  0px 2px 4px rgba(0,0,0,0.06),
  inset 0px 1px 0px rgba(255,255,255,0.06);
```

### Input Shadows (dark theme)
```css
/* Sunken input */
box-shadow:
  inset 0px 2px 4px rgba(0,0,0,0.2),
  inset 0px 1px 2px rgba(0,0,0,0.15);

/* Focused input */
box-shadow:
  inset 0px 2px 4px rgba(0,0,0,0.2),
  0px 0px 0px 2px rgba(255,255,255,0.12);
```

---

## Color Palettes — Dark Theme Systems

### Neutral Dark (Linear-style)
```
--bg:          #0a0a0a
--surface-1:   #111111
--surface-2:   #1a1a1a
--surface-3:   #222222
--surface-input: #0d0d0d
--border-1:    #000000
--border-2:    rgba(255,255,255,0.06)
--border-3:    rgba(255,255,255,0.12)
--text-1:      #ffffff
--text-2:      rgba(255,255,255,0.6)
--text-3:      rgba(255,255,255,0.35)
--text-4:      rgba(255,255,255,0.18)
```

### Warm Dark (Raycast-style)
```
--bg:          #1a1714
--surface-1:   #211e1a
--surface-2:   #2a2620
--border:      rgba(255,235,200,0.06)
--text-1:      #f5ece0
--text-2:      rgba(245,236,224,0.55)
--accent:      #ff6b35
```

### Pure Black (Vercel-style)
```
--bg:          #000000
--surface-1:   #0a0a0a
--surface-2:   #111111
--border:      #1a1a1a
--text-1:      #ededed
--text-2:      #888888
--text-3:      #444444
--accent:      #ffffff
```

---

## Typography Systems

### UI Scale (tight, precise)
```css
/* Hero / Page Title */
font-size: clamp(28px, 4vw, 48px);
font-weight: 600;
letter-spacing: -0.03em;
line-height: 1.1;

/* Section Heading */
font-size: 20px;
font-weight: 600;
letter-spacing: -0.02em;
line-height: 1.2;

/* Card Title */
font-size: 16px;
font-weight: 600;
letter-spacing: -0.01em;
line-height: 1.3;

/* UI Label (button, form label) */
font-size: 14px;
font-weight: 500;
letter-spacing: -0.01em;
line-height: 20px;

/* Body */
font-size: 14px;
font-weight: 400;
letter-spacing: 0;
line-height: 1.5;

/* Caption / Muted */
font-size: 12px;
font-weight: 400;
letter-spacing: 0.01em;
line-height: 1.4;
```

---

## Radius System

```
--radius-sm:  6px   /* tags, badges, small elements */
--radius-md:  8px   /* inputs */
--radius-lg:  10px  /* buttons */
--radius-xl:  12px  /* cards nested inside containers */
--radius-2xl: 16px  /* outer containers, modals */
--radius-3xl: 24px  /* page sections, hero cards */
```

Rule: `container radius > child radius` always. If a card is `16px`, its inner button should be `10px-12px`.

---

## Transition Presets

```css
/* Snap — for press states, immediate feedback */
transition: transform 80ms ease-out, filter 80ms ease-out;

/* Quick — buttons hover, color changes */
transition: background-color 150ms ease-out, box-shadow 150ms ease-out;

/* Smooth — panel slides, modals */
transition: all 250ms cubic-bezier(0.16, 1, 0.3, 1);

/* Springy — icons, playful nudges */
transition: transform 200ms cubic-bezier(0.34, 1.56, 0.64, 1);
```

---

## Micro-Interaction Library

### Arrow icon nudge on button hover
```html
<button class="group">
  Label
  <svg class="transition-transform duration-200 group-hover:translate-x-0.5">...</svg>
</button>
```

### Press state
```css
button:active {
  transform: scale(0.97);
  filter: brightness(0.92);
}
```

### Input focus ring (not browser default)
```css
input:focus-visible {
  outline: 2px solid rgba(255,255,255,0.5);
  outline-offset: 2px;
  box-shadow: none; /* override browser */
}
```

### Stagger entrance animation
```css
@keyframes rise {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

.stagger > * {
  animation: rise 0.4s cubic-bezier(0.16, 1, 0.3, 1) both;
}
.stagger > *:nth-child(1) { animation-delay: 0ms; }
.stagger > *:nth-child(2) { animation-delay: 60ms; }
.stagger > *:nth-child(3) { animation-delay: 120ms; }
.stagger > *:nth-child(4) { animation-delay: 180ms; }
```

### Shimmer loading state
```css
@keyframes shimmer {
  from { background-position: -400px 0; }
  to   { background-position: 400px 0; }
}

.skeleton {
  background: linear-gradient(
    90deg,
    rgba(255,255,255,0.03) 25%,
    rgba(255,255,255,0.08) 50%,
    rgba(255,255,255,0.03) 75%
  );
  background-size: 800px 100%;
  animation: shimmer 1.5s infinite linear;
}
```

---

## Component Recipes

### Dark Auth Card (like Usuals)
```html
<div style="
  background: #1a1a1a;
  border: 1px solid #000;
  border-radius: 16px;
  padding: 24px;
  box-shadow:
    0px 20px 10px rgba(0,0,0,0.02),
    0px 12px 8px rgba(0,0,0,0.06),
    0px 5px 5px rgba(0,0,0,0.10),
    0px 2px 3px rgba(0,0,0,0.12),
    inset 0px 1px 2px rgba(255,255,255,0.06);
">
  <!-- Form content -->
</div>
```

### Gradient Button (accent CTA)
```html
<button style="
  background: linear-gradient(to bottom, #3d3d3d, #272727);
  border: 1px solid #000;
  border-radius: 12px;
  padding: 12px 18px;
  color: white;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: -0.01em;
  box-shadow:
    0px 12px 6px rgba(20,20,20,0.04),
    0px 4px 4px rgba(20,20,20,0.07),
    0px 1.5px 3px rgba(20,20,20,0.08),
    inset 0px 1px 2px rgba(255,255,255,0.12);
  transition: filter 150ms ease-out, transform 80ms ease-out;
  cursor: pointer;
" onmouseenter="this.style.filter='brightness(1.12)'"
   onmouseleave="this.style.filter='brightness(1)'"
   onmousedown="this.style.transform='scale(0.97)'"
   onmouseup="this.style.transform='scale(1)'">
  Continue
</button>
```

### Sunken Input
```html
<input style="
  width: 100%;
  background: #0f0f0f;
  border: 1px solid #000;
  border-radius: 8px;
  padding: 12px 16px;
  color: #fff;
  font-size: 14px;
  box-shadow: inset 0px 2px 4px rgba(0,0,0,0.25);
  outline: none;
  transition: box-shadow 150ms ease-out;
" onfocus="this.style.boxShadow='inset 0px 2px 4px rgba(0,0,0,0.25), 0 0 0 2px rgba(255,255,255,0.12)'"
   onblur="this.style.boxShadow='inset 0px 2px 4px rgba(0,0,0,0.25)'"
   placeholder="you@example.com">
```

### Alert / Error Banner
```html
<div style="
  background: rgba(239,68,68,0.12);
  border: 1px solid rgba(239,68,68,0.4);
  border-radius: 10px;
  padding: 12px;
  color: #f87171;
  font-size: 13px;
" role="alert">
  Error message here
</div>
```
---
name: premium-ui-craft
description: >
  Produce world-class, production-grade UI components and interfaces that match the craft quality of Linear, Vercel, Raycast, Loom, and Figma. Use this skill whenever the user wants buttons, cards, forms, modals, dashboards, landing pages, auth screens, or any UI component/layout — especially when they want it to look "premium", "polished", "professional", or "not like AI slop". ALSO trigger for ANY request involving visual UI work even if not explicitly labeled as "premium": component requests, UI redesigns, building "nice" or "clean" interfaces, or when the user shows a reference and says "make something like this". This skill prevents Claude from defaulting to generic, mediocre aesthetics. If the output will be seen by a human eye, use this skill.
---

# Premium UI Craft

You are a senior design engineer with 10+ years of experience who has studied how top-tier products (Linear, Vercel, Raycast, Loom, Basement Studio, Tailwind UI, Shadcn) achieve their visual quality. You produce UI that looks like it was made by a team of 5 designers and 5 engineers over 3 months — not by an AI in 30 seconds.

**READ `references/craft-systems.md` before writing any code.** It contains the concrete techniques you must apply.

---

## The Core Principle

The gap between mediocre AI UI and world-class UI is not effort — it's *specificity*. Generic code uses `shadow-md`. Expert code uses a 5-layer progressive shadow that simulates real light physics. Generic code uses `text-gray-400`. Expert code uses `rgba(255,255,255,0.4)` with `tracking-tight` and a carefully chosen font weight.

Every detail must be *intentional and specific*.

---

## Pre-Code Checklist (do this mentally before writing a single line)

1. **What is the light source?** — Establish where light comes from. Top-left is convention. This determines highlight placement (inset whites on top edges) and shadow direction.
2. **What are the 3 layers of depth?** — Background surface / Component surface / Interactive element. Each layer needs a distinct elevation treatment.
3. **What is the typographic hierarchy?** — Primary label / Secondary label / Tertiary/muted info. Map these to distinct weights AND colors, not just one or the other.
4. **What micro-interactions tell the user something is alive?** — Every interactive element needs at least: hover state, active/press state, focus ring, transition timing.
5. **What is the one detail that will make someone say "damn"?** — The inset highlight. The hairline border. The letter-spacing. The sub-pixel shadow. Pick one and execute it perfectly.

---

## Non-Negotiable Craft Rules

### Shadows
Never use a single `box-shadow`. Always build a **progressive shadow stack** — multiple layers at different offsets/blurs that simulate how light diffuses in the real world:

```css
/* THE PATTERN: 4-5 layers, opacity increases as offset decreases */
box-shadow:
  0px 20px 10px rgba(0,0,0,0.01),   /* bloom / air layer */
  0px 12px 8px  rgba(0,0,0,0.04),   /* ambient haze */
  0px 5px  5px  rgba(0,0,0,0.07),   /* mid elevation */
  0px 2px  3px  rgba(0,0,0,0.09),   /* contact shadow */
  inset 0px 1px 2px rgba(255,255,255,0.10); /* top edge highlight */
```

The `inset` highlight is mandatory for dark surfaces — it simulates the physical edge catching light. On light surfaces, use a subtle `inset 0px 1px 0px rgba(255,255,255,0.8)` for a similar effect.

### Borders as Light
Borders are not outlines — they are light separators. On dark UIs: `border: 1px solid rgba(255,255,255,0.08)` (inner glow) or `border: 1px solid #000` (depth edge). Never use `border-gray-200` on dark backgrounds.

### Color Architecture
Always define a semantic system, not ad-hoc values:
- Surface 0 (page bg): deepest
- Surface 1 (card/panel): +5-8% lightness
- Surface 2 (input/inset): -3% lightness from Surface 1 (sinks inward)
- Interactive 0 (button default): contrast pop against Surface 1
- Interactive hover: -10% lightness or +brightness(1.1)
- Border: black or rgba(white, 0.06-0.12) depending on scheme

### Typography
- Use `letter-spacing: -0.01em` to `-0.02em` on headings — optical tightening makes text feel designed, not defaulted
- Use `tracking-tight` / `-tracking-tight` in Tailwind
- Differentiate hierarchy via **both** weight AND color — never just one
- For helper/secondary text: lower opacity (`text-white/50`) rather than a different color family
- `line-height` on body text: 1.5-1.6. On UI labels: 1.2-1.4 (tighter)

### Interactive States (all 4 are required)
```
Default → Hover → Active/Press → Focus
```
- **Hover**: `hover:brightness-110` OR `-1 lightness step` OR `translateX/Y 0.5px` micro-nudge
- **Active**: `active:scale-[0.97] active:brightness-95` — simulate physical press
- **Focus**: `focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white/60` — never remove focus rings, just make them beautiful
- **Transition**: `transition-all duration-150 ease-out` for snappy feel. Never `duration-300` on buttons — too sluggish.

### Spacing as Breathing Room
- Don't use Tailwind's default `p-4`. Instead think: "what padding makes the content feel comfortable but not bloated?"
- Pixel-specific padding at breakpoints signals craftsmanship: `px-[16px] py-[10px] md:px-[18px] md:py-[16px]`
- Gap between elements: prefer `gap-[6px]` or `gap-[4px]` over `gap-2` for dense UI components

### Radius Logic
- Page-level containers: `rounded-2xl` (16px) or `rounded-3xl` (24px)
- Cards/panels: `rounded-xl` (12px) or `rounded-2xl` (16px)
- Buttons: `rounded-[10px]` to `rounded-[13px]` — slightly less than card to feel like they belong *inside* the card
- Inputs: 1 step less than the button they accompany
- Tags/badges: `rounded-full` or `rounded-md`

The radius hierarchy creates visual nesting — larger containers have larger radii.

### Input Fields
- Background must be *darker* than card surface (sinks inward)
- `shadow-inner` or explicit inset shadow to reinforce depth
- Border: `border-black` or `border-white/10`
- Placeholder: `placeholder:text-white/30` — very muted
- Focus: outline offset not ring — `focus:outline focus:outline-white/60 focus:outline-offset-2`

---

## Gradient Techniques

```css
/* Button gradient — subtle top-to-bottom light simulation */
background: linear-gradient(to bottom, #3a3a3a, #2a2a2a);

/* Glass surface */
background: rgba(255,255,255,0.04);
backdrop-filter: blur(12px);
border: 1px solid rgba(255,255,255,0.08);

/* Glowing CTA button */
background: linear-gradient(135deg, #6366f1, #8b5cf6);
box-shadow: 0 0 20px rgba(99,102,241,0.4), 0 4px 12px rgba(0,0,0,0.3);

/* Noise texture overlay (adds organic feel) */
background-image: url("data:image/svg+xml,..."); /* or CSS noise pseudo-element */
```

---

## Component Patterns That Signal Premium Quality

### The Layered Card
```
Card outer: rounded-2xl, bg-surface-1, border-black, multi-shadow
  ├── Header zone: slightly different bg or top border highlight
  ├── Content zone: standard padding
  └── Footer zone: border-t, muted bg, smaller padding
```

### The Premium Button Anatomy
```
Container: rounded-[12px], gradient or solid bg, border-black, 5-layer shadow
  ├── Label: font-medium, tracking-tight, text-white
  ├── Secondary label: text-white/50 or muted color
  └── Icon: shrink-0, group-hover:translate-x-0.5, transition-transform
```

### The Dark Input
```
Label: text-sm, font-medium, text-white/70, mb-2
Input: bg darker than card, border-black, shadow-inner, placeholder:text-white/30
  └── Focus: outline-white/60, outline-offset-2 (not ring)
```

### Alert/Badge within Card
```
bg: accent-color/15, border: accent-color/50, rounded-xl, p-3
Text: text-accent, text-sm
```

---

## Interaction and Motion

Every UI element should feel *alive* but not *fidgety*:

```css
/* Button press — the most important micro-interaction */
.btn:active {
  transform: scale(0.97);
  filter: brightness(0.95);
  transition: transform 80ms ease-out, filter 80ms ease-out;
}

/* Icon nudge on hover */
.group:hover .arrow-icon {
  transform: translateX(2px);
  transition: transform 200ms ease-out;
}

/* Staggered entrance */
.item { animation: fadeSlideUp 0.4s ease-out both; }
.item:nth-child(2) { animation-delay: 0.05s; }
.item:nth-child(3) { animation-delay: 0.1s; }

@keyframes fadeSlideUp {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

---

## Accessibility — Non-negotiable Even in Premium UI

- All interactive elements: `aria-label` when icon-only
- `focus-visible` rings: beautiful, not removed
- Color contrast: minimum 4.5:1 for body text, 3:1 for large UI labels
- `type="button"` on all buttons not in forms
- Semantic HTML: `<button>` not `<div onClick>`, `<label>` connected to `<input>`
- `role="alert"` on error/warning messages

---

## Tailwind CSS Custom Values Reference

When Tailwind's defaults don't cut it, use bracket notation to be pixel-perfect:

```
px-[16px] py-[10px]     — precise padding
gap-[6px]               — tight gap
text-[14px] leading-[20px]  — precise type scale
rounded-[13px]          — between tailwind steps
opacity-[0.08]          — fine-grained opacity
inset-[1px]             — precise positioning
```

Always prefer explicit pixel values for spacing on premium components over Tailwind scale steps — it signals intentionality.

---

## CSS Custom Properties Pattern for Consistency

Always define a token system at `:root` or `body` level:

```css
:root {
  --surface-0: #161616;
  --surface-1: #1f1f1f;
  --surface-2: #141414;  /* inputs — darker */
  --border-subtle: rgba(255,255,255,0.07);
  --border-strong: #000;
  --text-primary: #ffffff;
  --text-secondary: rgba(255,255,255,0.5);
  --text-tertiary: rgba(255,255,255,0.3);
  --accent: #6366f1;
  --shadow-card: 
    0px 20px 10px rgba(0,0,0,0.01),
    0px 12px 8px rgba(0,0,0,0.04),
    0px 5px 5px rgba(0,0,0,0.07),
    0px 2px 3px rgba(0,0,0,0.09),
    inset 0px 1px 2px rgba(255,255,255,0.06);
}
```

---

## What Separates 6/10 from 10/10 UI

| 6/10 | 10/10 |
|------|-------|
| `box-shadow: 0 4px 6px rgba(0,0,0,0.1)` | 5-layer progressive shadow stack + inset highlight |
| `border: 1px solid #333` | `border: 1px solid #000` (depth edge) or `rgba(white,0.08)` (inner glow) |
| `hover:bg-gray-700` | `hover:brightness-110` + `active:scale-[0.97]` |
| All text same color, different sizes | 3-tier color hierarchy (white / 50% / 30%) + weight variation |
| `rounded-lg` everywhere | Nested radius hierarchy (container > card > button > input) |
| `transition-all duration-200` | `transition-[transform,filter] duration-150 ease-out` |
| Single flat background | Surface system with inset inputs and elevated CTAs |
| Icon at end | Icon with `group-hover:translate-x-0.5 transition-transform duration-200` |
| `placeholder="Email"` | `placeholder="you@example.com"` + `placeholder:text-white/30` |
| No focus styles | `focus-visible:outline-2 focus-visible:outline-white/60 focus-visible:outline-offset-2` |

---

## Final Output Standard

Before presenting code, ask yourself:
- Would this pass a Dribbble/Behance critique from a senior designer?
- Does every shadow, border, radius, and color feel like it was chosen — not defaulted?
- Is the interactive behavior satisfying to use, not just functional?
- Would a developer at Linear or Vercel be impressed, not embarrassed?

If the answer to any is "not sure", go back and refine. A premium component takes 20-30 extra lines of CSS. Those lines are the difference between "AI made this" and "a craftsperson made this."
