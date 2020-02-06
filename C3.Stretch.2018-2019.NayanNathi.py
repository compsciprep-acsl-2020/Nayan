# Name: Nayan Nathi
# Grade: 7th
# Division: Junior-5 (Python)
# Contest3 Year: 2018-2019
# Team: Herndon Test Prep
# Program:Junior Division: Stretch

for Line in (open("Stretchtxt","r")):
    
    Final = []
    lastcolumn = []
    Final_check = []
    
    Row = int(Line.split(" ")[0])
    Column= int(Line.split(" ")[1])
    Start = int(Line.split(" ")[2])
    NumberOfBlocked = int(Line.split(" ")[3])
    LastNumber = Start - 1
    
    if NumberOfBlocked > 0:
        blocked = Line.split(" ")[4:]
    else:
        blocked = [0]
        
    for Number in range(0, Row + 1):
        blocked.append((Number * Column) + 1)
        
    for Number in range((Row * Column) + 1, ((Row * Column) + 12)):
        blocked.append(Number)
    blocked.remove(Start)
    
    for Number in blocked:
        blocked[blocked.index(Number)]=int(Number)
    Number = 0
    
    while (Number != Row * Column):
        Number = Number + Column
        lastcolumn.append(Number)
        
    if Start == 1:
        pass
    else:
        lastcolumn.remove(Start - 1)

    while(not(LastNumber in lastcolumn)):
        
        LastNumberset_A = LastNumber
        
        if not(LastNumber + 1 in blocked):
            LastNumber = LastNumber + 1
            if not (LastNumber + 1 in blocked):
                LastNumber = LastNumber + 1
                if not (LastNumber + 1 in blocked):
                    LastNumber = LastNumber + 1
                    Final.append("A")
                else:
                    LastNumber = LastNumberset_A
            else:
                LastNumber = LastNumberset_A
        else:
            LastNumber = LastNumberset_A
            
        LastNumberset_B = LastNumber
        
        if not(LastNumber + 1 in blocked):
            LastNumber = LastNumber+1
            if not (LastNumber + Column in blocked):
                LastNumber = LastNumber + Column
                if not (LastNumber + 1 in blocked):
                    LastNumber = LastNumber + 1
                    Final.append("B")
                else:
                    LastNumber = LastNumberset_B
            else:
                LastNumber = LastNumberset_B
        else:
            LastNumber=LastNumberset_B
            
        LastNumberset_C = LastNumber
        
        if not(LastNumber + 1 in blocked):
            LastNumber = LastNumber+1
            if not (LastNumber + 1 in blocked):
                LastNumber = LastNumber + 1
                if not (LastNumber + Column in blocked):
                    LastNumber = LastNumber + Column
                    if not (LastNumber + Column in blocked):
                        LastNumber = LastNumber + Column
                        Final.append("C")
                    else:
                        LastNumber = LastNumberset_C
                        continue
                else:
                    LastNumber = LastNumberset_C
                    continue
            else:
                LastNumber = LastNumberset_C
                continue
        else:
            LastNumber=LastNumberset_C
            continue

    print ("".join(Final))
