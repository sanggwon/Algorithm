celendar = {
    1:31,2:28,3:31,4:30,5:31,6:30,
    7:31,8:31,9:30,10:31,11:30,12:31
}
weeks = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"] 

count_week = 0
for month,count in celendar.items() : ## 딕셔너리 반복
    print(f"{month:10} 월") ## formating
    for week in weeks :
        print(f"{week}", end =" ")
    print()    
    print("   "*(count_week),end="")
    for day in range(1,count+1) :
        print(f"{day:2}",end=" ")
        count_week  += 1
        if count_week == 7 :
            print()
            count_week = 0
    print() 
    print()