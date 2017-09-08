
#Write an algorithm (in English) that takes two inputs,
# start and end that prints every number from start to end (inclusive).
# However, if a number is evenly divisible by 3,
#print the word “fizz” instead of the number.
#If a number is evenly divisible by 5,
# print “buzz” instead of the number. 
# If a number is evenly divisible by both 3 and 5,
# print “fizzbuzz” instead of the number.



def fizzbuzz(start,end):
    for i in range(start,end+1):
        if i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)
            
fizzbuzz(3,10)
