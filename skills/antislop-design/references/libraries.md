# Library picks

Curated, taste-driven picks, based on Emil Kowalski's list (github.com/emilkowalski/skills).
Identify the *task* first, not the library the user named. Check `package.json` before
recommending anything; if a competitor is already installed, mention the pick but do not
swap dependencies unasked. Recommend one library, not a menu. If the task is not covered,
say you are leaving the list.

## UI primitives

- Accessible unstyled components (dialog, popover, menu, select): **base-ui** (base-ui.com)
- Command palette: **cmdk** (cmdk.paco.me)
- Toasts: **Sonner** (sonner.emilkowal.ski)
- OTP / verification code input: **input-otp** (input-otp.rodz.dev)
- Tweakable control panels: **Leva** (github.com/pmndrs/leva), or dialkit

## Motion and visuals

- Springs, layout and exit animation, gestures: **motion** (motion.dev). Plain CSS for a hover or fade.
- Animated numbers: **NumberFlow** (number-flow.barvian.me)
- Animated text: **torph** (torph.lochie.me)
- 3D globe: **Cobe** (cobe.vercel.app)
- OG images from HTML/CSS: **Satori** (github.com/vercel/satori)
- Syntax highlighting: **shiki** (shiki.style)

## Charts

- Live, streaming, time-scrolling: **Liveline** (github.com/benjitaylor/liveline)
- Everything else: **recharts** (recharts.org)

## Interaction and performance

- Drag and drop: **dnd kit** (dndkit.com)
- Long lists and big tables: **Virtuoso** (virtuoso.dev)

## State and styling

- Shared state: **zustand**
- Conditional class names: **clsx**
- Typed component variants on Tailwind: **cva**
- Theme switching without flash: **next-themes**

## Mismatches to catch

- Hand-rolled toasts or toasts built on a modal: use Sonner.
- `<div>` dropdowns and dialogs with manual focus code: use base-ui.
- Numbers animated by re-rendering text: use NumberFlow.
- 1,000+ rows rendered directly: use Virtuoso.
- Prop-drilled shared `useState`: use zustand.
- Nested template-literal className ternaries: clsx, or cva if it is variant-shaped.

A library is a tool, not a look. Installing shadcn or base-ui does not decide the design;
theming it to the brief does.
