import itertools
from prettytable import PrettyTable
import csv


def extract_csv(_file='data/records.csv'):
    ''' Extracts Data from CSV '''
    _data = []
    with open(_file, 'rt', encoding='utf-8-sig')as f:
        data = csv.reader(f)
        for row in data:
            _data.append(row)
    return _data


def display_records(bidList, askList):
    ''' Display all Records '''
    _table = PrettyTable(['Bid Price', 'Bid Size', 'Ask Price', 'Ask Size'])
    bidList = dict(sorted(bidList.items(), reverse=True))
    for (bid_price, ask_price, bid_qty, ask_qty) in itertools.zip_longest(bidList.keys(), askList.keys(), bidList.values(),  askList.values(), fillvalue=' 0 '):
        _table.add_row([bid_price, bid_qty, ask_price, ask_qty])
    print(_table)

# def display_table_layout(_header=False):
#     ''' Print Table Layout '''
#     print("[______________________________________________]")
#     if _header:
#         print("[        Buy          ||          Sell         ]")
#         print("[  Quantity  |  Price || Quantity   |  Price   ]")
#         print("|____________|________||____________|__________|")

# def display_table_body(_arr, _newLine=False):
#     ''' Print Body of Table '''
#     for key in _arr:
#         print("|   ", key, end="   ")
#     print("", end="|")
#     if _newLine:
#         print(" ")
