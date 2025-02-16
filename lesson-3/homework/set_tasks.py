s1={1,2,3,4,5}
s2={9,7,4,2,3}

#task1
print(s1|s2)

#task2
print(s1&s2)

#task3
print(s1-s2)

#task4
print(s1.issubset(s2))

#task5
el=2
print(el in s1)

#task6
print(len(s1))

#task7
l = [1,2,3,4,3,2,7]
print(set(l))

#task8
print(s1.discard(el))

#task9
print(s1.copy().clear())

#task10
print(len(s1)==0)

#task11
print(s1^s2)

#task12
newEl = 8
print(s1.add(newEl))

#task13
if el in s1:
    s1.pop(newEL)
else:
    None

#task14
maxEl = max(s1,default=None)
print(maxEl)

#task15
minEl = min(s1,default=None)
print(minEl)

#task16
print({x for x in s1 if x%2==0})

#task17
print({x for x in s1 if x%2!=0})

#task18
rangedSet = set(range(1,11))
print(rangedSet)

#task19
l2= [4,5,7,9]
print(set(l+l2))

#task20
print(s1.isdisjoint(s2))

#task21
newL=[1,2,2,6,7,9,3,3,1]
print(list(set(newL)))

#task22
print(len(set(newL)))

#task23
import random
randSet = {random.randint(1,10) for _ in range(5)}
print(randSet)
