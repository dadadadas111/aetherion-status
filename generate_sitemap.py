#!/usr/bin/env python3
"""Simple sitemap generator for the static site.

Run from the project root. It scans for .html files (excluding sitemap.xml and robots.txt)
and writes `sitemap.xml` with full URLs using the domain from CNAME.
"""
import os
from datetime import date

ROOT = os.path.dirname(__file__)
CNAME_PATH = os.path.join(ROOT, 'CNAME')
OUT = os.path.join(ROOT, 'sitemap.xml')

def read_domain():
    try:
        with open(CNAME_PATH, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception:
        return 'aetherion-status.dash.id.vn'

def main():
    domain = read_domain()
    today = date.today().isoformat()
    pages = []
    for fname in os.listdir(ROOT):
        if not fname.endswith('.html'):
            continue
        if fname in ('sitemap.xml',):
            continue
        if fname.startswith('.'):
            continue
        url = f'https://{domain}/{fname}' if fname != 'index.html' else f'https://{domain}/'
        pages.append((url, today))

    # write sitemap
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url, lastmod in pages:
            f.write('  <url>\n')
            f.write(f'    <loc>{url}</loc>\n')
            f.write(f'    <lastmod>{lastmod}</lastmod>\n')
            f.write('    <changefreq>weekly</changefreq>\n')
            f.write('    <priority>0.5</priority>\n')
            f.write('  </url>\n')
        f.write('</urlset>\n')
    print('Wrote', OUT)

if __name__ == '__main__':
    main()
