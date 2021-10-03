s= input(" Enter a string: ")
v=['a','e','i','o','u']
s=s.lower()
for i in s:
    if i in v:


        s=s.replace(i," ")
        print(s)
