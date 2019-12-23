#open and write a python file
f =open("python.txt", mode='w')
f.write("python features.\n 1.Easy to learn and use. \n 2.Expressive language. \n 3.Interprited language. \n 4.Cross-platform language. \n 5.free and open source. \n 6.Object oriented language. \n 7.Extensible. \n 8.Large standard library. \n 9.Gui programming support. \n 10.Integrated lanuage ")
f.close()

#read a file
f =open("python.txt", mode='r')
print(f.read())
f.close()

#no of chraacters in a file
f =open("python.txt", mode='r')
chars=f.read()
print("number of characters are: ", len(chars))

#Append:add the data to an existing file
f =open("python.txt", mode='a')
f.write("\n thank u")
print("successfully file appended")




