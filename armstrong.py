t1 = int(input('Enter the minimum value of the range:'))
t2 = int(input('Enter the maximum value of the range:'))
n=len(str(t2))
print('The Armstrong numbers in this range are: ')

for j in range(t1, t2+1):
    i=j
    cube_sum = 0
    while i!= 0:
        k = i % 10
        cube_sum += k**n
        i = i//10
    if cube_sum == j:
                     print(j)