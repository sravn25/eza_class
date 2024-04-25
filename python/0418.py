print("Input: num, num > 0, num < 100 \n")
print("1. If num can be divided by 3, print \"Fizz\"")
print("2. If num can be divided by 5, print \"Buzz\"")
print("3. If num can be divided by 3 and 5, print \"FizzBuzz\"")
print("4. If num cannot be divided by 3 and/or 5 , print \"none\"")
num = int(input("Number?: "))

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("WAWA",end="")
    elif num % 3 == 0: 
        print("wa",end="")
    elif num % 5 == 0:
        print("WA",end="")
    else:
        print("",end="")

for i in range(100):
    fizzbuzz(i)
