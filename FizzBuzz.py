def fizz_buzz():
    sum=0  # i removed string as we just have to print it
    for i in range(1, 100):
        #calculating sum
        if ((i % 3)==0 or (i % 5)== 0):
            sum+=i
        #printing result
        if ((i % 3)==0 and (i % 5)== 0):
            print("FizzBuzz")
        elif  (i% 5) == 0:
            print("Buzz")
        elif  (i% 3) == 0:
            print("Fizz")
        else:
            print(i)
        
    return sum


if __name__ == "__main__":
    sum=fizz_buzz()
    print(f"Total sum of series is : {sum}")
