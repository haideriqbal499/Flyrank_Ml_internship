# Week 9 — Plant your flag (domain + analytics + badge)

**Card:** [Plant Your Flag](https://aifluency.flyrank.ai/week-09.html#plant-your-flag)  
**Proof portfolio (source of truth):** `docs/` on GitHub Pages  
**Live today:** https://haideriqbal499.github.io/Flyrank_Ml_internship/ (HTTPS)  
**Clean free subdomain (do this if budget is zero):** Netlify → publish `docs` → rename to `haideriqbal`  
**Personal domain (preferred if you can spend ~$10–15/yr):** point it at the same site

---

## Status right now (checked Jul 30, 2026)

| Check | Status |
|---|---|
| Portfolio HTTPS | Pass — GitHub Pages 200 |
| `haideriqbal.netlify.app` | Fail — 404 (Drop / Git connect not done yet) |
| `haideriqbal.flyrank.ai` | Fail — DNS not granted / not resolving (capstone later) |
| Share preview / favicon / titles | Pass in `docs/` HTML (confirm again on the *final* address) |
| Graduate badge in footer | Wired in repo → push, then confirm live |
| Analytics | Script ready in `docs/js/analytics.js` — needs your Cloudflare token |

---

## Path A — clean free subdomain (zero budget)

You already have a long GitHub Pages URL. Reviewers accept a **clean** free subdomain as the fallback. Do this:

1. Open [app.netlify.com](https://app.netlify.com) → **Add new site** → **Import an existing project** → GitHub → this repo.
2. **Publish directory:** `docs` (not `site`). Build command: leave empty.
3. Deploy. Open the random `*.netlify.app` URL — padlock should show.
4. **Site configuration → Change site name** → `haideriqbal` (or `haideriqbal499` if taken).
5. Launch URL becomes: `https://haideriqbal.netlify.app/`
6. Confirm: home loads, favicon in the tab, footer badge visible, HTTPS padlock.

**How you know it worked:** the short URL opens the same home title as Pages, over HTTPS, with no certificate warning.

---

## Path B — personal domain (small cost, preferred)

1. Buy a domain (Namecheap / Cloudflare Registrar / Google Domains successor — pick something you can say out loud).
2. In Netlify (after Path A) **or** GitHub → Settings → Pages → Custom domain: enter `yourname.com`.
3. Add the DNS records the host shows (usually A/AAAA or CNAME). Wait minutes to a few hours.
4. Turn on HTTPS / “Force HTTPS” once the certificate issues.
5. Update every `canonical` + `og:url` + `og:image` host in `docs/*.html` to the new domain (search-replace the github.io base). Contact form `_next` URL too.

**How you know it worked:** phone browser opens `https://yourname.com` with the padlock and your HI favicon.

---

## Analytics (Cloudflare Web Analytics — free)

1. [dash.cloudflare.com](https://dash.cloudflare.com) → **Analytics & logs** → **Web Analytics** → **Add a site**.
2. Site hostname = your **launch** URL (Netlify rename or custom domain — not only the long github.io path if that is not the flag you plant).
3. Copy the **token** from the JS snippet Cloudflare shows.
4. Open `docs/js/analytics.js` (and `site/js/analytics.js`) and replace:

   `PASTE_CLOUDFLARE_WEB_ANALYTICS_TOKEN`

   with your real token.
5. Commit + push (and wait for Netlify if connected).
6. Open the live site once in a private window.
7. Back in Cloudflare: you should see a visitor. **Screenshot that dashboard** for the portal Files upload.

**How you know it worked:** the dashboard shows ≥1 page view after you visited.

---

## Graduate badge

Already in every public footer on `docs/` and `site/`:

- Image: `docs/img/flyrank-graduate-badge.svg`
- Link: https://internship.flyrank.ai/verify

When the portal unlocks your **credential ID** (after five fluency submissions + accepted capstone), if FlyRank gives you a personal verify URL or official badge asset, swap the `href` / `img` to that. Until then, the public verifier is the correct destination.

**How you know it worked:** footer shows the badge; click opens the verify page.

---

## Launch hygiene checklist (run on the *final* address)

Do this on your phone after Path A or B:

| Check | Pass looks like |
|---|---|
| HTTPS | Padlock; URL starts with `https://` |
| Favicon | HI monogram in the tab |
| Page title | Home tab: `Haider Iqbal — ranking queues for content refresh` |
| Share preview | Paste URL into [opengraph.xyz](https://www.opengraph.xyz/) or Facebook Sharing Debugger — title, description, `og-share.png` |
| Badge | Visible in footer; links to verify |
| Analytics | Cloudflare shows a hit after your visit |
| Contact | Form still posts; thanks page loads |

---

## Portal paste

**Deliverable links** (one per line — use your real launch URL):

```
https://haideriqbal.netlify.app/
https://internship.flyrank.ai/verify
https://github.com/haideriqbal499/Flyrank_Ml_internship/blob/main/work/week09_plant_your_flag.md
```

(If you bought a domain, put that HTTPS URL on line 1 instead.)

**Files:** Cloudflare analytics screenshot; optional phone screenshot of the footer badge.

**Notes:**

```
Launch: Netlify publish docs/ → haideriqbal.netlify.app (or personal domain).
HTTPS confirmed. Share preview / favicon / titles checked on final URL.
Analytics: Cloudflare Web Analytics token in docs/js/analytics.js.
Graduate badge in footer → internship.flyrank.ai/verify (swap to personal credential URL when issued).
Phone pass done on final address.
```

---

## Pass check

| Criterion | Who |
|---|---|
| Live on custom domain **or** clean free subdomain over HTTPS | **You** — Path A or B |
| Analytics installed and working | **You** — token + screenshot |
| Share preview, favicon, titles correct on real address | Confirm after deploy |
| Badge in footer → verification page | In repo; confirm live after push |
