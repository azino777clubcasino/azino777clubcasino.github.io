# Duel Casino — Multi-region SEO Portal

Ultra-fast static review site for the Duel Casino brand. Pure HTML5 + CSS + vanilla JS — no frameworks, no build step at runtime.

## Locales (11 pages)

| Path | Language | Target market |
|------|----------|---------------|
| `/` | English | Global / Canada (en, en-ca) |
| `/no/` | Norsk | Norway — *beste krypto casino norge* |
| `/de/` | Deutsch | Germany — *Duel Casino Test & Bonus* |
| `/fi/` | Suomi | Finland — *parhaat krypto kasinot* |
| `/da/` | Dansk | Denmark |
| `/is/` | Íslenska | Iceland |
| `/fr/` | Français | France |
| `/it/` | Italiano | Italy |
| `/nl/` | Nederlands | Netherlands |
| `/be/` | Nederlands (BE) | Belgium (nl-BE) |
| `/ch/` | Deutsch (CH) | Switzerland (de-CH) |

## SEO features

- **Reciprocal hreflang** on every page (12 alternates + `x-default`)
- **Self-referencing canonical** URL on every page
- **JSON-LD** schemas: `Organization`, `Review`, `Product` with `AggregateRating` (4.9★ — golden stars in SERP), `FAQPage`, `BreadcrumbList`
- **Semantic HTML5**: `<header> <main> <section> <article> <footer>`, strict H1→H4 hierarchy
- **Open Graph + Twitter Card** meta on every page
- **sitemap.xml** with hreflang xhtml:link entries on the home URL
- **robots.txt** pointing to sitemap

## Performance

- System font stack (zero font requests, FOUT-proof)
- Single CSS file (~9 KB), single JS file (~1.5 KB)
- All images include `width`/`height` (CLS = 0)
- Inline JSON-LD (no extra requests)
- Mobile-first CSS, breakpoints at 720px and 980px
- `prefers-reduced-motion` honored
- Target: 100/100 Core Web Vitals

## UI / UX

- Dark mode: `#060a13` base, neon green `#00ff88` accent, gold `#ffd166` for stars
- Mobile sticky CTA "Play Duel Casino" (hidden on desktop)
- Click-to-copy promo codes (`DUEL200`, `DUELFREE`, `CASHDUEL`)
- Comparison table: Duel Casino vs average crypto casino
- Trustpilot / Reddit-style review cards
- FAQ as `<details>`/`<summary>` (accessible, no JS needed for collapse)
- Language switcher dropdown in header

## Affiliate links

All "Play" CTAs are direct anchors — no hidden redirects:

```html
<a href="https://duel.com/?ref=duelreview" target="_blank" rel="nofollow noopener noreferrer">Play Duel Casino</a>
```

## Deployment

This is pure static HTML — drop the entire folder onto:
- Cloudflare Pages
- Netlify
- Vercel (static)
- AWS S3 + CloudFront
- Any nginx/Apache webroot

No build step. No server needed beyond static file serving.

Recommended HTTP headers for production:
```
Cache-Control: public, max-age=3600, s-maxage=86400
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
```

## Regenerating localized pages

To rebuild locale pages from translation tables:

```bash
python3 build.py
```

This reads the `T` translation dict in `build.py` and writes one `index.html` per locale.

## File structure

```
.
├── index.html              # English (Global/CA) homepage
├── sitemap.xml
├── robots.txt
├── build.py                # locale page generator
├── assets/
│   ├── css/style.css
│   ├── js/main.js
│   └── img/
├── no/index.html
├── de/index.html
├── fi/index.html
├── da/index.html
├── is/index.html
├── fr/index.html
├── it/index.html
├── nl/index.html
├── be/index.html
└── ch/index.html
```

## Responsible gambling

Each locale links its country's official helpline (Hjelpelinjen.no, BZgA-Spielsucht.de, Peluuri.fi, StopSpillet.dk, SAA.is, Joueurs-Info-Service.fr, Giocaresponsabile.it, Loket Kansspel, Spelersbescherming.be, Sos-Spielsucht.ch).
