import src.orderList as oList
import src.helper as app


def print_msg(_msg):
    print("\n-----------------------------------------\n")
    print("     [   ", _msg, "   ]")
    print("\n-----------------------------------------\n")


def return_obj(_type, reverse=False):
    if _type == 'A':
        if reverse:
            return _bid
        return _ask
    if reverse:
        return _ask
    return _bid


# driving function
if __name__ == '__main__':
    # # Extrating Data from CSV
    csv_data = [
        ['B', 'TCS', 'NSE', '700', '11.36', '1618148393', '2'],
        ['B', 'TCS', 'NSE', '100', '11.35', '1618148394', '1'],
        ['A', 'TCS', 'NSE', '100', '11.40', '1618148402', '9', '11.39'],
        ['B', 'TCS', 'NSE', '100', '11.34', '1618148395', '2'],
        ['B', 'TCS', 'NSE', '100', '', '1618148402', '9'],
        ['B', 'TCS', 'NSE', '600', '11.33', '1618148396', '3'],
        ['A', 'TCS', 'NSE', '100', '11.40', '1618148402', '9', '11.38'],
        ['A', 'TCS', 'NSE', '100', '', '1618148402', '9'],
        ['A', 'TCS', 'NSE', '100', '11.40', '1618148402', '9', '11.38'],
        ['B', 'TCS', 'NSE', '700', '11.32', '1618148397', '4'],
        ['A', 'TCS', 'NSE', '900', '11.42', '1618148398', '5'],
        ['A', 'TCS', 'NSE', '400', '11.41', '1618148399', '6'],
        ['A', 'TCS', 'NSE', '205', '11.4', '1618148400', '7'],
        ['A', 'TCS', 'NSE', '600', '11.39', '1618148401', '8'],
        ['A', 'TCS', 'NSE', '600', '11.39', '1618148401', '8'],
        ['A', 'TCS', 'NSE', '400', '11.38', '1618148402', '9'],
        ['B', 'TCS', 'NSE', '100', '11.38', '1618148402', '9'],
        ['A', 'TCS', 'NSE', '100', '11.36', '1618148402', '9'],
        ['A', 'TCS', 'NSE', '100', '', '1618148402', '9'],
        ['A', 'TCS', 'NSE', '100', '11.36', '1618148402', '9', '11.38'],
    ]    
    
    # csv_data = app.extract_csv()

    # Defining Order List Instances
    _bid = oList.OrderList(True)
    _ask = oList.OrderList()
    _sl = oList.OrderList()

    # Looping through Queries
    for data in csv_data:
        # defining variables
        _qty = int(data[3])
        _price = data[4]

        # print("Executing Order => ", data[6])
        # print("Max Price", _bid._max_price)
        # print("Max Price", _ask._max_price)

        # Defining Objects
        _obj = return_obj(data[0])
        _rev_obj = return_obj(data[0], True)

        # For Market Order
        if(_price == ''):
            if(_rev_obj._max_price == 0):
                if _obj == '_bid':
                    print_msg(
                        "Market Order can not be Executed. No Sell Order Yet!!")
                else:
                    print_msg(
                        "Market Order can not be Executed. No Buy Order Yet!!")
                continue
            _rev_obj._execute(_qty)
            print_msg("Market Order Executed. Size = " + str(_qty))
            continue

        # For Stop Loss
        if 0 <= 7 < len(data):
            market_price = input("Enter the Current the Market Price: ")
            _sl_price = data[7]
            if data[0] == 'A':
                if market_price <= _sl_price <= _price:
                    # add record to _sl
                    _sl._add(_sl_price, [_price, _qty])
            else:
                if market_price >= _sl_price >= _price:
                    # add record to _sl
                    _sl._add(_sl_price, [_price, _qty])

        # For Limit Order
        # Check For limit Order
        _check = _rev_obj._check(_qty, _price)
        if(_check == True):
            print_msg("Limit Order Executed. Size = " + str(_qty))
            continue

        # For un executed Limit order
        if _check != False:
            if isinstance(_check, int):
                _qty = _check

        # Add new entry
        _obj.add(_qty, _price)

        # Priting Records
        app.display_records(_bid._return(), _ask._return())
        # # Run Next ?
        # _next = input("Do you want to continue? (Y/N): ")
        # if(_next == 'N' or _next == 'n'):
        #     break

    print_msg("All Orders Executed!!")
    # Priting Records
    app.display_records(_bid._return(), _ask._return())
