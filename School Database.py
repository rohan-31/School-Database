
print('''\t\t\t\tSCHOOL DATABASE SYSTEM

          \t\t\t\tWELCOME

          \t\tChoose your preferred operation below :

          \t\t 1. View student list by Grade

          \t\t 2. View teacher list 

          \t\t 3. New student admission

          \t\t 4. New teacher appointment

          \t\t 5. Examination Grades Entry

          \t\t 6. Fee Payment

          \t\t 7. School Cafeteria ''')


x=0

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Cd@Psswrd248", database="SCHOOLADMIN")
if mydb:
    print("")
    print("Connection with MySQL established")

mycursor = mydb.cursor()


# OPERATION 1  : VIEW STUDENT LIST BY GRADE
while x < 8:
    print("")
    x=int(input(" Choose your preferred operation : " ))

    if x == 1:
        def View():
            Student_Dict={}
            mydata = mycursor.fetchall()
            for i in mydata:
                Student_Dict[i[0]] = i[1]
            for key,value in Student_Dict.items():
                print("")
                print("{0:<35}{1:<35}".format(key,value))
                print("____________________________________________________________________________")

        def Format():
            print("____________________________________________________________________________")
            print(" ADMISSION NUMBER\t\tNAME OF THE STUDENT ")
            print("____________________________________________________________________________")
            print("")
        print("")
        print(" \t\tLIST OF STUDENTS")
        print("")
        y = int(input("Enter the Grade to be viewed : "))
        print("")
        if y == 1:
            print("\t\tGrade 1")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 1")
            View()
        if y == 2:
            print("\t\tGrade 2")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 2")
            View()
        if y == 3:
            print("\t\tGrade 3")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 3")
            View()
        if y == 4:
            print("\t\tGrade 4")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 4")
            View()
        if y == 5:
            print("\t\tGrade 5")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 5")
            View()
        if y == 6:
            print("\t\tGrade 6")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 6")
            View()
        if y == 7:
            print("\t\tGrade 7")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 7")
            View()
        if y == 8:
            print("\t\tGrade 8")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 8")
            View()
        if y == 9:
            print("\t\tGrade 9")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 9")
            View()
        if y == 10:
            print("\t\tGrade 10")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 10")
            View()
        if y == 11:
            print("\t\tGrade 11")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 11")
            View()
        if y == 12:
            print("\t\tGrade 12")
            Format()
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS where Grade = 12")
            View()

# OPERATION 2 : VIEW TEACHER LIST
    if x == 2:
        print("")
        print("\t\tLIST OF TEACHERS")
        print("")
        z=input("Enter Primary Section or Secondary Section : ")
        print("")

        def View():
            Teacher_Dict={}
            mydata = mycursor.fetchall()
            for i in mydata:
                Teacher_Dict[i[0]] = i[1]
            for key,value in Teacher_Dict.items():
                print("")
                print("{0:<35}{1:<35}".format(key,value))
                print("____________________________________________________________________________")

        def Format():
            print("____________________________________________________________________________")
            print(" NAME OF THE TEACHER\t\tSUBJECTS TAUGHT ")
            print("____________________________________________________________________________")
            print("")

        z.title()
        if z == "Primary Section":
            print("\t\tLIST OF PRIMARY SECTION TEACHERS")
            Format()
            mycursor.execute("select NAME_OF_THE_TEACHER, SUBJECTS from TEACHERS where SECTION = 'Primary Section'")
            View()
        elif z == "Secondary Section":
            print("\t\tLIST OF SECONDARY SECTION TEACHERS")
            Format()
            mycursor.execute("select NAME_OF_THE_TEACHER, SUBJECTS from TEACHERS where SECTION = 'Secondary Section'")
            View()
        else:
            print("Please enter a valid section following the guidelines given above")
            
# OPERATION 3 : NEW STUDENT ADMISSION
    if x == 3:
        print("")
        print("\t\tNEW STUDENT ADMISSION")
        print("")
        def NewStudent():
            def NewAdmissionUpdate():
                mycursor.execute("insert into STUDENTS(ADMISSION_NO,NAME_OF_THE_STUDENT,FEE_RECORD,CAFETERIA_FEE_RECORD,MATHEMATICS,EVS,ENGLISH,HINDI,SCIENCE,PHYSICS,CHEMISTRY,COMPUTER_SCIENCE,GRADE) values({},'{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{})".format(c,a,n1,n1,n2,n2,n2,n2,n2,n2,n2,n2,b))
                mydb.commit()
                print("Record successfully added")

            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS")
            Student_List=[]
            Student_Dict={}
            mydata=mycursor.fetchall()
            for i in mydata:
                Student_List.append(i)
            for i in range(len(Student_List)):
                 Student_Dict[Student_List[i][0]] = Student_List[i][1]
            Fee_List = dict.fromkeys(Student_Dict,0)
            c = max(Student_Dict) + 1
            print("")
            print("Student's assigned admission number: " ,c)
            a=input("Enter the full name of the new student : ")
            b=int(input("Enter the Grade to be admitted to (GRADE 1 - 12) : "))
            n1=0
            n2="N/A"
            if b == 1:
                NewAdmissionUpdate()
            if b == 2:
                NewAdmissionUpdate()
            if b == 3:
                NewAdmissionUpdate()
            if b == 4:
                NewAdmissionUpdate()
            if b == 5:
                NewAdmissionUpdate()
            if b == 6:
                NewAdmissionUpdate()
            if b == 7:
                NewAdmissionUpdate()
            if b == 8:
                NewAdmissionUpdate()
            if b == 9:
                NewAdmissionUpdate()
            if b == 10:
                NewAdmissionUpdate()
            if b == 11:
                NewAdmissionUpdate()
            if b == 12:
                NewAdmissionUpdate()
        NewStudent()

                          
# OPERATION 4 : NEW TEACHER APPOINTMENT
    if x == 4:
        print("")
        print("\t\tNEW TEACHER APPOINTMENT")
        print("")
        def NewAppointUpdate():
            mycursor.execute("insert into TEACHERS(EMP_ID, NAME_OF_THE_TEACHER, SUBJECTS, SECTION, GRADE) values({},'{}','{}','{}',{})".format(c,d,e,f,g))
            mydb.commit()
            print("Record successfully added")
        Teacher_List=[]
        mycursor.execute("select EMP_ID, NAME_OF_THE_TEACHER from TEACHERS")
        Teacher_Dict={}
        mydata=mycursor.fetchall()
        for i in mydata:
            Teacher_List.append(i)
        for i in range(len(Teacher_List)):
            Teacher_Dict[Teacher_List[i][0]] = Teacher_List[i][1]
        Fee_List = dict.fromkeys(Teacher_Dict,0)
        c = max(Teacher_Dict) + 1
        print("")
        print("Teacher's assigned employee number: ", c)
        d=input("Enter the  full name of the New Teacher : ")
        e=input("Please enter the subjects taught by the Teacher : ")
        f=input("Please choose : (Primary Section or Secondary Section) : ")
        g=int(input("Enter the Grade in which the Teacher teaches: "))
        f.title()
        if f == "Primary Section" :
            NewAppointUpdate()
        if f == "Secondary Section" :
            NewAppointUpdate()

# OPERATION 5 : EXAMINATION GRADES ENTRY
    if x == 5:
        print("")
        print("\t\tEXAMINATION MARKS ENTRY SYSTEM")
        print("")
        def EntryofMarks():
            a=int(input("Enter Student GR.NO: "))
            print("")
            b=int(input("Enter student Grade: "))
            print("")
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS")
            mydata=mycursor.fetchall()
            Student_List=[]
            for i in mydata:
                Student_List.append(i)
            for i in range(0,len(Student_List)):
                if a == Student_List[i][0]:
                    print("Student Name: ",Student_List[i][1])

                    subject={1:("Maths","EVS","English"),
                         2:("Maths","EVS","English"),
                         3:("Maths","EVS","English","Hindi"),
                         4:("Maths","EVS","English","Hindi"),
                         5:("Maths","EVS","English","Hindi"),
                         6:("Science","English","Maths","Hindi"),
                         7:("Science","English","Maths","Hindi"),
                         8:("Science","English","Maths","Hindi"),
                         9:("Science","English","Maths","Hindi"),
                         10:("Science","English","Maths","Hindi"),
                         11:("Physics","Maths","Chemistry","English","Computer"),
                         12:("Physics","Maths","Chemistry","English","Computer")}

                    list1=[]
                    for e in subject[b]:
                        print("Enter marks for ",e)
                        q=float(input(""))
                        list1.append(q)
                    if b == 1 or b == 2:
                        mycursor.execute("update STUDENTS set MATHEMATICS = '"+str(list1[0])+"', EVS = '"+str(list1[1])+"', ENGLISH = '"+str(list1[2])+"' where ADMISSION_NO = '"+str(a)+"'")
                        mydb.commit()
                        print("Record successfully added")
                    if b == 3 or b == 4 or b == 5:
                        mycursor.execute("update STUDENTS set MATHEMATICS = '"+str(list1[0])+"', EVS = '"+str(list1[1])+"', ENGLISH = '"+str(list1[2])+"', HINDI = '"+str(list1[3])+"' where ADMISSION_NO = '"+str(a)+"'")
                        mydb.commit()
                        print("Record successfully added")
                    if b == 6 or b == 7 or b == 8 or b == 9 or b == 10:
                        mycursor.execute("update STUDENTS set SCIENCE = '"+str(list1[0])+"', ENGLISH = '"+str(list1[1])+"', MATHEMATICS = '"+str(list1[2])+"', HINDI = '"+str(list1[3])+"' where ADMISSION_NO = '"+str(a)+"'")
                        mydb.commit()
                    if b == 11 or b == 12:
                        mycursor.execute("update STUDENTS set PHYSICS = '"+str(list1[0])+"', MATHEMATICS= '"+str(list1[1])+"', CHEMISTRY = '"+str(list1[2])+"', ENGLISH = '"+str(list1[3])+"', COMPUTER_SCIENCE = '"+str(list1[4])+"' where ADMISSION_NO = '"+str(a)+"'")
                        mydb.commit()
                        print("Record successfully added")
                    stud_marks={}
                    for i in subject[b]:
                        l=subject[b].index(i)
                        stud_marks[i]=list1[l]
                    
        EntryofMarks()

# OPERATION 6 : FEE PAYMENT
    if x == 6:
        Fee_List={}
        value = 0
        def FeePayment():
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS")
            Student_List=[]
            Student_Dict={}
            mydata=mycursor.fetchall()
            for i in mydata:
                Student_List.append(i)
            for i in range(len(Student_List)):
                 Student_Dict[Student_List[i][0]] = Student_List[i][1]
            Fee_List = dict.fromkeys(Student_Dict,0)
            print('''

                        FEE PAYMENT SYSTEM

                        ENTER YOUR STUDENT ID TO PROCEED

                        SCHOOL FEES : RS. 35000 P.A ''')

            l=int(input("Please enter the Student ID : "))
            if l not in Fee_List:
                print("Invalid Student ID. Please enter a valid Student ID")
            if l in Fee_List:
                if Fee_List[l] == 0:
                    print("Fees to be paid : Rs. 35000")
                elif Fee_List[l] != 0:
                    balance = 35000 - Fee_List[l]
                    print("Fees to be paid : " , balance )
                m=int(input("Enter the amount the student wishes to pay : "))
                if m < 0 or m > 35000:
                    print("Please pay the correct amount")
                else:
                    print( '''                       ****************


                          FEE RECEIPT     ''')


                    print( '''

                NAME OF THE STUDENT : ''' , Student_Dict[l])
                    print('''              \tSTUDENT ID : '''  ,l)
                    print('''              \tAMOUNT PAID : RS ''', m)
                if m < 35000:
                    balance2 = 35000 - m
                    print("             \tAMOUNT TO BE PAID : " , balance2 )
                print('''



                          THANK YOU


                        **************** ''')
                mycursor.execute("update STUDENTS set FEE_RECORD = '"+str(m)+"' where ADMISSION_NO = '"+str(l)+"'")
                mydb.commit()
                Fee_List[l] = m
        FeePayment()

# OPERATION 7: SCHOOL CAFETERIA
    if x == 7:
        def Cafeteria():
            print( '''

                      WELCOME TO THE SCHOOL CAFETERIA
                    THE LIST OF FOOD ITEMS IS AVAILABLE BELOW
    PLEASE BE MINDFUL OF ANY ALLERGIES OR POSSIBLE REACTIONS BEFORE YOU PLACE YOUR ORDER
                     

         CODE             FOOD ITEMS                            PRICES


         1            Blackcurrant and strawberry crepes  : 50
         2            Apple and thyme pancake             : 60
         3            Hazelnut cake                       : 50
         4            Milk chocolate cookies              : 60
         5            Peach and treacle biscuits          : 70          
         6            Chickpea and tubetti penne          : 90
         7            Chicken Nuggets                     : 50
         8            Chocolate Brownie                   : 70
         9            Black Forest Cake (1 slice)         : 60
         10           White Forest Cake (1 slice)         : 60
         11           Red Velvet Cake                     : 50
         12           Samosa (4 pieces)                   : 20
         13           Garlic Bread                        : 30
         14           Muffin                              : 40
         15           Lasagna                             : 60               ''' )


            Food_List = { 1 : ["Blackcurrant and strawberry crepes" , 50],
                          2 : ["Apple and thyme pancake" , 60],
                          3 : ["Hazelnut cake" , 50],
                          4 : ["Milk chocolate cookies" , 60],
                          5 : ["Peach and treacle biscuits" , 70],
                          6 : ["Chickpea and tubetti penne" , 90],
                          7 : ["Chicken Nuggets" , 50],
                          8 : ["Chocolate Brownie" , 70],
                          9 : ["Black Forest Cake (1 slice)" , 60],
                          10: ["White Forest Cake (1 slice)" , 60],
                          11: ["Red Velvet Cake" , 50],
                          12: ["Samosa (4 pieces)" , 20],
                          13: ["Garlic Bread" , 30],
                          14: ["Muffin" , 40],
                          15: ["Lasagna"  , 60] }

            Total=0
            Quantity=0
            value=0
            mycursor.execute("select ADMISSION_NO, NAME_OF_THE_STUDENT from STUDENTS")
            Student_List=[]
            Student_Dict={}
            mydata=mycursor.fetchall()
            for i in mydata:
                Student_List.append(i)
            for i in range(len(Student_List)):
                 Student_Dict[Student_List[i][0]] = Student_List[i][1]
            Cafeteria_List = dict.fromkeys(Student_Dict,value)
            p=int(input("Enter the Student ID : "))
            if p in Cafeteria_List:
                if Cafeteria_List[p] == 0:
                        print("Fees to be paid : Rs. 5000")
                elif Cafeteria_List[p]  > 0 :
                    balance = 5000 - Cafeteria_List[p]
                    print("Fees to be paid : " , balance )
                m=int(input("Enter the amount the student wishes to pay : "))
                if m < 0 or m > 5000 - Cafeteria_List[p]:
                    print("Please pay the correct amount")
                else:
                    print( '''                           ****************


                          CAFETERIA FEE RECEIPT     ''')


                    print( '''

                NAME OF THE STUDENT : ''' , Student_Dict[p])
                    print('''                STUDENT ID : '''  ,p)
                    print('''                AMOUNT PAID : RS ''', m)
                if m < 5000:
                    balance2 = 5000 - m
                    print("                AMOUNT TO BE PAID : " , balance2 )
                print('''
                                THANK YOU


                           **************** ''')
                Cafeteria_List[p] = m
                if Cafeteria_List[p] > 0:
                    n=int(input("Enter the number of food items to be purchased : "))
                    OrderList=[]
                    while Quantity < n:
                        o=int(input("Enter the code of the food item : "))
                        OrderList.append(o)
                        Total += Food_List[o][1]
                        Quantity +=1
                    if Quantity == n:
                        m -= Total
                        Cafeteria_List[p] = m
                        print('''                           ****************
 
                            SCHOOL CAFETERIA
                            ORDER RECEIPT
 
                            ORDER SUMMARY ''')
                        for i in OrderList:
                            print("{0:<35}{1:<35}".format(Food_List[i][0],Food_List[i][1]))
                        print("Net Price : " , Total)
                        print("Your remaining cafeteria balance is : " , m)
 
                        print('''
 
                            THANK YOU
 
                           **************** ''')
                        mycursor.execute("update STUDENTS set CAFETERIA_FEE_RECORD = '"+str(m)+"' where ADMISSION_NO = '"+str(p)+"'")
                        mydb.commit()
            
        Cafeteria()
         
        
        
        


        
                
                
                
            
            
        
        
           
        
        
                
            


            
            
                    
                    
                              
            


    
        
    
        
    
            
        
            
            

        
                



    







        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
