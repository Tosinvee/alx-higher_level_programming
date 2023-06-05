#!/usr/bin/python3
def fizzbuzz():
    for i in range (1, 101):
        if (i % 15) == 0:
            print("{}".format('FizzBuzz'))
        elif (i % 3) == 0:
            print("{}".format('Fizz'))
        elif (i % 5) == 0:
            print("{}".format('Buzz'))
        else:
            print("{}".format(i))
