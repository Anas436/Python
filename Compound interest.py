# Python3 program to find compound
# interest for given values.

def Compound_Interest(principle, rate, time ) :

    # Calculates compound interest
    amount = principle*(pow((1+rate/100),time))
    CI = amount - principle

    print('Your compound interest is : ', CI)


Compound_Interest(345, 89, 67)