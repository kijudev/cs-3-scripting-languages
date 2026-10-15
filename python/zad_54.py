from fractions import Fraction

text = input("decimal number: ")

fraction = Fraction(text).limit_denominator()

print(fraction)
