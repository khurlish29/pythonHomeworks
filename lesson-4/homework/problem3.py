txt = input("Enter a string:")
skip = "aeiou"
result = ""
cnt =0
for i in range(len(txt)):
    cnt+=1
    result+=txt[i]
    if i!=len(txt)-1 and cnt>=3 and txt[i] not in skip:
        skip +=txt[i]
        result+="_"
        cnt=0
print(result)