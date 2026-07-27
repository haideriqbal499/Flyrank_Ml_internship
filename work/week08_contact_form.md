# Week 8 — Wire one real thing

**Track card:** [Make It Do Something](https://aifluency.flyrank.ai/week-08.html#make-it-do-something)  
**One feature:** working contact form on the live portfolio  
**Free tier:** [FormSubmit](https://formsubmit.co/) (no server of mine)  
**Live form:** https://haideriqbal499.github.io/Flyrank_Ml_internship/contact.html

---

## Plain-words explainer (teach a friend)

**What a backend is.** A plain web page can show text and links. It cannot, by itself, remember a message or email it to me. The “backend” is the part that *does something* after you click Send — store, forward, or compute. I did not rent a server. I borrowed a tiny free backend: FormSubmit.

**What my feature does.** On Contact, a visitor types name, email, and a short message, then hits Send. That message is supposed to land in my Gmail (`haideriqbal499@gmail.com`). If the send works, the browser opens a Thanks page.

**How the data flows**

1. Visitor fills the form in `docs/contact.html` (live on GitHub Pages).
2. Browser **POSTs** the fields to `https://formsubmit.co/haideriqbal499@gmail.com` (FormSubmit’s free service).
3. FormSubmit checks it is not empty spam (I also hide a honeypot field bots often fill).
4. FormSubmit **emails** the fields to my inbox.
5. Hidden field `_next` sends the visitor to `contact-thanks.html` on my site.

My HTML never sees a password database. GitHub Pages still only serves files. FormSubmit is the middleman that turns a form submit into an email.

**First-time catch:** the very first test triggers an activation email from FormSubmit. I must click Confirm once. After that, real submissions reach me.

---

## Evidence checklist (you)

1. Push is live → open Contact on the public URL (private window).
2. First submit → open Gmail → confirm FormSubmit activation if asked → submit again.
3. Screenshot: (a) Thanks page and (b) the email that arrived.
4. Portal Files: those screenshots. Deliverable link: the Contact URL + this doc.

---

## Files involved (only this feature)

| File | Role |
|---|---|
| `docs/contact.html` | Form markup + FormSubmit `action` |
| `docs/contact-thanks.html` | Success landing (`_next`) |
| `docs/styles.css` | `.contact-form` styles |

No second feature. Mailto link stays as a fallback, not a second backend.

---

## Portal paste

```
Week 8 — one feature: contact form via FormSubmit free tier.
Live: https://haideriqbal499.github.io/Flyrank_Ml_internship/contact.html
Flow: browser POST → formsubmit.co → my Gmail; _next → contact-thanks.html.
Backend in plain words: FormSubmit is the part that emails me; Pages only serves HTML.
Test: [attach thanks + inbox screenshots after activation].
Doc: work/week08_contact_form.md
```
