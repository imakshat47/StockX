from sortedcontainers import SortedDict

class OrderList(object):
    def __init__(self, reverse=False):
        ''' Initaited Object '''
        self.__orderList = SortedDict()
        self._max_price = 0
        self._reverse = reverse
        # print("Obect Initaited")

    def __set_max(self):
        ''' Set Max price for instance '''
        if self._reverse:
            self._max_price = sorted(
                self.__orderList.keys(), reverse=True)[0]
            return        
        if(self.__orderList.__len__() > 1):
            self._max_price = self.__orderList.keys()[0]

    def __update(self, key, value):
        '''Update Value or respective key '''
        self.__orderList[key] = value

    def __remove(self, key):
        ''' Remove a key from Indtance '''
        self.__orderList.__delitem__(key)

    def _return(self, key=None):
        ''' To return value or whole container '''
        if(key):
            return self.__orderList[key]
        return self.__orderList

    def _check(self, quantity, price):
        ''' Check for Quantity '''
        if(self.__orderList.__contains__(price)):
            _qty = self.__orderList[price]
            if(_qty >= quantity):
                self.__update(price, _qty - quantity)
                return True
            else:
                self.__remove(self._max_price)
                self.__set_max()
                return int(quantity - _qty)
        return False

    def _execute(self, quantity):
        ''' Executes and order in OrderBook '''
        while quantity:
            _qty = self.__orderList[self._max_price]
            if quantity >= _qty:
                # more iterations
                quantity -= _qty
                self.__remove(self._max_price)
                self.__set_max()
            else:
                self.__update(self._max_price, _qty - quantity)
                quantity = 0

    def _add(self, key, value):
        ''' Adds key n value '''
        self.__orderList[key] = value
        self.__set_max()
        return

    def add(self, quantity, price):
        ''' Add Records for OrderList Book '''
        quantity = int(quantity)
        if self.__orderList.__contains__(price):
            self.__orderList[price] = self.__orderList[price] + quantity
        else:
            self.__orderList[price] = quantity
        self.__set_max()
        return