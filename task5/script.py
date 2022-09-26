import unittest

def factors(n):
    p = 2
    f = list()
    while n >= p*p :
        if n % p == 0:
            f.append(p)
            n = int(n / p)
        else:
            p = p + 1
            f.append(n)
    return f

def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
        else:
            return True

def vowels(text):
    v = list()
    for i in text:
        if i in 'aeiouAEIOU':
            v.append(i)
    return v

class FactorsTest(unittest.TestCase):
    def testType(self):
        factorsResult = factors(16)
        self.assertIsInstance(factorsResult, bool, "Wrong type!")
    def testNum(self):
        factorsTestNum = factors(6)
        self.assertEqual(factorsTestNum, [1, 8])
    def testNegative(self):
        factorsNeg = factors(-6)
        self.assertEqual(factorsNeg, [])
    def testArg(self):
        with self.assertRaises(TypeError):
            factors('12345')

class TestPrimes(unittest.TestCase):
    def testType(self):
        primeRes = is_prime(47)
        self.assertIsInstance(primeRes, bool)
    def testArg(self):
        with self.assertRaises(TypeError):
            is_prime('47')
    def testNegative(self):
        primeRes = is_prime(-1984)
        self.assertEqual(primeRes, False)
    def testPrime(self):
        primeRes = is_prime(4769)
        self.assertEqual(primeRes, True)
    def testNonprime(self):
        primeRes = is_prime(8080)
        self.assertEqual(primeRes, False)
    
class TestVowels(unittest.TestCase):
    def testType(self):
        vovelTest = vowels('Death can have me when it earns me')
        self.assertIsInstance(vovelTest, list)
    def testArg(self):
        with self.assertRaises(TypeError):
            vowels(5)
    def testVowels(self):
        vw_res = vowels('I feel like my whole life is just a series of loosely related wacky misadventures')
        self.assertEqual(vw_res, ['I', 'e', 'e', 'i', 'e', 'o', 'e', 'i', 'e', 'i', 'u', 'a', 'e', 'i', 'e', 'o', 'o', 'o', 'e', 'e', 'a', 'e', 'a', 'i', 'a', 'e', 'u', 'e'])

if __name__ == "__main__":
    unittest.main()
