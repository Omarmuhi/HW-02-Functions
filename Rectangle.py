Enter_the_length: 25
Enter_the_width:  10

Area =   250
Perimeter = 70
"Thanks for using this program!"
# reading length
length = int(input("Enter the length: "))

# reading width
width = int(input("Enter the width: "))

# calculating area
area = length*width

# calculating perimeter
perimeter = 2*length+2*width

# printing area and perimeter
print("================")
# print strings with left justification of 11 characters
print("Area =".ljust(11),area)
print("Perimeter =".ljust(11),perimeter)
print("================")
print("Thanks for using this program!")


