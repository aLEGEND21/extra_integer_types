class Prime(object):
    

    def __init__(self, num):
        self._val = int(num)
        if not self.isPrime(self._val):
            raise TypeError(f'{self._val} is not a prime number')

    
    def __repr__(self):
        return str(self._val)


    def isPrime(self, num):
        for i in range(2, num-1):
            if num % i == 0:
                return False
        return True


    def nextPrime(self, num=None):
        if not num:
            _ = self._val
        else:
            _ = num
        while True:
            _ += 1
            if self.isPrime(_):
                if not num:
                    self._val = _
                return _


    def prevPrime(self, num=None):
        if not num:
            _ = self._val
        else:
            _ = num
        if _ == 0:
            raise SyntaxError(f'{_} is the lowest prime number')
        while True:
            _ -= 1
            if self.isPrime(_):
                if not num:
                    self._val = _
                return _



class Composite(object):


    def __init__(self, num):
        self._val = int(num)
        if not self.isComposite(self._val):
            raise TypeError(f'{self._val} is not a composite number')
    

    def __repr__(self):
        return str(self._val)
    

    def isComposite(self, num):
        for i in range(2, num-1):
            if num % i == 0:
                return True
        return False
    

    def nextComposite(self, num=None):
        if not num:
            _ = self._val
        else:
            _ = num
        while True:
            _ += 1
            if self.isComposite(_):
                if not num:
                    self._val = _
                return _


    def prevComposite(self, num=None):
        if not num:
            _ = self._val
        else:
            _ = num
        if _ == 0:
            raise SyntaxError(f'{_} is the lowest composite number')
        while True:
            _ -= 1
            if self.isComposite(_):
                if not num:
                    self._val = _
                return _



class Odd(object):

    
    def __init__(self, num):
        self._val = int(num)
        if not self.isOdd(self._val):
            raise TypeError(f'{self._val} is not an odd number')
    

    def __repr__(self):
        return str(self._val)


    def isOdd(self, num):
        if num % 2 == 0:
            return False
        return True
    

    def nextOdd(self, num=None):
        if not num:
            _ = self._val
        else:
            _ = self._val
        _ += 2
        if not num:
            self._val = _
        return _
    
    
    def prevOdd(self, num=None):
        if not num:
            _ = self._val
        else:
            _ = self._val
        _ -= 2
        if not num:
            self._val = _
        return _
    


class Even(object):

    
    def __init__(self, num):
        self._val = int(num)
        if not self.isEven(self._val):
            raise TypeError(f'{self._val} is not an even number')
    

    def __repr__(self):
        return str(self._val)


    def isEven(self, num):
        if num % 2 == 0:
            return True
        return False
    

    def nextEven(self, num=None):
        if not num:
            _ = self._val
        else:
            _ = self._val
        _ += 2
        if not num:
            self._val = _
        return _
    
    
    def prevEven(self, num=None):
        if not num:
            _ = self._val
        else:
            _ = self._val
        _ -= 2
        if not num:
            self._val = _
        return _
    