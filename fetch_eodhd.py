import os
import argparse
import requests
import pandas as pd

# Simple script to fetch OHLCV data from EOD Historical Data

def parse_args():
    parser = argparse.ArgumentParser(description="Fetch OHLCV data using EODHD API")
    parser.add_argument('--symbol', required=True, help='Ticker symbol, e.g. AAPL')
    parser.add_argument('--interval', default='5m', help='Interval like 1m,5m,15m,1h,1d')
    parser.add_argument('--start', required=True, help='Start date YYYY-MM-DD')
    parser.add_argument('--end', required=True, help='End date YYYY-MM-DD')
    parser.add_argument('--output', default='eodhd_data.csv', help='Output CSV file')
    parser.add_argument('--api-key', default=None, help='EODHD API key')
    return parser.parse_args()


def resolve_api_key(cli_key: str | None) -> str | None:
    """Return the API key from CLI arg, env var, or eodhd_api_key.txt."""
    if cli_key:
        return cli_key
    env_key = os.getenv('EODHD_API_KEY')
    if env_key:
        return env_key
    key_path = os.path.join(os.path.dirname(__file__), 'eodhd_api_key.txt')
    if os.path.exists(key_path):
        with open(key_path) as f:
            key = f.read().strip()
            if key:
                return key
    return None

BASE_URL = 'https://eodhistoricaldata.com/api/intraday/{symbol}'


def fetch_data(symbol, api_key, interval, start, end):
    url = BASE_URL.format(symbol=symbol)
    params = {
        'api_token': api_key,
        'interval': interval,
        'from': start,
        'to': end,
        'fmt': 'json'
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)


def main():
    args = parse_args()
    api_key = resolve_api_key(args.api_key)
    if not api_key:
        raise SystemExit('API key required. Use --api-key, set EODHD_API_KEY, or place your key in eodhd_api_key.txt.')
    df = fetch_data(args.symbol, api_key, args.interval, args.start, args.end)
    df.to_csv(args.output, index=False)
    print(f"Saved {len(df)} rows to {args.output}")


if __name__ == '__main__':
    main()