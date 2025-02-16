tpl = (1,3,4,5,7,8,9,3,2)

#task1
el=3
print(tpl.count(el))

#task2
if tpl:
    print(max(tpl))
else:
    None

#task3
if tpl:
    print(min(tpl))
else:
    None

#task4
print(el in tpl)

#task5
if tpl:
    print(tpl[0])
else:
    None

#task6
if tpl:
    print(tpl[-1])
else:
    None

#task7
print(len(tpl))

#task8
print(tpl[:3])

#task9
tpl2=(6,2,12)
print(tpl+tpl2)

#task10
print(len(tpl)==0)

#task11
print([i for i, x in enumerate(tpl) if x == el])

#task12
u = sorted(set(tpl), reverse=True)
if len(u) > 1:
    print(u[1])
else:
     None

#task13
u = sorted(set(tpl))
if len(u) > 1:
    print(u[1])
else:
     None

#task14
print(42,)

#task15
l=[21,34,65]
print(tuple(l))

#task16
sortCheck = tpl == tuple(sorted(tpl))
print(sortCheck)



#task17
start, end = 1, 5
sub_max = max(tpl[start:end]) if tpl[start:end] else None
print(sub_max)


#task18
sub_min = min(tpl[start:end]) if tpl[start:end] else None
print(sub_min)


#task19
if el in list(tpl):
    list(tpl).remove(el)
print(tuple(list(tpl)))


#task20
print(((1, 2), (3, 4), (5, 6)))


#task21
repeat_count = 2
print(tuple(x for x in tpl for _ in range(repeat_count)))

#task22
print(tuple(range(1, 11)))

#task23
print(tpl[::-1])

#task24
print(tpl==tpl[::-1])

#task25
seen=set()
print(tuple(x for x in tpl if not (x in seen or seen.add(x))))