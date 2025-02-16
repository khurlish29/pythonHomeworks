l = [1,3,2,3,4,5,6,3,2,4]
#task1_count_occurrences
el=3
l.count(el)

#task2_sum_of_elements
total = sum(l)
print(total)

#task3_maxEl
maxEl = max(l)
print(maxEl)

#task4_minEl
minEl = min(l)
print(minEl)

#task5_checkEl
el=4
el in l

#task6_firstEl
if(l):
    print(l[0])
else:
    print("list is empty")


#task7_lastEl
if (l):
    print(l[-1])
else:
    print("the list is empty")

#task8_newL
newL = l[:3]
print(newL)

#task9_reverse
reverse = l[::-1]
print(reverse)

#task10_sort
srtL = sorted(l)
print(srtL)

#task11_remove
rd = list(dict.fromkeys(l))
print(rd)

#task12_insert
l.insert(11,9)
print(l)

#task13_index
inX = l.index(el) if el in l else -1
print(inX)


#task14_empty
if (l):
    print("list is not empty")
else:
    print("list is empty")


#task15_even
s=0
for e in l:
    if (e%2==0):
        s+=1
print(s)

#task16_odd
s=0
for e in l:
    if (e%2!=0):
        s+=1
print(s)

#task17_concatenate
l2=[9,3,2]
print(l+l2)

#task18_findSub
sl=[3,2]

#task19_replace
if el in l:
    l[l.index(el)] = 12

#task20_secLar
sList = sorted(set(l))
if len(sList)>1:
    secLar = sList[-2]
print(secLar)

#task21_secSmall
if len(secSmall)>1:
    print(sList[1])

#task22_eveNum
eveNums=[]
for e in l:
    if (e%2==0):
        eveNums.append(e)
print(eveNums)

#task23_odd
oddNums=[]
for e in l:
    if (e%2!=0):
        oddNums.append(e)
print(oddNums)

#task24_len
print(len(l))

#task25_copy
copyList = l.copy()
print(copyList)

#task26_mid
mid = len(l)//2
if len(l)%2!=0:
    print(l[mid])
else:
    print(l[mid-1:mid+1])

#task27_maxSub
print(max(l[2:4+1], default=None))

#task28_minSub
print(min(l[2:5+1], default=None))

#task29_remove
index = 4
if 0 <= index < len(l):
    del l[index]


#task30
print(l==sorted(l))

#task31
print([x for x in l for _ in range(2)])

#task32
print(sorted(l + l2))

#task33
print([i for i, x in enumerate(l) if x == el])

#task34
print(l[-2 % len(l):] + l[:-2 % len(l)])

#task35
print(list(range(1, 11)))

#task36
print(sum(x for x in l if x > 0))

#task37
print(sum(x for x in l if x<0))

#task38
print(l==l[::-1])

#task39
print([l[i:i+3] for i in range(0, len(l), 3)])

#task40
seen=set()
print([x for x in l if not (x in seen or seen.add(x))])
