/* Cloudflare Web Analytics (privacy-friendly, no cookie banner).
   1. Open https://dash.cloudflare.com → Analytics & logs → Web Analytics → Add a site
   2. Site URL = your live launch URL (Netlify rename or custom domain)
   3. Copy the token from the JS snippet Cloudflare shows
   4. Replace PASTE_CLOUDFLARE_WEB_ANALYTICS_TOKEN below
   5. Commit + push, open the live site once, then screenshot the Cloudflare dashboard */
(function () {
  var TOKEN = "PASTE_CLOUDFLARE_WEB_ANALYTICS_TOKEN";
  if (!TOKEN || TOKEN.indexOf("PASTE_") === 0) return;
  var s = document.createElement("script");
  s.defer = true;
  s.src = "https://static.cloudflareinsights.com/beacon.min.js";
  s.setAttribute("data-cf-beacon", JSON.stringify({ token: TOKEN }));
  document.head.appendChild(s);
})();
