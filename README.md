# Kalshi Crypto Bot Dashboard — Stage 2

This is a static, read-only dashboard prototype. It attempts to fetch publicly available Kalshi open-market data from the official public market endpoint. No credentials are required. It never submits orders.

## Publish
Upload `index.html` to the root of the existing GitHub Pages repository, replacing the previous `index.html`. Keep `manifest.webmanifest`, `sw.js`, and `icon.svg` in the repository root.

## Limits
- Browser CORS/network restrictions may block direct API calls. If that happens, the next step is a small server-side read-only proxy.
- Crypto markets are found by searching the markets returned by up to four pages; this is not guaranteed exhaustive.
- Displayed contract prices are Kalshi prices, not spot prices.
- No account authentication, trading, probability model, or risk enforcement is implemented.
- Do not put secrets, API keys, or passwords in this public repository.
