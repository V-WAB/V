# Vanessa Woenam Banini

Personal website: one place to find my work, talks, press and links.

Live at **https://vanessa-banini.netlify.app/** (hosted on Netlify, which republishes automatically whenever `main` changes).

## What's here

| File | What it is |
|---|---|
| `index.html` | The whole site: text, layout, animations (the only page file to edit) |
| `about.html`, `work.html`, `talks.html`, `press.html`, `contact.html` | Separate pages generated from `index.html` by `tools/build_pages.py` |
| `config.js` | Contact-form settings (Supabase address and public key) |
| `assets/img/` | Photos |
| `assets/og.jpg` | The preview image shown when the link is shared |
| `supabase/migrations/001_enquiries.sql` | Creates the table that stores contact-form messages |
| `404.html` | Page shown for broken links |

## Hosting

The site is hosted on Netlify, connected to this repository:

- Build command: none. Publish directory: `.` (the repository root).
- Every change merged into `main` goes live a minute later.
- GitHub Pages is switched off for this repository on purpose. This GitHub account's Pages domain is
  baninibutter.com, so a Pages copy would appear under baninibutter.com/v/ instead of standing on its own.

## Connecting the contact form

1. In Supabase (project `kckywwwommpntwcejrzw`), open **SQL Editor**, paste the contents of
   `supabase/migrations/001_enquiries.sql`, and run it.
2. Open **Project Settings → API**, copy the **anon public** key, and paste it into
   `supabaseAnonKey` in `config.js`.
3. Messages then appear in Supabase under **Table Editor → enquiries**. Visitors can send
   messages but cannot read them.

## Pages

The homepage (`index.html`) is the whole site in one scroll. The menu links open separate pages:
`about.html`, `work.html`, `talks.html`, `press.html` and `contact.html`.

Those five files are generated from `index.html`, so **only edit `index.html`**, then run:

```bash
python3 tools/build_pages.py
```

and commit the regenerated pages along with your change.

## Updating content

- **Press, talks and work** are written directly in `index.html`, one block per item.
  Copy an existing block and change the text and link.
- **Video links** for talks: replace `href="#talks" data-missing` on a talk card with the
  video's address plus `target="_blank" rel="noopener"`, and change "Video link needed" to "Watch".
- **Social links** are in the footer near the end of `index.html`. Add each profile to the
  `sameAs` list near the top as well, so search engines connect them to this site.

## Using your own domain later

When you buy a domain, add it in Netlify under **Domain management**, follow Netlify's DNS steps,
then update the addresses in `index.html`, `robots.txt` and `sitemap.xml`.
