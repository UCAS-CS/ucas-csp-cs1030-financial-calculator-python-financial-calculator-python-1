import os.path
import sys
import calculator

def test_calculator():
  try:
    exists = ox.path.exists("calculator.py")
    assert exists == True
  except:
    sys.exit()

set_keyboard_input([3000, 1000, 150, 200, 400])
output = get_display_output()

assert output == [
  "Hello, and welcome to your financial calculator!\n",
  "What is your monthly income: ",
  "What is your monthly rent: ",
  "What is your monthly utilities: ",
  "What is your monthly groceries: ",
  "What is your monthly transportation costs: ",
  f"Your monthly income is $3000.00\n",
  f"Your monthly expenses are $1750.00\n",
  f"Your monthly savings is $600.00\n",
  f"Your monthly spending money is $650.00\n",
  f"Your rent is 33% of your monthly income\n",
  f"Your utilities are 5% of your monthly income\n",
  f"Your groceries are 6% of your monthly income\n",
  f"Your transportation is 13% of your monthly income\n",
  f"Your savings are 20% of your monthly income\n",
  f"Your expenses are 58% of your monthly income\n"
