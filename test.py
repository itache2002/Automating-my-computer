def test():
  result  = 0
  print("Enter -1 to end")
  while True:
    value = int(input("Insert a number: "))
    if value == -1:
      return result
    else:
      result += value

res = test()
print("The sum of the values entered:", res)