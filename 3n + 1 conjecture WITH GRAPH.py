import matplotlib.pyplot as plt

num = int(input("Enter the number: "))

def output(num):
    if num % 2 == 0:
        num_2 = num//2
    else:
        num_2 = (3*num)+1
        
    return num_2

li = [num]

num_2 = output(num)
    
print(num_2)

li.append(num_2)

count = 1

while num_2 != 1:
    num_2 = output(num_2)
    print(num_2)
    li.append(num_2)
    count += 1

print("Count:", count)

li_2 = []

for i in range(1, count+2):
    li_2.append(i)

plt.plot(li, li_2)