#!/usr/local/bin/python3

from math import pow

class complex:
    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine
    def __add__(self, other):
        output = complex(self.real + other.real, self.imagine + other.imagine)
        return output
    def __sub__(self, other):
        output = complex(self.real - other.real, self.imagine - other.imagine)
        return output
    def __mul__(self, other):
        output = complex(self.real * other.real - self.imagine * other.imagine, self.real * other.imagine + other.real * self.imagine)
        return output
    def __truediv__(self, other):
        try:
            output = self.__mul__(complex(other.real, -1*other.imagine))
            output = output.__mul__(complex(1/other.mod().real**2, 0))
            return output
        except ZeroDivisionError as zde:
            print(e)
            return None
    def mod(self):
        output = complex(pow(self.real**2 + self.imagine**2, 0.5), 0)
        return output
            
    def to_string(self):
        return (str("%.2f" % self.real) + "+" + str("%.2f" % self.imagine) + "i" if self.imagine >= 0 else str("%.2f" % self.real) + str("%.2f" % self.imagine) + "i")
    
first_real, first_imagine = map(float, input().strip().split(" "))
second_real, second_imagine = map(float, input().strip().split(" "))
first = complex(first_real, first_imagine)
second = complex(second_real, second_imagine)

print((first+second).to_string())
print((first-second).to_string())
print((first*second).to_string())
print((first/second).to_string())
print(first.mod().to_string())
print(second.mod().to_string())
