numbers ="1,2,3,4,5,6,7,8,9,0"

total=0

a = input("Please Write Hier:")
for i in a:
    if i in numbers:
        total += int(i)

print(total)