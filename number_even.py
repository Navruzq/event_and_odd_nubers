#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
a=1357

x1=a%10
a=a//10

x2=a%10
a=a//10

x3=a%10
a=a//10

x4=a%10
a=a//10

s=x1%2+x2%2+x3%2+x4%2-4
s=s*(-1)
print(s)

