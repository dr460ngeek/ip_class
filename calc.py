def add(x, y):
  """Adds two numbers."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides two numbers."""
  return x / y

def main():
  x=int(input("enter the first no: "))
  y=int(input("enter the second no: "))
  """Prints the results of adding, subtracting, multiplying, and dividing two numbers."""
  print("10 + 5 = ", add(x, y))
  print("10 - 5 = ", subtract(x, y))
  print("10 * 5 = ", multiply(x, y))
  print("10 / 5 = ", divide(x, y))

if __name__ == "__main__":
  main()