print("Enter birthyear:")
Year = str(input())
print("Enter birthmonth")
Month = int(input())
print("Enter birthday")
Day= int(input())

#YC
YC = int(Year[-2:])
YC = (YC + (YC//4))%7

#MC
monthcode = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
MC = monthcode[Month-1]


#CC
GregValues = [4, 2, 0, 6, 4, 2, 0]
GregYears = [17, 18, 19, 20, 21, 22, 23]
CC = int(Year[0:2])
for i in range(7):
    if GregYears[i] == CC:
        CC = GregValues[i]


#DN
DN = int(Day)


# LC
LC = 0
if Month == 1 or Month == 2:
    if int(Year)%4 == 0 and int(Year)%100 != 0:
        LC = 1
if int(Year)%400 == 0:
    LC = 1

Datelist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
Number = (YC + MC + CC + DN - LC)%7
dateOfweek = Datelist[Number]
print("YC:" + str(YC))
print("MC:" + str(MC))
print("CC:" + str(CC))
print("DN:" + str(DN))
print("LC:" + str(LC))
print("You were born " + dateOfweek + "!")
