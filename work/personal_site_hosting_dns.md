# Personal site + DNS walkthrough

**Card:** free host, clean public URL, DNS explained before the FlyRank subdomain  
**Site folder (Netlify Drop):** `site/`  
**Also on GitHub Pages:** internship portfolio at `docs/` (already HTTPS)

---

## 1. Plan (one page is enough)

| Block | Content |
|---|---|
| Who | Haider Iqbal — ranking queues for content refresh |
| What I am building | Refresh / opportunity ranking with honest limits; capstone + cases |
| Links | LinkedIn, GitHub, CV (`cv.html`), booking (mailto “Book a chat”) |
| Later | Card for posts / more cases; FlyRank subdomain is a pointer, not a rebuild |

---

## 2. Hosting path

| Choice | Why |
|---|---|
| **Netlify (recommended for this card)** | Free HTTPS, rename to `haideriqbal.netlify.app`, custom domain later without rebuild |
| GitHub Pages (already live) | Week 4 stack; portfolio + paper stay at `https://haideriqbal499.github.io/Flyrank_Ml_internship/` |

**Deploy Netlify (you do this — ~2 minutes):**

1. Open [app.netlify.com/drop](https://app.netlify.com/drop) (sign up free if needed).
2. Drag the whole **`site/`** folder onto the page (must contain `index.html` at the root of what you drop).
3. Wait for the random `*.netlify.app` URL → open it over HTTPS.
4. **Site configuration → Change site name** → `haideriqbal` (or `haideriqbal499`) so the CV-worthy URL is `https://haideriqbal.netlify.app`.
5. Before Drop: search-replace `LINKEDIN_URL` in `site/index.html` and `site/cv.html` with your real LinkedIn profile URL.

**Update later without a second site:** connect the GitHub repo in Netlify (publish directory `site`) so push = republish. Do not Drop a second copy.

---

## 3. Every file you deploy (`site/`)

| File | What it does |
|---|---|
| `index.html` | Home: claim, what you are building, link list |
| `cv.html` | Short CV page (the CV link) |
| `styles.css` | Identity kit: Fraunces, Source Sans 3, cream `#f4f1ea`, green `#0b5f45` |
| `favicon.svg` | HI monogram tab icon |

No build step. No framework. If you cannot explain a line, delete or rewrite it before Drop.

---

## 4. DNS walkthrough (own words — for when Ops grants the subdomain)

**Who this is for:** a teammate who does not live in DNS. Read once now; run as a checklist at capstone.

### What a CNAME is

A **CNAME** (“canonical name”) is a DNS record that says: “this hostname is an alias for that other hostname.” It does not store an IP address. It points one name at another name. When FlyRank gives you something like `haideriqbal.flyrank.ai`, you will not move your files. You will point that name at your host’s name (for Netlify, usually your `something.netlify.app`).

**Value yours will hold (Netlify path):**

| Field | Value |
|---|---|
| Type | CNAME |
| Name / host | `haideriqbal` (the left part of `haideriqbal.flyrank.ai`) — Ops often creates this side |
| Target / points to | `haideriqbal.netlify.app` (or whatever Netlify shows under Domain management — sometimes a Netlify DNS target they list in the UI) |

If you stay on **GitHub Pages** instead, the target is typically `haideriqbal499.github.io` (and you add a `CNAME` file in `docs/` plus the custom domain in repo Settings → Pages). Same idea: alias in, files stay put.

### What happens when someone types your address

1. **They type** `https://haideriqbal.flyrank.ai` in a browser.
2. **Resolver** — their device asks a DNS resolver (often the ISP or 1.1.1.1 / 8.8.8.8): “Where is this name?”
3. **Nameserver** — the resolver walks the DNS tree to the nameservers that own `flyrank.ai` and asks for the record for `haideriqbal.flyrank.ai`.
4. **Record** — those nameservers answer with the **CNAME**: “it is an alias of `haideriqbal.netlify.app`.” The resolver then asks where *that* name points (A/AAAA to Netlify’s edge).
5. **Response** — the browser opens a TCP/TLS connection to that IP, shows the **padlock** (HTTPS certificate for your hostname, issued via the host), and Netlify returns your `index.html`.

Nothing about your HTML folder changes. A custom domain is a **pointer**, not a migration.

### Checklist when the subdomain is granted

1. Ops confirms `haideriqbal.flyrank.ai` (or your assigned name) exists.
2. In Netlify: Domain management → Add custom domain → enter the subdomain.
3. Confirm the CNAME target Netlify shows matches what Ops published (or update your side if you control DNS).
4. Wait for propagation (minutes to a few hours). Hard-refresh; try a phone / private window.
5. Confirm the padlock on `https://haideriqbal.flyrank.ai`. If HTTPS stalls, use Netlify’s HTTPS/SSL docs and Domain troubleshooting before asking for help.
6. Swap the URL on LinkedIn + CV from the free `*.netlify.app` to the FlyRank subdomain. Keep the old URL working if you want; both can serve the same site.

---

## 5. Link from LinkedIn and CV (you)

| Place | Action |
|---|---|
| LinkedIn | Edit profile → Website / Featured → paste your clean Netlify URL (or Pages URL until Netlify is renamed) |
| CV | Already links out from `cv.html`; also paste the live site URL at the top of any PDF you send |

---

## 6. Portal paste

**Deliverable links**

```
https://haideriqbal.netlify.app
https://github.com/haideriqbal499/Flyrank_Ml_internship/blob/main/work/personal_site_hosting_dns.md
```

(Use your real renamed Netlify URL if different. Until Drop is done, Pages URL still proves HTTPS hosting: `https://haideriqbal499.github.io/Flyrank_Ml_internship/`.)

**Notes**

```
Personal hub: site/ (index, cv, styles, favicon) — identity kit cream/green.
Host: Netlify Drop + rename to haideriqbal.netlify.app (GitHub Pages still serves docs/ portfolio).
Links: LinkedIn (set URL), GitHub, CV page, booking mailto.
DNS walkthrough: CNAME alias to Netlify; resolver → nameserver → record → HTTPS. Capstone: add domain in host, confirm padlock.
Doc: work/personal_site_hosting_dns.md
```

---

## Pass check

| Criterion | Status |
|---|---|
| Site live HTTPS on clean public URL | **You:** Netlify Drop + rename (Pages already live as backup) |
| Positioning + LinkedIn, GitHub, CV, booking | Built in `site/`; **set LinkedIn URL** |
| DNS walkthrough in own words | Section 4 above |
| Can explain every deployed file | Section 3 |
| Linked from LinkedIn + CV | **You** after URL is live |
| Capstone subdomain | Later — checklist in section 4 |
