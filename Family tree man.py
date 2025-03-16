def add():
    perid=input("ENTER THE PERSON ID=")
    name=input("ENTER THE NAME=")
    dob=input("ENTER THE BIRTHDATE=")
    relation=input("ENTER THE RELATION=")
    notes=input("ENTER THE NOTES=")
    age=int(input("ENTER THE AGE="))

    f_perid.append(perid)
    f_name.append(name)
    f_dob.append(dob)
    f_relation.append(relation)
    f_notes.append(notes)
    f_age.append(age)

def viewfamily():
    print("perid \t name \t dob \t relation \t notes \t age")
    for i in range(len(f_perid)):
        print(f_perid[i],"\t",f_name[i],"\t",f_dob[i],"\t",f_relation[i],"\t",f_notes[i],"\t",f_age[i])

def delete():
    dperid=input("ENTER THE PERSON ID=")
    for i in range(len(f_perid)):
        if(f_perid[i]==dperid):
            f_perid.remove(f_perid[i])
            f_name.remove(f_name[i])
            f_dob.remove(f_dob[i])
            f_relation.remove(f_relation[i])
            f_notes.remove(f_notes[i])
            f_age.remove(f_age[i])
            print("RECORD DELETED SUCCESSFULLY")
            break

def update():
    dperid=input("ENTER THE PERSON ID=")
    for i in range(len(f_perid)):
        if(f_perid[i]==dperid):
            uperid=input("ENTER THE PERSON ID=")
            uname=input("ENTER THE NAME=")
            udob=input("ENTER THE DATE OF BIRTH=")
            urelation=input("ENTER THE RELATION=")
            unotes=input("ENTER THE NOTES=")
            uage=input("ENTER THE AGE=")
            f_perid[i]=uperid
            f_name[i]=uname
            f_dob[i]=udob
            f_relation[i]=urelation
            f_notes[i]=unotes
            f_age[i]=uage
            break

def countmembers():
    ct=0
    for i in range(len(f_perid)):
         ct+=1
    print(ct)
        
def relation():
   print("f_name  \t  f_relation")
   for i in range(len(f_perid)):
       print(f_name[i], "   =    \t", f_relation[i])
       
def average():
    sum = 0
    for i in range(len(f_age)):
        sum += int(f_age[i])
    avg = sum / len(f_age)
    print(avg)


f_perid=[]
f_name=[]
f_dob=[]
f_relation=[]
f_notes=[]
f_age=[]
count=3
while(count!=0):

    uname=input("ENTER THE USERNAME=")
    upass=input("ENTER THE PASSWORD=")
    username="rohan"
    password="5595"

    if(uname==username and upass==password):
        print("LOGIN SUCCESSFUL")
        count=1
        cnt=1
        while(cnt!=0):
            print("FAMILY TREE MANAGER")
            print("1.ADD FAMILY")
            print("2.VIEW FAMILY")
            print("3.DELETE FAMILY")
            print("4.UPDATE FAMILY")
            print("5.TOTAL NUMBER OF FAMILY MEMBERS ")
            print("6.LIST OF MEMBERS BY RELATION")
            print("7.AVERAGE AGE OF FAMILY MEMBERS")
            print("8.EXIT")
            ch=int(input("ENTER YOUR CHOICE="))

            if ch==1:
                print("ADD FAMILY")
                add()
            if ch==2:
                print("VIEW FAMILY")
                viewfamily()
            if ch==3:
                print("DELETE FAMILY")
                delete()
            if ch==4:
                print("UPDATE FAMILY")
                update()
            if ch==5:
                print("NUMBERS OF FAMILY MEMBERS=")
                countmembers()
            if ch==6:
                print("lIST- MEMBERS BY REALATION =")
                relation()
            if ch==7:
                print("AVERAGE AGE OF FAMILY MEMBERS=")
                average()
            if ch==8:
                print("EXIT")
                cnt=0
    elif(uname!=username and upass!=password):
        print("BOTH ARE INCORRECT")
    elif(uname!=username):
        print("INCORRCET USERNAME")
    elif(upass!=password):
        print("INCORRECT PASSWORD")
    count-=1