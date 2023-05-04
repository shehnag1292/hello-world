def compound_interest(principal, rate, time):
  
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)

compound_interest(12000, 5.4, 2)