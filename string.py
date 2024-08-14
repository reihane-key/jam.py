temp = input("please enter your string")
sum = 0
for i in range(len(temp)):
	if temp[i] == 'b':
	    sum = sum + 1
print("Your string has "+str(sum)+" 'b' character")
