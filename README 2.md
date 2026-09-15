# Ledger — Invoice Maker 🧾

A complete, professional invoice generator: business/client details, line items, tax, live preview, one-click PDF export. Free version shows a "SAMPLE" watermark; a $9 license removes it.

## How the money part works (no backend needed)

1. **Host the free version** so people can try it (same steps as before):
   - Create a public GitHub repo, upload `index.html` (and `manifest.json`/`service-worker.js`/icons if included)
   - Settings → Pages → Branch: main, folder: / (root) → Save
   - You'll get a link like `https://yourusername.github.io/ledger/`

2. **Sell the unlock on Gumroad** (free to sign up, they just take a cut per sale):
   - Go to gumroad.com → create account → **New product**
   - Name: "Ledger — Invoice Maker License", price: **$9** (or "pay what you want" with a $5 minimum)
   - In **Content → Licensing**, turn on **"Generate a unique license key per sale"**
   - Set the license key format to start with `LEDGER-` (e.g. `LEDGER-XXXXXXXX`) — Gumroad auto-generates a unique key like this for every buyer and emails it to them automatically
   - In the product description, paste something like:
     > "This unlocks the full version of Ledger (the invoice tool). After purchase, you'll get a license key by email — go to [your GitHub Pages link], click 'Unlock', and paste your key in."
   - Publish the product — Gumroad gives you a payment link you can post anywhere (Instagram bio, Twitter/X, Reddit, a Linktree, etc.)

3. **Buyer flow**: they find your Gumroad link → pay → Gumroad emails them a `LEDGER-XXXXXXXX` key → they open your hosted tool, tap **Unlock — $9**, paste the key → watermark gone on their device.

## Where to actually get buyers (the hard part)

Building it is the easy 10%. To get real sales:
- Post it in freelancer-focused spaces: r/freelance, r/smallbusiness, Indie Hackers, Product Hunt
- Short demo video/GIF of it working posted to Twitter/X or TikTok with a link in bio
- Reach out directly to a few freelancers you know and offer it free in exchange for a review/testimonial you can then use

## Customizing it further

- Change the price by editing the Gumroad product — no code changes needed
- Want more features (recurring invoices, multiple currencies auto-converted, saved client list)? Ask and I can add them
- The whole tool works 100% offline once loaded — no data ever leaves the browser, which is worth mentioning to buyers who care about privacy
