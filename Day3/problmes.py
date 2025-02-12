# numbers = [2, 13, 17, 19, 22, 33]
# new_list = []

list = list(range(5,20))
prime=[]
for each in list:
    
    if each < 2:
        continue
    else:
        count = 0
        for i in range(2,each):
            if each % i == 0:
                count += 1
                break
        if(count==0):
            prime.append(each)
            print(each)
print(prime)


count = 0
for i in list:
    for j in range(1,i+1):
        if i % j == 0:
            count+=1
    if count < 3:
        print(i)
list = range(1,100)