__author__ = 'ChuTan'

import datetime as dt
import QSTK.qstkutil.DataAccess as da


def simulate(startdate, enddate, symbols, weights):
    vol = 0
    daily_ret = 0
    sharpe = 0
    cum_ret = 0

    q = da.DataAccess("Yahoo")
    ts_list = ["AAPL"]
    symbol_list = [ dt.datetime(2010,6,1) ]
    df_close = q.get_data(ts_list, symbol_list, "adjclose")

