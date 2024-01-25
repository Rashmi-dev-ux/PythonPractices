#Check if number is binary or not

num = int(input("Enter the number: "))
while(num>0):
    j = num%10
    if j!= 0 and j!=1:
        print("It is not a binary number")
        break
    num = num//10
    if num == 0:
        print("It is binary number")