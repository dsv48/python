billno = int(input("enter bill no"))
name   = input("enter name")
date   = input("enter date")
units = int(input("enter units"))

if (units <= 50):
    amount = units * 2
    surcharge = 25

#above 50 units first take the 50 units charge next subtract the 50 units from given units
elif (units <= 100):
    amount = (50*2) + ((units - 50) * 3)
    surcharge = 35

#above 100 units first take 50 and 100 units charge next subtract the 100 units from given units
elif (units <= 200):
    amount = (50*2) +(100*3)  + ((units - 100) * 5)
    surcharge = 45

#above 200 units first take the 50 and 100 and 200 units charge and next subtract the 200 units from given units
else:
    amount = (50*2) + (100*3) +(100*5) + ((units - 200) * 8)
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill = %d"  %total)
