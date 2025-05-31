n = int(input())
numbers = []

for i in range(n):
    age, name = input().split()
    numbers.append([int(age), name])
    
numbers.sort(key = lambda x : int(x[0]))
 
for i in numbers:
    print(i[0], i[1])