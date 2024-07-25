import csv 

def adddata():
    print("\nadd data ")
    eid=input("Enter Event ID : ")
    ename=input("Enter Event name : ")
    edate=input("Enter Event date : ")
    eattendees=input("Enter number of Event Attendees : ")

    event_id.append(eid)
    event_name.append(ename)
    event_date.append(edate)
    event_attendees.append(eattendees)

    with open ('eventman.csv' , mode='w' ,newline='') as file :
        writer =csv.writer(file)
        for i in range (len(event_id)):
            writer.writerow([event_id[i],event_name[i],event_date[i],event_attendees[i]])

def viewdata():
    print("\nview data")
    print("EID \t Ename \t\t Edate \t\t Eattendees ")
    for i in range(len(event_id)):
     print(event_id[i],"\t",event_name[i],"\t",event_date[i],"\t",event_attendees[i])

def updatedata():
    print("update data")
    eid=input("Enter Event id to update : ")
    for i in range(len(event_id)):
        if(event_id[i]==eid):
            e_id=input("Enter Event ID to update : ")
            ename=input("Enter Event name to update : ")
            edate=input("Enter Event date to update : ")
            eattendees=input("Enter number of Event Attendees to update : ")

            event_id[i]=e_id
            event_name[i]=ename
            event_date[i]=edate
            event_attendees[i]=eattendees 
            with open ('eventman.csv' , mode='w' ,newline='') as file :
                writer =csv.writer(file)
                for i in range (len(event_id)):
                    writer.writerow([event_id[i],event_name[i],event_date[i],event_attendees[i]])
            
def deletedata():
    print("delete data")
    eid=input("Enter Event id to delete : ")
    for i in range(len(event_id)):
        if(event_id[i]==eid):
            event_id.pop(i)
            event_name.pop(i)
            event_date.pop(i)
            event_attendees.pop(i)
            break
            with open ('eventman.csv' , mode='w' ,newline='') as file :
                writer =csv.writer(file)
                for i in range (len(eid)):
                    writer.writerow([event_id[i],event_name[i],event_date[i],event_attendees[i]])

def total_attendees():
    total=0
    for i in range(len(event_id)):
        total+=int(event_attendees[i])
    print("Total Attndees = ",total)
    return total

def ave_attendees():
    x = total_attendees()
    average_attendees=x/len(event_id)
    print("Average Attendees = ",average_attendees)
    return average_attendees

def report():
    print("\n  Report   ")
    print("EID \t Ename \t\t Edate \t\t Eattendees ")
    for i in range(len(event_id)):
        print(event_id[i],"\t",event_name[i],"\t",event_date[i],"\t",event_attendees[i])
    total_attendees()
    ave_attendees()

event_id=[]
event_name=[]
event_date=[]
event_attendees=[]

try:
    with open ('eventman.csv',mode='r') as file:
        reader=csv.reader(file)
        for row in reader:
                event_id.append(row[0])
                event_name.append(row[1])
                event_date.append(row[2])
                event_attendees.append(row[3])
except FileNotFoundError:
    pass

count=3
while count!=0:
    uname=input("Enter the User name : ")
    upass=input("Enter User Password : ")
    if uname=="ajay" and upass=="1234" :
        print(" Login succesfulll ")
        count=1
        cnt=1
        while cnt!=0:
            print("1.Add data \n2.View data \n3.Update data \n4.Delete data \n5.Total Attendees \n6.Average Attendees \n 7.report \n8.Exit ")
            ch=int(input("Enter your choice : "))
            if ch==1:
                adddata()
            elif ch==2:
                viewdata()
            elif ch==3:
                updatedata()
            elif ch==4:
                deletedata()
            elif ch==5:
                total_attendees()
            elif ch==6:
                ave_attendees()
            elif ch==7:
                report()
            elif ch==8:
                exit()
    elif uname!="ajay":
        print("User name is incorrect !!")
    elif upass!="1234":
        print("User password is incorrect !!")
    elif uname!="ajay" and upass!="1234":
        print("Both user name and password is incorrect ")

    count-=1
    print("Remaining attmpts = ",count)