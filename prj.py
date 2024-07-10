uname="project"
upass="123"
count=0

uname=input("ENTER THE USERNAME=")
upass=input("ENTER THE PASSWORD=")

if uname==uname and upass==upass:
    print("LOGIN SUCCESSFUL")
elif(uname!=uname):
    print("INCORRECT USERNAME")
elif(upass!=upass):
    print("INCORRECT PASSWORD")
elif(uname!=uname and upass!=upass):
    print("BOTH ARE INCORRECT")
count-=1