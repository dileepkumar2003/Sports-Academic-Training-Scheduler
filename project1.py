import random 
def identification():
    flag = 0
    while flag == 0: 
        print("\nWelcome to BITM sports center !")
        ask = int(input("Choose to login as \n1.Admin, \n2.Student:\n3.exit\n  "))    
        if ask == 1:
            adminlogin()    
        elif ask == 2:
            while True:
                ask1 = int(input("Are you a Registered Student (0 for yes, 1 for no)? "))
                if ask1 == 0:
                    rstudentlogin()
                    break
                if ask1 == 1:
                    studentmenu()
                    break
                else:
                    print("Invalid input. Please try again.")
        elif ask==3:

            flag = 1 
            break
        else:
            print("Invalid input. Please try again")
def adminlogin(): 
    print("\nPlease login to access system.")
    while True:
        name = str(input("Username: "))
        pswd = str(input("Password: "))
        if (name == "deepak" and pswd == "3br22ai020") or (name == "dileep" and pswd == "3br22ai040") or (name == "bramha" and pswd == "3br22ai030") or (name == "jagan" and pswd == "3br22ai001"): #only continue if both name and pswd are correct
            print("Login Successful!")
            adminmenu()
            break
        else: 
            print("Username or password incorrect, please try again.")
def rstudentlogin():
    print("\nPlease login to access system.")
    studname = [] 
    studid = [] 
    f = open("Registered_Students_Records.txt", "r") 
    for line in f: 
        studid.append(line.split(",")[0]) 
        studname.append(line.split(",")[1]) 
    f.close()
    trylogin = True 
    flag = 0 
    while flag == 0:
        name = str(input("Username: "))
        pswd = str(input("Your Student ID: "))
        for i in studname:
            if name == i:
                index1 = studname.index(i) 
                trylogin = True 
                break
            else:
                trylogin = False
                continue 
        for j in studid:
            if pswd == j:
                index2 = studid.index(j)
                trylogin = True
                break
            else:
                trylogin = False
                continue  
        while trylogin == True: 
            if name == studname[index1] and pswd == studid[index2]: 
                print("Login Successful!")
                flag = 1
                rstudentmenu() 
                break

        while trylogin == False:
            print("Username or StudentID incorrect. Please try again.")
            break
def studentmenu():
    flag = 0
    while flag == 0: 
        print("\nWELCOME, STUDENT.")
        print("1. View details of Sport\n2. View details of Sport Schedule\n3. Register to Access Other Details\n4. Exit")
        action = int(input("Please choose an action (Enter numbers 1-4):"))
        if action == 1:
            showsportrec()
        elif action == 2:
            showschedulerec() 
        elif action == 3:
            addregstudrec()
        elif action == 4:
            flag = 1
        else:
            print("Invalid input. Please enter numbers 1-4 only.")
def rstudentmenu():
    flag = 0
    while flag == 0: 
        print("\nWELCOME, REGISTERED STUDENT!")
        print("1. View Coach Record\n2. View Self Record\n3. Provide Feedback and Rating to Coach\n4. Exit")
        action = int(input("Please choose an action (Enter numbers 1-6):"))
        if action == 1:
            showcoachrec()
        elif action == 2:
            showselfrec()
       
        
        elif action == 3:
            feedback()
        elif action == 4:
            flag = 1
            break 
        else:
            print("Invalid input. Please enter numbers 1-5 only.")    
def adminmenu():
    flag = 0
    while flag == 0: 
        print("\nWELCOME, ADMIN!")
        print("1. Add Records\n2. Display Records\n3. Attendence \n4. Exit")
        action = int(input("Please choose an action (Enter numbers 1-4):"))
        if action == 1:
            addrec() 
        elif action == 2:
            disrec() 
        elif action ==3:
            attendence()
    
        elif action==4:
            flag = 1 
        else:
            print("Invalid input. Please enter numbers 1-3 only.")
def addcoachrec():
    flag = 0
    f = open("Coach_Records.txt", "a") 
    while flag == 0: 
        print("\nEnter coach details:")
        coach_ID = input("Enter ID: ") 
        name = input("Enter name: ")
        date_join = input("Enter date joined (dd/mm/yyyy): ")
        date_term = input("Duaration: ")
        hrly_rate = input("Enter hourly rate: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        SC_code = input("Enter Sport Centre code: ")
        SC_name = input("Enter Sport Centre name: ")
        sport_code = input("Enter sport code: ")
        sport_name = input("Enter sport name: ")
        rating = input("Rating (1-5): ")
        while True:
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break 
            elif ask ==1:
                flag = 1 
                break
            else:
                print("Invalid input, please try again.")
        f.write(coach_ID +","+ name +","+ date_join +","+ date_term +","+ hrly_rate +","+ phone +","+ address +","+ SC_code +","+ SC_name +","+ sport_code +","+ sport_name +","+ rating +"\n")
    f.close() 
def addsportrec():
    flag = 0
    f = open("Sport_Records.txt", "a") 
    while flag == 0: 
        print("\nEnter Sport details:")
        sport_code = input("Enter sport code: ")
        sport_name = input("Enter sport name: ")
        while True: 
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break
            elif ask ==1:
                flag = 1
                break 
            else:
                print("Invalid input, please try again.")
        f.write(sport_code +","+ sport_name + "\n")
    f.close() 
def addsportschedulerec():
    flag = 0
    f = open("Sport_Schedule_Records.txt", "a")
    while flag == 0: 
        print("\nEnter Sport Schedule details:")
        SC_code = input("Enter Sport Centre code: ")
        SC_name = input("Enter Sport Centre name: ")
        sport_code = input("Enter sport code: ")
        sport_name = input("Enter sport name: ")
        coach_ID = input("Enter coach ID: ")
        name = input("Enter coach name: ")
        
        time_start = input("Enter start time (e.g. 12:00PM): ")
        time_end = input("Enter end time (e.g. 12:00PM): ")
        while True: 
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break 
            elif ask ==1:
                flag = 1 
                break 
            else:
                print("Invalid input, please try again.")
        f.write(SC_code +","+ SC_name +","+ sport_code +","+ sport_name +","+ coach_ID +","+ name +","+ time_start +","+ time_end + "\n") #Write inputs to text file
    f.close() 
def addregstudrec():
    flag = 0
    f = open("Registered_Students_Records.txt", "a")
    while flag == 0: 
        print("\nEnter student details:")
        stud_ID = random.randrange(100,10**3) 
        name = input("Enter student name: ")
        age = input("Enter age: ")
        sex = input("Enter gender (Male/Female): ")
        date_join = input("Enter date joined (dd/mm/yyyy): ")
        date_term = input("Duration: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        while True: 
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break 
            elif ask ==1:
                flag = 1 
                break 
            else:
                print("Invalid input. Please try again.")
        f.write(str(stud_ID) +","+ name +","+ age +","+ sex +","+ date_join +","+ date_term +","+ phone +","+ address +"\n") 
    f.close() 
    print("\nWelcome, registered student! You can now login as Registered Student at main menu (username: " + name + "; password: " + str(stud_ID)+")")    
def showcoachrec():
    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format("Coach_ID","Coach_Name","Date_Joined","Date_Terminated","Hourly_Rate","Phone_Number","Address","SC_Code","SC_Name","Sports_Code","Sports_Name","Rating"))#prints title with formatted spacing
    with open("Coach_Records.txt", "r") as f: 
        for line in f: 
            Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating = line.split(",") #split the line using comma
            print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format(Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating))
    while True:
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break
        else:
            print("Invalid input, please try again.")
def showsportrec():
    print("{0:<20}{1:<20}".format("Sports_Code","Sports_Name")) 
    with open("Sport_Records.txt", "r") as f:  
        for line in f: 
            Sports_Code, Sports_Name = line.split(",") 
            print("{0:<20}{1:<20}".format(Sports_Code, Sports_Name))
    while True: 
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break 
        else:
            print("Invalid input, please try again.")
def showregstudrec():
    print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format("Student_ID","Student_Name","Age_When_Joined","Gender","Date_Joined","Duration","Phone_Number","Address"))#prints title with formatted spacing
    with open("Registered_Students_Records.txt", "r") as f: 
        for line in f: 
            Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address = line.split(",") 
            print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format(Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address)) #print line with formatted spacing
    while True: 
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break 
        else:
            print("Invalid input, please try again.")  
def showschedulerec():
    print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}".format("SC_Code","SC_Name","Sports_Code","Sports_Name","Coach_ID","Coach_Name","Start_Time", "End_Time"))#prints title with formatted spacing
    with open("Sport_Schedule_Records.txt", "r") as f: 
         for line in f: 
            SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Start_Time, End_Time = line.split(",")
            print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}".format(SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name,  Start_Time, End_Time)) #print line with formatted spacing
    while True: 
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break
        else:
            print("Invalid input, please try again.")
def showregschedulerec():
    print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}".format("SC_Code","SC_Name","Sports_Code","Sports_Name","Coach_ID","Coach_Name","Start_Time", "End_Time"))
    with open("Registered_Sport_Schedule_Records.txt", "r") as f: 
        for line in f: 
            SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name,  Start_Time, End_Time = line.split(",") 
            print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}".format(SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Start_Time, End_Time)) #print line with formatted spacing
    while True: 
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break 
        else:
            print("Invalid input, please try again.")
def showselfrec():
    flag = 0
    while flag == 0: 
        data = input("\nEnter your name (Search is case-sensitive): ") 
        with open("Registered_Students_Records.txt", "r") as f: 
            for line in f: 
                Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address = line.split(",") 
                if line.startswith(data,4):
                    print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format("Student_ID","Student_Name","Age_When_Joined","Gender","Date_Joined","Date_Terminated","Phone_Number","Address")) #prints title with formatted spacing
                    print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format(Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address)) #print line with formatted spacing            
        while True: 
            ask = int(input("\nWould you like to search again (0 for yes, 1 for no)? "))
            if ask == 0:
                break 
            elif ask == 1: 
                flag = 1 
                break 
            else:
                print("Invalid input, please try again.")

def feedback():
    flag = 0
    f = open("Feedback.txt","a")
    while flag == 0: 
        print("Feedback Details:")
        name1 = input("Enter your name: ")
        name2 = input("Enter coach's name: ")
        fdbck = input("Feedback: ")
        rate = input("Rating (1-5): ")
        while True:
            ask = int(input("\nWould you like to add another entry? (0 for yes, 1 for no)"))
            if ask == 0:
                break 
            elif ask ==1:
                flag = 1 
                print("Thanks for the feedback!")
                break 
            else:
                print("Invalid input, please try again.")            
        f.write(name1 + "," + name2 + "," + fdbck + "," + rate +"\n") 
    f.close()  
def addrec():
    while True: 
        print("\nADD RECORDS MENU")
        print("1. Coach\n2. Sports\n3. Sport Schedule\n4. Exit")
        action = int(input("Choose item to add records of (Enter numbers 1-3) or exit (Enter number 4): "))
        if action == 1:
            addcoachrec() 
        elif action == 2:
            addsportrec() 
        elif action == 3:
            addsportschedulerec() 
        elif action == 4:
            break 
        else:
            print("Invalid input. Please enter numbers 1-4 only.")
def disrec():   
    while True: 
        print("\nDISPLAY RECORDS MENU")
        print("1. Coach\n2. Sports\n3. Registered Students\n4. Exit")
        action = int(input("Choose item to display records of (Enter numbers 1-3) or exit (Enter number 4): "))
        if action == 1:
            showcoachrec() 
        elif action == 2:
            showsportrec() 
        elif action == 3:
            showregstudrec() 
        elif action == 4:
            break 
        else:
            print("Invalid input. Please enter numbers 1-4 only.")
def attendence(): 
   flag=0
   while flag==0: 
    action=int(input("1. Mark attendence \n2. Monitor attendence \n3. Exit\n Enter your choice 1-2:"))
    if action==1:
        markatten()
    elif action == 2:
        monitoratten()
    elif action==3:
        flag=1
    else:
        print("Invalid input. Please enter numbers 1-3 only.")
def markatten():
   flag=0
   while flag==0: 
    action=int(input("1.coach\n2.student\n3.Exit\nEnter your choice 1-3:"))
    if action==1:
        markattecoach()
    elif action == 2:
        markattestudent()
    elif action==3:
        flag=1
    else:
        print("Invalid input. Please enter numbers 1-3 only.")
def monitoratten():
   flag=0
   while flag==0: 
    action=int(input("1.coach\n2.student\n3.Exit\nEnter your choice 1-3:"))
    if action==1:
        disattecoach()
    elif action == 2:
        disattestudent()
    elif action==3:
        flag=1
    else:
        print("Invalid input. Please enter numbers 1-3 only.")
def markattecoach():
    flag = 0
    f = open("Coach_attendence.txt", "a") 
    while flag == 0: 
        print("\nEnter coach details:")
        coach_ID = input("Enter ID: ") 
        name = input("Enter name: ")
        Attendence = input("Enter Attendence: ")        
        while True: 
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break 
            elif ask ==1:
                flag = 1
                break 
            else:
                print("Invalid input, please try again.")
        f.write(coach_ID +","+ name +","+ Attendence +"\n")
    f.close()
def markattestudent():
    flag = 0
    f = open("Student_attendence.txt", "a") 
    while flag == 0: 
        print("\nEnter Student details:")
        student_ID = input("Enter ID: ") 
        name = input("Enter name: ")
        Attendence = input("Enter Attendence: ")
        while True: 
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break 
            elif ask ==1:
                flag = 1 
                break 
            else:
                print("Invalid input, please try again.")
        f.write(student_ID +","+ name +"," + Attendence +"\n")
    f.close()
def disattecoach():
    print("{0:<10}{1:<13}{2:>15}".format("Coach_ID","Coach_Name","Attendence"))
    with open("Coach_attendence.txt", "r") as f: 
        for line in f: 
            Coach_ID, Coach_Name ,Attendence = line.split(",") 
            print("{0:<10}{1:<13}{2:>15}".format(Coach_ID, Coach_Name , Attendence))
    while True: 
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break 
        else:
            print("Invalid input, please try again.")
def disattestudent():
    print("{0:<10}{1:<13}{2:>15}".format("Student_ID","Student_Name", "Attendence"))
    with open("Student_attendence.txt", "r") as f: 
        for line in f: 
            Student_ID, Student_Name, Attendence  = line.split(",") 
            print("{0:<10}{1:<13}{2:>15}".format(Student_ID, Student_Name ,  Attendence))
    while True: 
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break 
        else:
            print("Invalid input, please try again.")
identification()