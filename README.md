# Kalshi Crypto Bot — Installable Web App Prototype (Stage 1)

## What this is
A phone-first Progressive Web App (PWA) dashboard shell. Once hosted over HTTPS, a compatible browser can offer **Add to Home screen / Install app**.

## Safety boundary
- This is a UI prototype with illustrative sample data.
- It does not connect to Kalshi or market-data providers.
- It cannot place, amend, or cancel orders.
- Start/Pause/Emergency Stop controls only change the local demo status.
- Live trading is not implemented.

## Files
- `index.html` — responsive dashboard and demo controls
- `manifest.webmanifest` — PWA install metadata
- `sw.js` — basic offline asset caching
- `icon.svg` — app icon

## How to preview locally
Open `index.html` in a browser to inspect the layout. PWA installation and service-worker features require an HTTPS host or localhost; opening the file directly does not enable installation.

## Install on Android after hosting
1. Open the HTTPS site in Chrome.
2. Open Chrome's three-dot menu.
3. Tap **Install app** or **Add to Home screen**.
4. Follow the prompts; launch it from the new home-screen icon.

## Next build stages
1. Host this dashboard securely over HTTPS.
2. Add authenticated server-side API connections using official current Kalshi documentation.
3. Add read-only market scanning.
4. Add demo/paper trading, conservative fill assumptions, fees, risk checks, and durable logs.
5. Backtest and paper-trade before any separate, explicit authorization for live trading.

A website/PWA dashboard alone is not a 24/7 trading engine. The trading engine must run separately on a reliable server, with secrets stored server-side and never in browser code.
