SEO Quick Actions — Aetherion
===========================

What I changed:
- Added `sitemap.xml` and `robots.txt`.
- Improved page `title`, `description`, `robots` meta tags, `canonical`, Open Graph tags, and JSON-LD on key pages.
- Added `generate_sitemap.py` to regenerate `sitemap.xml` from `.html` files using the `CNAME` domain.

How to run the sitemap generator (Windows / PowerShell):

```powershell
python .\generate_sitemap.py
curl https://aetherion-status.dash.id.vn/robots.txt
curl https://aetherion-status.dash.id.vn/sitemap.xml
```

Submit sitemap to Google Search Console:
- In GSC choose your property (add `https://aetherion-status.dash.id.vn/` if not added).
- Go to "Sitemaps" and submit `/sitemap.xml`.

Quick recommendations:
- Use unique, descriptive `<title>` and `<meta name="description">` per page (done).
- Add social-preview images sized 1200x630 at `images/og-*.png` and reference them in OG tags.
- Compress and serve images with caching headers from your host.
- Enable HTTPS and ensure TLS certificate is valid (site appears to be on dash.id.vn).
