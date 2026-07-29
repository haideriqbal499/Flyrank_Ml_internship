# Week 9 — Break your own site

**Live URL:** https://haideriqbal499.github.io/Flyrank_Ml_internship/

**Proof statement:** I build ranking systems on messy search data and say what they can and cannot claim.

**How I attacked it:** empty + garbage form submits, double-click submit path, phone-width (390px) viewport, every nav/work/demo/repo link, name search, free speed check, HTML meta audit.

---

## Where it breaks — fix-now (fixed in this pass)

| # | Finding | Expected | What I saw | Fix |
|---|---|---|---|---|
| 1 | LinkedIn href was the literal `LINKEDIN_URL` | Real profile or no link | 404 at `/LINKEDIN_URL` on home + CV | Removed broken link; named LinkedIn as not linked yet |
| 2 | No Open Graph / Twitter share tags | Paste-ready card | Title + description only; no `og:*` / `twitter:*` | Added canonical, OG, Twitter tags on home, about, contact, CV, paper, both cases |
| 3 | No share image | 1200×630 preview | Missing | Added `docs/img/og-share.png` and pointed `og:image` / `twitter:image` at it |
| 4 | Double submit on contact form | One send; button locks | Button stayed clickable after first submit (no busy state) | Disable button + “Sending…” on valid submit (`contact.html`) |
| 5 | No crawl hints | Sitemap / robots for findability | None | Added `docs/robots.txt` + `docs/sitemap.xml` (blocks `_before-mobile.html`) |

### Evidence of SEO/meta

- Home `<title>`: Haider Iqbal — ranking queues for content refresh
- Meta description present on public pages
- Share preview tags: `og:title`, `og:description`, `og:image`, `twitter:card=summary_large_image`
- Preview the card after push: [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) or [opengraph.xyz](https://www.opengraph.xyz/) with the live URL

### Speed check (free)

- PageSpeed Insights API was rate-limited (HTTP 429) during this session — re-run after push: https://pagespeed.web.dev/analysis?url=https%3A%2F%2Fhaideriqbal499.github.io%2FFlyrank_Ml_internship%2F
- Direct fetch of the home HTML: ~5 KB body, ~170 ms wall time from this machine (static GitHub Pages; fonts still load from Google)
- Stack is HTML/CSS + two font families + SVG charts — no app JS bundle on most pages (contact has a tiny submit guard)

### Findability

- Searching “Haider Iqbal ranking queues / Flyrank github.io” did **not** surface this site yet (common names + new index).
- After push: site is findable by direct URL; sitemap/robots help crawlers. Google indexing can take days — named as known limitation below until Search Console shows it.

---

## Where it breaks — known limitations (named, not hidden)

| # | Finding | Why not fixed for this checkpoint |
|---|---|---|
| A | Form accepts a nonsense **name** (`!!!@@@###`) if email + message pass HTML5 | Browser validates empty + bad email; name has no pattern. FormSubmit spam filter / honey field is the backstop. Over-filtering names is worse than a weird name. |
| B | Contact depends on **FormSubmit** free tier (activation email, outages, rate limits) | Third-party; mailto fallback stays on the page |
| C | Double-submit guard needs **JavaScript** | No-JS users can still double-post; rare for hiring managers |
| D | **Google Fonts** fail closed on old / locked-down browsers → system serif/sans | Acceptable fallback; layout still readable (Week 7 typography) |
| E | Name search does not yet rank this portfolio | Indexing lag; custom domain + Search Console are Week 9 launch steps |
| F | Personal hub `haideriqbal.netlify.app` returned **404** when checked | Separate Drop deploy not live yet — internship Pages URL is the source of truth |
| G | `_before-mobile.html` still public if you know the path | Intentional Week 7 before-artifact; disallowed in `robots.txt`, not in nav |
| H | No LinkedIn profile URL on the site yet | Honest gap until a real profile URL is ready |

---

## Attack checklist (what a well-behaved site should do)

| Attack | Well-behaved | Mine |
|---|---|---|
| Submit empty | Block with clear field message | Pass — “Please fill out this field.” |
| Garbage email | Block email type | Pass — requires `@` |
| Garbage name only | Either allow or pattern-block | Known limitation A |
| Double submit | Lock button / ignore second | Fixed (#4) |
| Untested viewport (390px) | No horizontal spill; tap targets | Pass (Week 7 layout still holds) |
| Click all links | 200 / real destination | Fail then fix: LinkedIn 404; others 200 (repo, paper, cases, Colab GET 200) |
| Search own name | Site or clear profile | Not in results yet — limitation E |
| Speed check | Run free tool; note score | Tool 429; fetch + stack notes above — re-run after push |

---

## Hardening review packet (for mentor / structured peer)

**Must-fixes before launch (this list):**

1. Confirm LinkedIn 404 is gone on live home + CV after push.
2. Confirm share debugger shows title, description, and `og-share.png`.
3. Submit one real contact message; confirm thanks page + inbox; confirm button shows “Sending…”.
4. Re-run PageSpeed (mobile + desktop); paste scores into the portal Notes.
5. Peer/mentor: open the site on *their* phone browser once.

**Ask the reviewer:**

- Does any claim on the home cards overstate the paper numbers?
- Is the one CTA still email about an ML intern / junior role?
- Any remaining placeholder text or 404s?

---

## Portal paste (short)

```
Live: https://haideriqbal499.github.io/Flyrank_Ml_internship/
Break list: work/week09_break_your_own_site.md (fix-nows fixed; known limitations named)
SEO: title + description + OG/Twitter + og-share.png + robots.txt + sitemap.xml
Speed: home ~5KB; re-run PageSpeed after push (API 429 during audit)
Hardening review: ready — see “Hardening review packet” in that file
```

After you push `docs/` to `main`, GitHub Pages will republish. Then paste the portal block, attach a PageSpeed screenshot, and send the hardening packet to your mentor or peer.
