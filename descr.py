class Account(object):
   
    class Value(object):
    
        def __get__(self, instance, owner):
            return instance._amount
        
        def __set__(self, instance, value):
            instance._amount = value - (instance.commission * value)
            return instance._amount
        
    def __init__(self, commission):
        self.commission = commission
        self._amount = Account._amount

    amount = Value()
    _amount = 0

    

        

