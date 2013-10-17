from runpy import _get_main_module_details

__author__ = 'ChuTan'

"""
python marketsim.py {cash} {orders.csv} {output.csv}

Orders CSV = Year, Month, Day, Symbol, BUY or SELL, Shares

Output CSV = Year, Month, Day, Portfolio Value
"""

import sys
import csv

def main():
    print "Opening " + sys.argv[2]
    file = open(sys.argv[2], mode='rb')
    reader = csv.reader(file)
    for line in reader:
        print line

if __name__ == '__main__':
    main()