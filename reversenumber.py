# Python Program to Reverse a Number using Functions

def Reverse_Integer(Number):
    Reverse = 0
    while(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Number = Number //10
    return Reverse
Number = int(input("Please Enter any Number: "))
Reverse = Reverse_Integer(Number)
print("/n reverse of enterde no is = %d" %Reverse)