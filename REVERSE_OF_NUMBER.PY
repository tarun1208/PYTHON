#REVERSE OF A NUMBER
n=int(input("Enter the Number: "))
org=n
num=0
while n!=0:
     rem=n%10
     num=(num*10)+rem
     n=n//10
print("The Reverse of ",org,"number is:",num)
