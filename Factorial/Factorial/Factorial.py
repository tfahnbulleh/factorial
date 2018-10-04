
 #compute the factorial of a number
def computerFactorial(number):
    if number ==0 or number == 1 or number == 2: # number is 0, 1, or 2
       return number     
    else: # number is greater than 2

       total=(number-1) *number 
       number=number-2
       while number >1:
           total=total*number
           number=number-1
    print(total)
    return total
