import itertools
from prettytable import PrettyTable
import csv


def extract_csv(_file_path='data/records.csv'):
    ''' Extracts Data from CSV @ filePath '''
    _data = []
    with open(_file_path, 'rt', encoding='utf-8-sig')as f:
        data = csv.reader(f)
        for row in data:
            _data.append(row)
    return _data


def display_records(bidList, askList):
    ''' Display all Records for bidList and askList'''
    _table = PrettyTable(['Bid Price', 'Bid Size', 'Ask Price', 'Ask Size'])
    bidList = dict(sorted(bidList.items(), reverse=True))
    for (bid_price, ask_price, bid_qty, ask_qty) in itertools.zip_longest(bidList.keys(), askList.keys(), bidList.values(),  askList.values(), fillvalue=' 0 '):
        _table.add_row([bid_price, bid_qty, ask_price, ask_qty])
    print(_table)
