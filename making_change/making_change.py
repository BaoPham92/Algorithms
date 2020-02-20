#!/usr/bin/python

import sys

def making_change(amount, denominations = []):

  # * FLOAT INPUT AMOUNT
  amount = float(amount)
  print(f'Amount: {amount} Denominations: {denominations}')

  # * PLACEHOLDER FOR VALID CONVERSIONS
  available_conversions = 0
  print(f'Current Conversions: {available_conversions}')

  # * IF THERE ARE ARRAY OF DENOMINATIONS IS NOT EMPTY
  if (len(denominations) > 0):
    
    # * CALCULATE NUMBER OF POSSIBLE CONVERSIONS
    for denominator in denominations:
      division = float(amount / denominator)

      # ? IF TRUE, INCREMENT POSSIBLE CONVERSIONS
      if (division * denominator == amount): 
        available_conversions += 1

  print(f'{available_conversions}')
  return available_conversions

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")

  making_change(20, [0.01, 0.05, 0.10, 0.25, 0.50])
  making_change(350, [1, 5, 10, 25, 50])