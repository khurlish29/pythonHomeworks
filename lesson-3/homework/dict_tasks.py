#task1
d={"Name ": "Ken", "Age": 20, "Occupation" : "Sales assistant"}
key="Age" 
default = "-"
if key in d:
    print(d.get(key,default))
else:
    print(default)

#task2
print(key in d)

#task3
print(len(d))

#task4
print(list(d.keys()))

#task5
print(list(d.values()))

#task6
d1={"color": "red", "size": "medium"}
d2={"color": "blue", "size": "small"}
d1.update(d2)
print(d1)

#task7
print(d.pop(key,None))

#task8
d={}
print(d)

#task9
print(not bool(d))

#task10
if key in d:
    print(key,d[key])
else:
    None


#task11
value=23
d[key]=value
print(d[key])

#task12
print(list(d.values()).count(value))

#task13
print(dict((v,k) for k, v in d.items()))

#task14
for k,v in d.items():
    if v==value:
        print(k)


#task15
keys = ["Zoe", "John"]
values =[98,85]
newD = dict(zip(keys,values))
print(newD)

#task16
for value in d.values():
    if isinstance(value,dict):
        print("true")
    else:
        print("false")

#task17
data = {'0': {'id': 1245, 'name': 'Ben', 'mark':97}, '1':             
   {'id': 7654, 'name': "Tom", 'mark': 83}}
print(list(data.values())[0]['mark'])

#task18
defaultVal = "not available"
print(defaultdict(lambda:defaultVal))

#task19
print(len(set(d.values())))


#task20
print(dict(sorted(d.items())))

#task21
newD=dict(sorted(d.items(),key=lambda item:item[1]))
print(newD)

#task22
newDict = {'a':10, 'b':20, 'c':30}
print({k: v for k, v in newDict.items() if v>15})

#task23
print(set(d1.keys())&set(d2.keys()))

#task24
tuples = [("a","b"),("c","d")]
print(dict(tuples))

#task25
print(next(iter(d.items()),None))