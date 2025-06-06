# OHLC Data Fetching Environment

This repository contains a simple script for downloading OHLCV data from TradingView using the [`tvDatafeed`](https://github.com/StreamAlpha/tvdatafeed) library.

## Setup

1. Install Python packages:

```bash
pip install pandas tvDatafeed requests
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

## Using the EODHD API

To fetch data from [EOD Historical Data](https://eodhistoricaldata.com),
install the dependencies as shown above and set your API key:

```bash
export EODHD_API_KEY='your_api_key'
```

Run `fetch_eodhd.py` with the desired options:

```bash
python fetch_eodhd.py --symbol AAPL.US --interval 1m --start 2023-01-01 --end 2023-01-31 --output aapl_intraday.csv
```

The script will download the specified range of OHLCV data and save it as a CSV
file.
