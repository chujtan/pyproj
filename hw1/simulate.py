__author__ = 'ChuTan'

import datetime as dt
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import matplotlib.pyplot as plt
import numpy as np


def calc_returns(df_price):
    return df_price / df_price.shift(1)

def calc_vol(df_pret):
    df_count = df_pret.count()
    return (((df_pret - (df_pret.sum() / df_count)) ** 2) / df_count) ** 0.5

def simulate(dt_sd, dt_ed, l_sym, l_w):
    '''Calculate vol, daily return, sharpe ratio, cum ret '''
    vol = 0
    daily_ret = 0
    sharpe = 0
    cum_ret = 0

    df_close = get_data(dt_sd, dt_ed, l_sym, [da.DataItem.CLOSE])[da.DataItem.CLOSE]
    if hasMissingValues(df_close): return
    df_value = sim_value(df_close, l_w)
    df_pvalue = df_value.sum(axis=1)
    df_pret = calc_returns(df_pvalue)
    df_pvol = calc_vol(df_pret)
    df_pcumret = df_pvalue / df_pvalue[0]

    plot(["PValue"], df_pvalue.index, df_pvalue)


def hasMissingValues(df_price):
    for col in df_price.columns:
        if np.any(df_price[col].isnull()):
            print "Col " + col + " contains NaN"
            return True
    return False


def rejectAllNAs(df_price):
    drop = []
    for col in df_price.columns:
        if np.all(df_price[col].isnull()):
            drop.append(col)
    print "Dropping " + str(drop)
    for col in drop: del df_price[col]
    return drop

def sim_value(df_close, qtys):
    return df_close * qtys

def get_data(dt_sd, dt_ed, l_sym, keys):
    q = da.DataAccess(da.DataSource.YAHOO)
    timestamps = du.getNYSEdays(dt_sd, dt_ed, dt.timedelta(hours=16))
    dfs = q.get_data(timestamps, l_sym, keys)
    return dict(zip(keys, dfs))

def plot(legend, ts, s):
    plt.legend(legend)
    plt.xlabel('Date')
    plt.plot(ts, s)
    plt.show()

if __name__ == "__main__":
    sd = dt.datetime(2009, 1, 1)
    ed = dt.datetime(2009, 12, 31)
    s = ["GOOG", "GS", "$SPX", "XOM", "JNJ", "IBM", "AAPL", "GLD"]
    w = [1.0 / len(s) for i in range(len(s))]
    df_close = get_data(sd, ed, s, [da.DataItem.CLOSE])[da.DataItem.CLOSE]

