# YOUR CODE HERE
l1 = []
l2 = []

n = int(input())

for i in range(n):
    q1 = int(input())
    l1.append(q1)

for i in range(n):
    q2 = int(input())
    l2.append(q2)

def summation(l1,l2):
    udl = []
    global n
    for i in range(n):
        sum = l1[i]+l2[i]
        udl.append(sum)
    return udl
udl = summation(l1,l2)

print(summation(l1,l2))

def find_min_max(udl):
    min = udl[0]
    max = udl[0]
    for i in udl :
        if i < min:
            min = i

    for i in udl :
        if i > max:
            max = i

    find_min_max = (min,max)
    return find_min_max
print(find_min_max(udl))
