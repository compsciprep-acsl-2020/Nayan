# Name: Nayan Nathi
# Grade: 8th
# Division: Junior-5 (Python)
# Contest1 Year: 2012-2013
# Team: Herndon Test Prep
# Program:Junior Division: Time Sheets
#start of data collection
input = open("Timesheetstext")
inpu = input.read()
inpu=inpu.replace(",","")
inpu= inpu.split("\n")
one=inpu[0]
two=inpu[1]
three=inpu[2]
four=inpu[3]#end of data collection
def time(a):
    timesheet = {"1": 9, "2": 9.5, "3": 10, "4": 10.5, "5": 11, "6": 11.5, "7": 12, "8": 12.5, "9": 13, "A": 13.5,
                 "B": 14, "C": 14.5, "D": 15, "E": 15.5, "F": 16, "G": 16.5, "H": 17}
    if len(a)==4: #if loco is 2 digit
        b=int(a[0:2])#loco
        c = a[2]  # start
        d = a[3]  # end
    else:
        b = int(a[0])  # loco
        c = a[1]  # start
        d = a[2]  # end
    e=timesheet[d]-timesheet[c]#totalwork time
    if (1<=b<=9):
        f=10
        return(f*e)#loco one through nine
    elif (10<=b<=19):
        if e <= 4:
            return(e*8)#loco 10through 19
        else:
            return (32+(e-4)*12)#if greater than 4 hours
    elif (20<=b<=29):
        if e <=4:
            return (e*12)#loco 20 through 29
        else:
            return(48+(e-4)*24)#if greater than 4 hours

print(str(time(one))+".00")
print(str(time(two))+".00")
print(str(time(three))+".00")
print(str(time(four))+"0")
print(str(time(one)+time(two)+time(three)+time(four))+"0")
