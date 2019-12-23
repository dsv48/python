n = int(input("enter a number"))
for row in range(n):
    for col in range(n):
        if col==0 or row==(n-1) or row==col: #any logic is true print o/p thats why using or logic operator
            print ("*",end="")  #end is empty for continue that line why because end default value \n(next line)
        else:
            print(end=" ")  #condition is false to print the empty spapce.
    print() # this function is for new line go to the first for condition.

