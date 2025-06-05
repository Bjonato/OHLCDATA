# OHLC Data Fetching Environment

This repository contains a simple script for downloading OHLCV data from TradingView using the [`tvDatafeed`](https://github.com/StreamAlpha/tvdatafeed) library.

## Setup

1. Install Python packages:

```bash
pip install pandas tvDatafeed
```

2. (Optional) Set environment variables for your TradingView credentials:

```bash
export TV_USERNAME='your_username'
export TV_PASSWORD='your_password'
```

The script will work without credentials but may have limited access.

## Usage

Run `fetch_data.py` to download data:

```bash
python fetch_data.py --symbol AAPL --exchange NASDAQ --interval 1h --bars 5000 --output aapl.csv
```

The resulting CSV file will contain the open, high, low, close, and volume data for the requested symbol.
