# Name: Nayan Nathi
# Grade: 7th
# Division: Junior-5 (Python)
# Contest3 Year: 2018-2019
# Team: Herndon Test Prep
# Program:Junior Division: Stretch

for x in (open("Stretchtxt","r")):
    final = []
    lastcolumn = []
    final_check = []
    r = int(x.split(" ")[0])
    c = int(x.split(" ")[1])
    s = int(x.split(" ")[2])
    n = int(x.split(" ")[3])
    lastnum = s-1
    
    if n > 0:
        blocked = x.split(" ")[4:]
    else:
        blocked = [0]
    for i in range(0, r + 1):
        blocked.append((i * c) + 1)
    for i in range((r * c) + 1, ((r * c) + 12)):
        blocked.append(i)
    blocked.remove(s)
    for i in blocked:
        blocked[blocked.index(i)]=int(i)
    i = 0
    while (i != r * c):
        i = i + c
        lastcolumn.append(i)
    if s == 1:
        pass
    else:
        lastcolumn.remove(s - 1)

    while(not(lastnum in lastcolumn)):
        lastnumset_A = lastnum
        if not(lastnum+1 in blocked):
            lastnum=lastnum+1
            if not (lastnum + 1 in blocked):
                lastnum = lastnum + 1
                if not (lastnum + 1 in blocked):
                    lastnum = lastnum + 1
                    final.append("A")
                else:
                    lastnum = lastnumset_A
            else:
                lastnum = lastnumset_A
        else:
            lastnum=lastnumset_A
        lastnumset_B=lastnum
        if not(lastnum+1 in blocked):
            lastnum=lastnum+1
            if not (lastnum + c in blocked):
                lastnum = lastnum + c
                if not (lastnum + 1 in blocked):
                    lastnum = lastnum + 1
                    final.append("B")
                else:
                    lastnum = lastnumset_B
            else:
                lastnum = lastnumset_B
        else:
            lastnum=lastnumset_B
        lastnumset_C = lastnum
        if not(lastnum+1 in blocked):
            lastnum=lastnum+1
            if not (lastnum + 1 in blocked):
                lastnum = lastnum + 1
                if not (lastnum + c in blocked):
                    lastnum = lastnum + c
                    if not (lastnum + c in blocked):
                        lastnum = lastnum + c
                        final.append("C")
                    else:
                        lastnum = lastnumset_C
                        continue
                else:
                    lastnum = lastnumset_C
                    continue
            else:
                lastnum = lastnumset_C
                continue
        else:
            lastnum=lastnumset_C
            continue

    print ("".join(final))