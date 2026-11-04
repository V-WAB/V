# Vanessa Woenam Banini

Personal website: one place to find my work, talks, press and links.

Live at **https://v-wab.github.io/v/** once GitHub Pages is switched on (see below).

## What's here

| File | What it is |
|---|---|
| `index.html` | The whole site: text, layout, animations |
| `config.js` | Contact-form settings (Supabase address and public key) |
| `assets/img/` | Photos |
| `assets/og.jpg` | The preview image shown when the link is shared |
| `supabase/migrations/001_enquiries.sql` | Creates the table that stores contact-form messages |
| `404.html` | Page shown for broken links |

## Switching the site on

1. On GitHub, open **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`, and save.
3. After a minute the site is live at `https://v-wab.github.io/v/`.

## Connecting the contact form

1. In Supabase (project `kckywwwommpntwcejrzw`), open **SQL Editor**, paste the contents of
   `supabase/migrations/001_enquiries.sql`, and run it.
2. Open **Project Settings → API**, copy the **anon public** key, and paste it into
   `supabaseAnonKey` in `config.js`.
3. Messages then appear in Supabase under **Table Editor → enquiries**. Visitors can send
   messages but cannot read them.

## Updating content

- **Press, talks and work** are written directly in `index.html`, one block per item.
  Copy an existing block and change the text and link.
- **Video links** for talks: replace `href="#talks" data-missing` on a talk card with the
  video's address plus `target="_blank" rel="noopener"`, and change "Video link needed" to "Watch".
- **Social links** are in the footer near the end of `index.html`. Add each profile to the
  `sameAs` list near the top as well, so search engines connect them to this site.

## Using your own domain later

When you buy a domain, add a file named `CNAME` containing just the domain, point the domain's
DNS at GitHub Pages, then update the addresses in `index.html`, `robots.txt` and `sitemap.xml`.
