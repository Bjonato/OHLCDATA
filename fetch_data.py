import os
import argparse
from tvDatafeed import TvDatafeed, Interval
import pandas as pd

# Simple script to fetch OHLCV data using tvDatafeed

def parse_args():
    parser = argparse.ArgumentParser(description="Fetch OHLCV data from TradingView")
    parser.add_argument('--symbol', required=True, help='TradingView symbol, e.g. AAPL')
    parser.add_argument('--exchange', required=True, help='Exchange name, e.g. NASDAQ')
    parser.add_argument('--interval', default='1h', help='Interval like 1m,5m,15m,1h,4h,1d')
    parser.add_argument('--bars', type=int, default=5000, help='Number of bars to fetch')
    parser.add_argument('--output', default='data.csv', help='Output CSV file')
    return parser.parse_args()

INTERVAL_MAP = {
    '1m': Interval.in_1_minute,
    '5m': Interval.in_5_minute,
    '15m': Interval.in_15_minute,
    '1h': Interval.in_1_hour,
    '4h': Interval.in_4_hour,
    '1d': Interval.in_daily,
    '1w': Interval.in_weekly,
    '1M': Interval.in_monthly,
}

def main():
    args = parse_args()
    username = os.getenv('TV_USERNAME')
    password = os.getenv('TV_PASSWORD')
    tv = TvDatafeed(username, password)
    interval = INTERVAL_MAP.get(args.interval.lower(), Interval.in_daily)
    df = tv.get_hist(args.symbol, args.exchange, interval=interval, n_bars=args.bars)
    df.to_csv(args.output)
    print(f"Saved {len(df)} rows to {args.output}")

if __name__ == '__main__':
    main()
