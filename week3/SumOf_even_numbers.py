sum=0
count_3=0
count_5=0
for i in range(1,51):
    if i%2==0:
        if i%3==0:
            count_3+=1
            print("Three")
        elif i%5==0:
            count_5+=1
            print("Five")
        else:
         sum+=i
print(f"sum: {sum}")
print(f"Number of times 3 replaced is {count_3}")
print(f"Number of times 5 replaced is {count_5}")
