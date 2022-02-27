sub1 = int(input("enter first subject marks:\n  "))
sub2 = int(input("enter 2nd sub marks:\n"))
sub3 = int(input("enter 3rd sub marks:\n"))
if sub1<33 or sub2<33 or sub3<33:
    print("u r fail beause your marks is less then 33")
elif (sub1+sub2+sub3)/3<40:
    print("you are fail")
else:
    print("congratulations! u r pass")        