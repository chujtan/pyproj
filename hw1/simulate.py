__author__ = 'ChuTan'

import datetime as dt
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tu
import matplotlib.pyplot as plt
import pandas as pd


def simulate(startdate, enddate, symbols, weights):
    vol = 0
    daily_ret = 0
    sharpe = 0
    cum_ret = 0

    q = da.DataAccess(da.DataSource.YAHOO)
    ldt_timestamps = du.getNYSEdays(startdate, enddate, dt.timedelta(hours=16))
    ls_keys = [da.DataItem.HIGH, da.DataItem.LOW, da.DataItem.CLOSE, da.DataItem.ADJUSTED_CLOSE]
    ldf_data = q.get_data(ldt_timestamps, symbols, ls_keys)
    return dict(zip(ls_keys, ldf_data))

#def plot():
#    plt.legend([])
#    plt.ylabel('Close')
#    plt.xlabel('Date')
#    plt.plot(ts, prices)
#    plt.show()


def main():
    sd = dt.datetime(2009, 1, 1)
    ed = dt.datetime(2009, 12, 31)
    s = ["GOOG", "GS", "XLF", "XLK", "$SPX", "XOM", "JNJ", "IBM", "AAPL", "GLD"]
    w = [1.0 / len(s) for i in range(len(s))]
    return simulate(sd, ed, s, w)


if __name__ == "__main__":
    main()