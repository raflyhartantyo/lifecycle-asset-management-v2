# Zurich Brand Guidelines

These are the rules for making a Zurich app look Zurich-branded. They come from the Zurich Design System (ZDS). Where a value here conflicts with anything else, ZDS wins.

## 1. Colors

- Primary palette: Zurich Blue #2167AE, Dark Blue #23366F, Light Blue #91BFE3, Sand #DAD2BD, Dove #DDE4E3, Zurich White #ECEEEF, Pure White #FFFFFF.
- Mid Blue #5495CF is part of the primary palette, but it is never a text background. It fails contrast with both white and Dark Blue.
- Dark Blue is the black. Use Dark Blue for text. Pure black #000000 is for functional use only.
- Text on Zurich Blue or Dark Blue is Pure White. Text on White, Zurich White, or Dove is Dark Blue or Zurich Blue.
- Secondary accents: Moss, Teal, Mint, Lime, Lemon, Peach, Rust, Candy, Powder Pink, Lilac. Use one at a time, for accents and backgrounds only. Never on text, never over photos, and at most three per page.
- Semantic meaning: Moss = positive or active. Peach = caution or at risk. Rust = error.
- Status badges may use one semantic accent each.
- Interactive-state tints (hover and focus only): Dark Blue-80 #4F5E8C, Light Blue-40 #D3E5F4, Light Blue-10 #F4F9FC, Dove-80 #E4E9EC, Sky Blue-25 #C7EBF9.
- Grays: Gray-50 #2B2E31, Gray-40 #5D6162, Gray-30 #828A8B, Gray-20 #A6ADAF, Gray-10 #D3DADA.
- Modal scrim: Overlay-Black rgba(0,0,0,0.54). Alternative: Overlay-White rgba(255,255,255,0.89). Loading skeleton: gradient from Gray-20 to Dove.
- Sky Blue #1FB1E6 is the "Inclusive" color. Use it only with photography.

## 2. Typography

- Font: Zurich Sans for all text. Fallback: Arial, which is the brand-approved substitute.
- Digital scale: base size 16 px. Body text 14, 16, 18, or 20 px at 150% line height. Captions 12 to 20 px. Secondary headings 24, 28, or 32 px at 125%. Main headings 36 px and up at 116%.
- Letter spacing: 0%.
- Ogg (serif) is for one headline per screen only. Pair it with Zurich Sans Light. Never use it for body text, labels, or buttons.
- Weight pairing: Light body with Light or Medium headings. Regular with Regular or Semibold. Medium with Medium or Bold.

## 3. Logo

- The Zurich logo is the only logo. Do not create variations, lock-ups, or team or project logos. Any change needs Group Customer Office approval.
- Horizontal Blue on light backgrounds. Horizontal White on dark backgrounds.
- Clear space: about half the logo height on every side. Minimum height: about 8 mm.

## 4. Shape, surface, and space

- Flat, not heavy: white cards with a 1 px Dove border and at most a very faint shadow.
- Rounding: pill-shaped buttons and badges. About 16 px on cards. About 8 px on inputs.
- Shape language: one or two curve or circle moments per screen, such as a curved header edge or circular icon badges.
- Roomy layout: 16 to 24 px card padding. 24 px between form elements. 30 px horizontal and 32 px vertical gaps between cards.
- Page background is off-white. Content sits on white cards.

## 5. Components

- Buttons: one Primary button per screen. Other types: Secondary, Negative, Positive, Link, Ghost, and Action (icon). Pill radius. Icon-only buttons need a tooltip and a label. At least 8 px between buttons.
- Inputs: floating labels. Use helper text in preference to placeholder text. Nine states, including error and read-only. Error messages go above the form, and each field links to its message.
- Tables: native table markup. Sortable headers. Dove row banding.
- Navigation: top bar fill is Dove-80 #E4E9EC. Side bar widths are 256, 128, or 72 px. Bottom bar is for mobile only, with 2 to 5 items.
- Modal: overlay rgba(0,0,0,0.54). Dismissible, unless it is a critical alert. A sidebar drawer allows interaction with the page behind it.
- Notifications: an Alert needs manual dismissal. A Toast dismisses itself and is not interactive. Four statuses: info, positive, negative, alert. Each uses color, an icon, and text together.
- Tooltips: appear on hover and on focus, 8 px from the trigger, one or two sentences.
- Loader: shown only when the wait is longer than 1 second. Use a progress bar for steps with no count. Use a progress stepper for multi-step flows: done = Zurich Blue, active = Dark Blue, error = Peach, not started = Gray-10.
- Empty state: a graphic, a title, and one next step. Never more than one primary action.
- Touch and pointer targets: at least 24 by 24 px. 44 by 44 px is recommended.

## 6. Icons

- Use Zurich (ZDS) icons only. No emoji and no generic icon font in branded output.
- Outlined style for navigation and UI. Blue icons on light backgrounds, white icons on dark.
- Social-media icons keep their own brand colors.

## 7. Accessibility

WCAG 2.2 AA is the minimum standard.

- Text contrast: 4.5:1. Large text: 3:1. Meaningful icons, input borders, and UI components: 3:1.
- Passes for text: Dark Blue on White, Zurich White, Dove, Light Blue-10 or -40, Sky Blue-25 or -40. Zurich Blue on White, Zurich White, or Dove.
- Large text only: Mid Blue on White (3.6:1). Several secondary accents on light backgrounds.
- Fails for text: Light Blue and Sky Blue on most brand backgrounds.
- Focus indicator: visible, at least 2 px, contrast 3:1 or better, and distinct from hover.
- Color is never the only signal. Status uses an icon and text together.
- Forms: a label for every input. Errors shown in a summary above the form. Instructions refer to fields by name, not by position.
- Support High Contrast mode and 200% zoom. Respect reduced-motion settings.
- Icon-only controls and meaningful icons need labels. Decorative icons are hidden from assistive technology.

## 8. Do and do not

Do:
- Dark Blue text and Zurich Blue links.
- One semantic accent per context.
- White cards with thin borders.
- The real logo, unaltered.
- Generous white space.
- Ogg for one headline per screen.

Do not:
- Pure black text.
- Several bright accents at once.
- Heavy shadows or sharp corners.
- Emoji icons.
- A recolored or stretched logo.
- Ogg for body text.
- Mid Blue as a text background.
- Open Sans or other non-Zurich fonts.

## 9. Judging a screen

A Zurich screen is mostly white and off-white with blue. It is calm and spacious, with soft rounded shapes, Zurich icons, and the logo. It has no heavy shadows, no accent overload, and no pure black text.
