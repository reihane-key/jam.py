count=0
mystring="aaaabbaabbb"
mychar1="a"
mychar2="b"
for i in mystring:
    if i==mychar1:
       count+=1       
print(count)

    else:    
print(mystring.count(mychar2))
