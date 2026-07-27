# Week 6 — Explain it like you built it

**Track card:** [Explain It Like You Built It](https://aifluency.flyrank.ai/week-06.html#explain-it-like-you-built-it)  
**Piece I picked:** how deploying works on *my* site — GitHub Pages serving the `docs/` folder  
**Why this piece:** I could edit HTML fine; the mystery was why a folder in a GitHub repo becomes `https://haideriqbal499.github.io/Flyrank_Ml_internship/` with a padlock.

---

## Plain-words explanation (teach a friend)

My site is not a special app server. It is a pile of normal files: `index.html`, `about.html`, `styles.css`, pictures. Those files live in a folder named `docs/` inside my public GitHub repo.

GitHub has a free feature called **Pages**. I flipped one switch: “take the `docs/` folder on the `main` branch and publish it.” After that, GitHub copies those files to their web machines and gives me a permanent address:

`https://haideriqbal499.github.io/Flyrank_Ml_internship/`

Read that URL like a path:

- `haideriqbal499` — my GitHub username  
- `Flyrank_Ml_internship` — this repo’s name  
- whatever comes after — files inside `docs/` (so `docs/cv.html` is `/cv.html` on the live site)

The `https` padlock is automatic. I did not buy a certificate. GitHub handles that for `*.github.io`.

**How an update goes live:** I change a file on my laptop → `git commit` → `git push` to `main`. Pages notices the push, republishes `docs/`, and a minute or two later a hard refresh shows the new text. There is no “upload to FTP” step. The repo *is* the website.

**What this is not:** It is not Netlify Drop (that is the separate `site/` hub). It is not a backend. If I put a password or a private CSV in `docs/`, anyone on the internet can open it — so I only put public-safe stuff there.

---

## Tiny snippet from my real build

From `docs/index.html` — the browser loads this page from the live URL; the CSS next to it is also in `docs/`:

```html
<link rel="stylesheet" href="styles.css">
```

`styles.css` is a **relative** path: “same folder as this HTML.” On the live site that means `…/Flyrank_Ml_internship/styles.css`. If I had written `/Users/Windows 11/.../styles.css`, it would work on my laptop and break for everyone else. Relative paths are why the deployed site still looks like the local one.

---

## Tutor check (I answered these out loud)

1. **If I rename `docs/index.html` to `docs/home.html` and push, what happens at the bare site URL?**  
   The home URL looks for `index.html` by default — I’d get a missing page or a file list unless I rename it back or add a redirect. So the homepage filename matters.

2. **Where does `docs/work/refresh-queue.html` show up live?**  
   At `…/Flyrank_Ml_internship/work/refresh-queue.html` — the folders under `docs/` become folders in the URL.

---

## Portal paste

```
Week 6 — explain one real piece: GitHub Pages serving my docs/ folder.
Live site = docs/ on main. Push to main republishes. URL is username.github.io/repo/. HTTPS is automatic. Relative href like styles.css keeps laptop and live in sync.
Doc: work/week06_explain_build.md
```
