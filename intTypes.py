class prime(object):

    def __init__(self, num):
        self.num = int(num) #This will throw an error if an integer is not provided
        if not self.isPrime(self.num):
            raise TypeError(f'{self.num} is not a prime number')
    
    def isPrime(self, num):
        for i in range(1, num):
            if num % i == 0:
                return True
        return False

    def nextPrime(self):
        num = self.num
        while True:
            num += 1
            if self.isPrime(num):
                self.num = num
                return self.num

    def prevPrime(self):
        if self.num == 0:
            raise SyntaxError(f'{self.num} is the lowest prime number')
            return
        num = self.num
        while True:
            num -= 1
            if self.isPrime(num):
                self.num = num
                return self.num

