import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone

API_URL = "https://external-api.kalshi.com/trade-api/v2/markets?status=open&limit=100"
OUTPUT_FILE = "data/kalshi_markets.json"

def main():
    request = urllib.request.Request(
        API_URL,
        headers={
            "Accept": "application/json",
            "User-Agent": "KalshiMarketMonitor/1.0",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.load(response)

        markets = data.get("markets", [])

        if not isinstance(markets, list):
            raise ValueError("Invalid market data received")

        output = {
            "source": "Kalshi public API",
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "market_count": len(markets),
            "markets": markets,
        }

        os.makedirs("data", exist_ok=True)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(output, file, indent=2)

        print(f"Successfully saved {len(markets)} markets.")

    except (urllib.error.URLError, ValueError, TimeoutError) as error:
        print(f"Failed to retrieve Kalshi markets: {error}")
        raise

if __name__ == "__main__":
    main()
