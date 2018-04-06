#family members and their age
name=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T')
age=(10,11,12,13,14,15,16,17,18,19,70,21,22,93,24,25,86,27,9,40)

print("20 family members are : ")
print(name)
print(age)
   
print("child group:")   
for i in range(20):
    if age[i]<=10:
        print(name[i],age[i])

print("youth group :")
for i in range(20):
    if age[i]>10 and age[i]<=20:
        print(name[i],age[i]) 

print("middle group :")
for i in range(20):
    if age[i]>20 and age[i]<45:
        print("age:",age[i])  

print("senior group :")
for i in range(20):
    if age[i]>=46:
        print(name[i],age[i])