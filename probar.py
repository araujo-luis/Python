def do_stuff():
    print ("Hello world")
    return ("Is it over yet?")
    print ("Goodbye cruel world!")



x =3
print (-5 *x**5 + 69 *x**2 - 47)


def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    return present_value*(1+rate_per_period)**periods

print ("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3))

import math
#¼ n s2 / tan(π/n).
n = 7
s = 3

print ( (1/4) *n*s**2/math.tan(math.pi/n) )
