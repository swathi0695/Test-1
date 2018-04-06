import numpy as np
a=[12,6,48,37,54,11,60,122,105,88,122,155,105]

#sorting
print(np.sort(a)) 
b=np.sort(a)
print("Enter a search key :")
key=int(input())

#iterating to find the key 
for i in range(len(b)):
    if key==b[i]:
        print("Key :",key)
        print("Position :",i)







"""def fun():
    print(np.sort(a1)) 
    b=np.sort(a)
    print("Enter a search key :")
    key=int(input())
    
    #iterating to find the key 
    for i in range(len(b)):
        if key==b[i]:
            print("Key :",key)
            print("Position :",i)"""
        