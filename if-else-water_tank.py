min=eval(input("Enter the Time in minute "))

# capacity of tank in miter
height= 10
radius= 5
a = 3.14*height*radius*radius

b= (min*15)-a     #overflow water
d= (min*15)/(3.14*5*5)      #filled height 
c= 10-d    #remaining height

#flow rate = 15m^3/m

if (min*15) > a:
    print(f"Overflow = {b:.2}")
    print("overflow") 
elif (min*15) < a:
    print("Underflow")
    print(f"filled height = {d:.2} , remmaing height {c:.2}")
else:
    print("Full")
