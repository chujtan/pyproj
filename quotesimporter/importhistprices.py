__author__ = 'ChuTan'

import ystockquote

ADJ_CLOSE = "Adj Close"
CLOSE = "Close"
HIGH = "High"
LOW = "Low"
OPEN = "Open"
VOLUME = "Volume"


def main():
    prices = ystockquote.get_historical_prices("XLF", "2013-01-01", "2013-12-31")


if __name__ == "__main__":
    main()