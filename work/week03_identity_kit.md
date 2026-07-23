# Week 3 — Identity kit

**Track card:** [Decide Once: Build Your Identity Kit](https://aifluency.flyrank.ai/week-03.html#identity-kit)  
**Live CSS source:** `docs/styles.css` (do not invent a second system)

---

## One-page kit

### Type (2 fonts)

| Role | Font | Source |
|---|---|---|
| Heading | **Fraunces** (500/600) | [Google Fonts](https://fonts.google.com/specimen/Fraunces) |
| Body | **Source Sans 3** (400/600/700) | [Google Fonts](https://fonts.google.com/specimen/Source+Sans+3) |

### Palette (4 colors)

| Role | Hex | Swatch use |
|---|---|---|
| Near-black text | `#14201a` | Body and headings |
| Near-white / paper | `#f4f1ea` | Page background |
| Main / accent | `#0b5f45` | Buttons, links, favicon field |
| Soft white (cards) | `#fffdf8` | Work cards, raised surfaces |

Muted secondary text `#3d4a42` and focus ring `#c45c26` stay in CSS for readability/a11y only — **not** brand colors. One accent on the page: green.

### Logo / favicon

| Asset | Path |
|---|---|
| Wordmark (name in heading font) | `docs/img/logo.svg` |
| Favicon (HI monogram on green) | `docs/favicon.svg` |
| Visual one-pager (screenshot this) | `docs/identity-kit.html` |

### Two-line style note (paste into Claude Project)

```
Fonts: Fraunces for headings, Source Sans 3 for body. Colors: text #14201a, background #f4f1ea, accent #0b5f45, cards #fffdf8.
Mood: calm editorial frame — cream paper, one forest-green accent — so the ranked-queue proof is louder than the chrome.
```

---

## Pass check

| Criterion | Hit |
|---|---|
| One or two fonts | Fraunces + Source Sans 3 |
| Tight palette with hex | Four named hexes above |
| Logo or favicon exists | `logo.svg` + `favicon.svg` |
| Style note = one mood that frames work | Calm editorial; work stays loudest |

## Claude Project — add under existing instructions

Paste the two-line style note after the proof statement block so every later page build inherits the same frame.
