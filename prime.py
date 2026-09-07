class Prime:
    def __init__(self):
        self.primes = [2]

    def notDivisible(self, num):
        sqrtnum = int(num ** 0.5)
        for x in self.primes:
            if x > sqrtnum:
                break
            if num % x == 0:
                return False
        return True

    def primesUntilN(self, n):
        start = self.primes[-1] + 1
        for x in range(start, n + 1):
            if self.notDivisible(x):
                self.primes.append(x)

    def printPrimes(self, n):
        start = 0
        end = len(self.primes)
        while(start < end):
            mid = (start+end)//2
            if self.primes[mid] <= n:
                start = mid+1
            else:
                end = mid
        mid = start
        print(self.primes[:mid])
        print('No of primes is ', mid)


p = Prime()
while True:
    n = int(input('Enter a Positive Integer Greater than 2 -'))
    p.primesUntilN(n)
    p.printPrimes(n)