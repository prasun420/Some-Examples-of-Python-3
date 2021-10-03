dictionary={}
while True:
        a=input("Enter voter no :")
        print()
        b=input("Enter Party name: ")
        print()
        dictionary[a]=b
        if a=="exit":
            break
print(dictionary)
bjp=0
tmc=0
none=0
for i in dictionary:
    if dictionary[i] =='bjp':
        bjp=bjp+1
    if dictionary[i] =='tmc':
        tmc=tmc+1
    if dictionary[i] =='none':
        none=none+1
list1=[bjp,tmc,none]
if max(list1)==bjp:
    print("BJP WINNER")
if max(list1)==tmc:
    print("TMC WINNER")
else:
    print("None Winner")
