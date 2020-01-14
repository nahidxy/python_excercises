#Finding the number of divisors

#Lets input a number first
number=int(input("Enter a number: "))

print('Divisors Are:')
divisor_counter=0
for i in range(1,number+1):
    if (number%i) == 0:
        divisor_counter+=1
        print(i)
print('Divisor Count=',divisor_counter)        
