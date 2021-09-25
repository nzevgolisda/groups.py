import math
class Complex:
    def __init__(self, real, imag):
        self.Re = real
        self.Im = imag
        self.r = self.abs()
        self.theta = self.getAngle()
    def abs(self):
        return (self.Re**2 + self.Im**2)**0.5
    def getAngle(self):
        return math.acos(self.Re/self.r)
    def _Z_(self):
        return Complex(self.Re, -self.Im)
    def add(self, other):
        return Complex(self.Re + other.Re, self.Im + other.Im)
    def prod(self, other):
        c1 = self.Re * other.Re - self.Im * other.Im
        c2 = self.Re * other.Im + self.Im * other.Re
        return Complex(c1, c2)
    def inProd(self, other):
        return self.Re*other.Re + self.Im*other.Im
    def getInnerAngle(self, other):
        cosAngle = self.inProd(other)/(self.r*other.r)
        return math.acos(cosAngle)
    def div(self, other):
        x = self.prod(other._Z_())
        y = other.r ** 2
        z1 = x.Re/y
        z2 = x.Im/y
        return Complex(z1, z2)
    def printInnerAngle(self, other):
        theta = self.getInnerAngle(other)
        return print('cos(angle) = ',math.cos(theta),', so inner angle = ',theta/math.pi,'π')
    def print(self):
        return print(self.Re,'+',self.Im,'*i')
    def printAngle(self):
        return print((self.theta)/math.pi,'π')
    def getPolar(self):
        return [self.r, self.theta]
    def CiS(self, n):
        theta = self.theta
        x = math.cos(n*theta)
        y = math.sin(n*theta)
        return Complex(x, y)
    def exp(self, n):
        R = Complex(self.r**n, 0)
        z = self.CiS(n)
        return R.prod(z)
