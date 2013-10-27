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

    df_close = get_data(startdate, enddate, symbols, [da.DataItem.CLOSE])[da.DataItem.CLOSE]
    df_ret = df_close / df_close.shift(1) - 1
    df_avg = df_ret.sum() / df_ret.count()
    df_var = (df_ret - df_avg) ** 2 / df_ret.count()
    df_vol = df_var ** 0.5




def get_data(dt_sd, dt_ed, l_symbols, l_keys):
    q = da.DataAccess(da.DataSource.YAHOO)
    l_ts = du.getNYSEdays(dt_sd, dt_ed, dt.timedelta(hours=16))
    l_dfs = q.get_data(l_ts, l_symbols, l_keys)
    return dict(zip(l_keys, l_dfs))


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
    l_keys = [da.DataItem.HIGH, da.DataItem.LOW, da.DataItem.CLOSE, da.DataItem.ACTUAL_CLOSE]
    return get_data(sd, ed, s, l_keys)


if __name__ == "__main__":
    main()