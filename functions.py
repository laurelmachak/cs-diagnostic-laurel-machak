# solution to problem 8

def fibonacci_iterative(num=10):
    current_number = 1
    last_number = 0
    for i in range(num):
        next_number = current_number + last_number
        print(next_number)
        last_number = current_number
        current_number = next_number
        

number = int(input())

fibonacci_iterative(number)


# solution to problem 10



        