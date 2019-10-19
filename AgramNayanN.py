#predata
input = open("AgramText")
inpu = input.read()
inpu=inpu.replace(",","")
inpu= inpu.split("\n")
one=inpu[0]
two=inpu[1]
three=inpu[2]
four=inpu[3]
five=inpu[4]

def Agram(inpu):

    oppo=inpu[:2]
    li=inpu[2:12]
    test1=[]#Finding same suites
    test2=[]#cards possible for rule 2
    test3=[]#integer for rule two

    for i in li:
        if i==inpu[1]:
            test1.append(li[li.index(i)-1]+i)
            li=li[(li.index(i)+1):]

    test1=sorted(test1)

    if test1==[]:
        return"NONE"#rule one end

    for j in test1:
        test2.append((str(j)).replace(str(inpu[1]),""))

    for k in test2:
        if int(inpu[0])<int(k):
            test3.append(k)

    if len(test3)==0:
        return (min(test1)[0] + "," + min(test1)[1])#end of 3rd rule

    if int(max(test3)[0]) > int(inpu[0]):
        return (max(test1)[0]+','+max(test1)[1])#end of 2nd rule

print(Agram(one))
print(Agram(two))
print(Agram(three))
print(Agram(four))
print(Agram(five))
