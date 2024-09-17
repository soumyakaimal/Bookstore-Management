# Name : SOUMYA KAIMAL
# Class : XII-A
# School Roll Number : 17
# Board Roll Number :______
# Shift : 1st Shift
# School : Kendriya Vidyalaya Andrews Ganj

# Project Report on : 'BOOKSTORE MANAGEMENT SYSTEM'

#Title
print('''
---------------------------------------------------------------------------------------------------
-----------------------------------"BOOKSTORE MANAGEMENT SYSTEM"-----------------------------------
------------------------------------------"ABC Bookstore"------------------------------------------
---------------------------------------------------------------------------------------------------''')

#Connecting Python and MySQL
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='root')

#Creating Database
mycursor=mydb.cursor()
mycursor.execute('create database if not exists Bookstore')
mycursor.execute('use Bookstore')

#Creating Table for Sign Up
mycursor.execute('create table if not exists Signup(Username varchar(20), Password varchar(20))')

while True:

    print('''
-------------------------
HOME PAGE

1: Sign Up
2: Login
3: Help
4: Exit
-------------------------
''')

    a=input('Enter your choice - (1 to 4) : ')  #a

#For Sign Up
    if a=='1':
        print('\n---FOR SIGN UP---\n')

        username=input('Create a username : ')
        password=input('Create a password : ')

        mycursor.execute("insert into Signup values('"+username+"','"+password+"')")
        mydb.commit()

        print('\nSign Up Successful...!!!')

#For Login
    elif a=='2':
        print('\n---FOR LOGIN---\n')

        username=input('Enter your username : ')

        mycursor.execute("select Username from Signup where Username='"+username+"'")
        b=mycursor.fetchone()   #b

        if b is not None:
            print('Valid Username...!!!\n')

            password=input('Enter your password : ')

            mycursor.execute("select Password from Signup where Password='"+password+"'")
            b1=mycursor.fetchone()   #b1

            if b1 is not None:
                print('Valid Password...!!!')

                print('\nLogin Successful...!!!')

#Welcome Message
                print('''
---------------------------------------------------------------------------------------------------
------------------------------------Welcome to \"ABC Book Store\"------------------------------------
---------------------------------------------------------------------------------------------------''')

#Creating Tables for Bookstore
                mycursor.execute('create table if not exists Available_Books(BookName varchar(20) primary key, Genre varchar(20), Quantity int(10), Author varchar(20), Publication varchar(20), Price int(10))')
                mycursor.execute('create table if not exists Sale_Records(CustomerName varchar(20), PhoneNo char(10), BookName varchar(20), Quantity int(10), SalePrice int(10), SaleDate date, foreign key(BookName) references Available_Books(BookName))')
                mycursor.execute('create table if not exists Staff_Details(Name varchar(20), Gender varchar(10), Age int(5), PhoneNo char(10), Address varchar(50), DateAdded date)')
                mydb.commit()

#Menu
                while True:
                    print('''
-----------------------------------------
MENU

1: Add Books
2: Sell Books
3: Search Books
4: Staff Options
5: Sale Records
6: Available Books
7: Total Income after latest Reset
8: Help
9: Log Out
-----------------------------------------
''')

                    choice=input('Enter your choice - (1 to 9) : ')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Option 1 : For Adding Books
                    if choice=='1':
                        print('\n---ADDING BOOKS---\n')

                        print('*All the information below are mandatory to be filled*\n')

                        book=input('Enter Name of the book : ')
                        genre=input('Enter Genre of the book : ')
                        quantity=int(input('Enter Quantity of the book : '))
                        author=input('Enter name of the Author : ')
                        publication=input('Enter name of the Publication : ')
                        price=int(input('Enter Price of the book : '))

                        mycursor.execute("select * from Available_Books where BookName='"+book+"'")
                        c=mycursor.fetchone()   #c

                        if c is not None:
                            mycursor.execute("update Available_Books set Quantity=Quantity+'"+str(quantity)+"' where BookName='"+book+"'")
                            mydb.commit()

                            print('\nThe book is succesfully added to the database...!!!')

                        else:
                            mycursor.execute("insert into Available_Books values('"+book+"','"+genre+"','"+str(quantity)+"','"+author+"','"+publication+"','"+str(price)+"')")
                            mydb.commit()

                            print('\nThe book is added successfully to the database...!!!')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Option 2 : For Selling Books
                    elif choice=='2':
                        print('\n---SELLING BOOKS---\n')

                        mycursor.execute('select count(*) from Available_Books')
                        d=mycursor.fetchone()  #d

                        d1=max(d)  #d1

                        if d1 !=0:
                            
                            mycursor.execute('select * from Available_Books')
                            print('''Details of available books :
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
('BookName','Genre','Quantity','Author','Publication','Price')
''')
                            for i in mycursor:
                                print(i)
                            print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

                            customer=input('\nEnter name of the Customer : ')
                            phone=int(input('Enter Phone Number : '))
                            book=input('Enter Name of the book : ')
                            price=int(input('Enter Price of the book : '))
                            quantity1=int(input('Enter Quantity of the book : '))

                            mycursor.execute("select BookName from Available_Books where BookName='"+book+"'")
                            d2=mycursor.fetchone()   #d2

                            if d2 is not None:

                                mycursor.execute("select Quantity from Available_Books where BookName='"+book+"'")
                                d3=mycursor.fetchone()   #d3

                                if max(d3)<quantity1:
                                    print('\nThis book is not enough in quantity...!!!')

                                else:
                                    mycursor.execute("insert into Sale_Records values('"+customer+"','"+str(phone)+"','"+book+"','"+str(quantity1)+"','"+str(price)+"',curdate())")
                                    mydb.commit()
                                    mycursor.execute("update Available_Books set Quantity=Quantity-'"+str(quantity1)+"' where BookName='"+book+"'")
                                    mydb.commit()
                                    mycursor.execute("update Sale_Records set SalePrice='"+str(quantity1)+"'*'"+str(price)+"' where CustomerName='"+customer+"'")
                                    mydb.commit()

                                    print('\nThe book has been sold...!!!')

                            else:
                                print('\nThis book is not available...!!!')

                        else:
                            print('The database is empty. There are no books to sell...!!!')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Option 3 : Search books on the basis of given options
                    elif choice=='3':
                        
                        mycursor.execute('select count(*) from Available_Books')
                        e=mycursor.fetchone()  #e

                        e1=max(e)    #e1

                        if e1 !=0:
                            print('\n---SEARCHING BOOKS---')

                            while True:
                                print('''
-------------------------
Search Options :

1: By Name
2: By Genre
3: By Author
4: Back to Menu
-------------------------
''')

                                search=input('Enter your choice - (1 to 4) : ')

#By Name
                                if search=='1':
                                    print('\n---SEARCH ON THE BASIS OF NAME OF THE BOOK---\n')

                                    booksearch=input('Enter book name to search : ')

                                    mycursor.execute("select BookName from Available_Books where BookName='"+booksearch+"'")
                                    e2=mycursor.fetchone()   #e2

                                    if e2 is not None:
                                        print('\nThe book is in stock...!!!')

                                        mycursor.execute("select * from Available_Books where BookName='"+booksearch+"'")
                                        print('''Book details is given below :
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
('BookName','Genre','Quantity','Author','Publication','Price')
''')         
                                        for i in mycursor:                                                                          
                                            print(i)
                                        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

                                    else:
                                        print('\nBooks of this name are not available...!!!')

#By Genre
                                elif search=='2':
                                    print('\n---SEARCH ON THE BASIS OF GENRE---\n')

                                    genresearch=input('Enter genre to search : ')

                                    mycursor.execute("select count(Genre) from Available_Books where Genre='"+genresearch+"'")
                                    e3=mycursor.fetchone()  #e3

                                    e4=max(e3)  #e4

                                    if e4 !=0:
                                        print('\nThe book is in stock...!!!')

                                        mycursor.execute("select * from Available_Books where Genre='"+genresearch+"'")
                                        print('''Book details is given below :
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
(BookName','Genre','Quantity','Author','Publication','Price')
''')
                                        for i in mycursor:
                                            print(i)
                                        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

                                    else:
                                        print('\nBooks of this genre are not available...!!!')
                                        
#By Author's Name
                                elif search=='3':
                                    print('\n---SEARCH ON THE BASIS OF AUTHOR\'S NAME---\n')

                                    authorsearch=input('Enter author\'s name to search : ')

                                    mycursor.execute("select count(Author) from Available_Books where Author='"+authorsearch+"'")
                                    e5=mycursor.fetchone()   #e5

                                    e6=max(e5)   #e6

                                    if e6 !=0:
                                        print('\nThe book is in stock...!!!')

                                        mycursor.execute("select * from Available_Books where Author='"+authorsearch+"'")
                                        print('''Book details are given below :
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
('BookName','Genre','Quantity','Author','Publication','Price')
''')
                                        for i in mycursor:
                                            print(i)
                                        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

                                    else:
                                        print('\nBooks of this author are not available...!!!')

                                elif search=='4':
                                    break

                                else:
                                    print('\nERROR! Invalid input...!!!')
                                    pass

                        else:
                            print('\nThe database is empty. There are no books to search...!!!')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#option 4 : Staff Options
                    elif choice=='4':

                        while True:
                            
                            print('''
---STAFF OPTIONS---
-----------------------------------
What do you want to do...???

1: New Staff Entry
2: Remove Staff
3: Existing Staff Details
4: Back to Menu
-----------------------------------
''')

                            staffchoice=input('Enter your choice - (1 to 4) : ')
                      
#For New Staff Entry
                            if staffchoice=='1':
                                print('\n---FOR NEW STAFF ENTRY---\n')

                                name=input('Enter full name of the staff member : ')
                                gender=input('Enter gender - (F/M/O) : ')
                                age=int(input('Enter age : '))
                                phone=int(input('Enter phone number : '))
                                address=input('Enter full address : ')

                                mycursor.execute("insert into Staff_Details values('"+name+"','"+gender+"','"+str(age)+"','"+str(phone)+"','"+address+"', curdate())")
                                mydb.commit()
                                print('\nThis staff member is added successfully...!!!')

#For Deleting Staff
                            elif staffchoice=='2':
                                
                                mycursor.execute('select count(*) from Staff_Details')
                                f=mycursor.fetchone()  #f

                                f1=max(f)  #f1

                                if f1 !=0:
                                    print('\n---FOR DELETING STAFF---')

                                    mycursor.execute('select * from Staff_Details')
                                    print('''
Existing staff details is given below :
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
('Name','Gender','Age','PhoneNo','Address','DateAdded')
''')
                                    for i in mycursor:
                                        print(i)
                                    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

                                    name=input('\nEnter name of the staff member to remove : ')

                                    mycursor.execute("select Name from Staff_Details where Name='"+name+"'")
                                    f2=mycursor.fetchone()  #f2

                                    if f2 is not None:
                                        mycursor.execute("delete from Staff_Details where Name='"+name+"'")
                                        mydb.commit()
                                        print('\nThis staff member is removed succesfully...!!!')

                                    else:
                                        print('\nThis staff member does not exists...!!!')

                                else:
                                    print('\nNo staff exists...!!!')


#Existing Staff Details
                            elif staffchoice=='3':

                                mycursor.execute('select count(*) from Staff_Details')
                                f3=mycursor.fetchone()   #f3

                                f4=max(f3)   #f4

                                if f4 !=0:
                                    print('\n---FOR EXISTING STAFF DETAILS---')
                                    
                                    mycursor.execute('select * from Staff_Details')
                                    print('''
Existing staff details is given below :
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
('Name','Gender','Age','PhoneNo','Address','DateAdded')
''')
                                    for i in mycursor:
                                        print(i)
                                    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

                                else:
                                    print('\nNo staff exists...!!!')

                            elif staffchoice=='4':
                                break

                            else:
                                print('\nERROR! Invalid input...!!!')
                                pass
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Option 5 : Sale Records
                    elif choice=='5':

                        while True:
                            
                            print('''
---SALE RECORDS---
-----------------------------------
What do you want to do ...???

1: Sale history details
2: Reset sale history
3: Back to Menu
-----------------------------------
''')

                            salechoice=input('Enter your choice -(1 or 3) : ')

#Sale History Details
                            if salechoice=='1':

                                mycursor.execute('select count(*) from Sale_Records')
                                g=mycursor.fetchone()   #g

                                g1=max(g)   #g1

                                if g1 !=0:
                                    mycursor.execute('select * from Sale_Records')
                                    print('\n---SALE HISTORY DETAILS---')
                                    print('''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
('CustomerName','PhoneNo','BookName','Quantity','Price','SaleDate')
''')
                                    for i in mycursor:
                                        print(i)
                                    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

                                else:
                                    print('\nSale history is empty...!!!')

#Reset Sale History
                            elif salechoice=='2':

                                mycursor.execute('select count(*) from Sale_Records')
                                g2=mycursor.fetchone()  #g2

                                g3=max(g2)    #g3

                                if g3 !=0:
                                    
                                    while True:
                                        
                                        print('''
***WARNING***
Are you sure you want to reset Sale History...???
If yes, sale history will be permanently deleted...!!!
''')

                                        warning=input('Enter Yes/No : ')

                                        warning=warning.capitalize()

                                        if warning=='Yes':
                                            
                                            mycursor.execute('delete from Sale_Records')
                                            mydb.commit()
                                            print('\nSale history has been reset...!!!')
                                            break

                                        elif warning=='No':
                                            break

                                        else:
                                            print('\nERROR! Invalid input...!!!')
                                            break

                                else:
                                    print('\nSale history is already empty/reset...!!!')

                            elif salechoice=='3':
                                break

                            else:
                                print('\nERROR! Invalid input...!!!')
                                pass
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Option 6 : Available Books Details
                    elif choice=='6':
                        
                        mycursor.execute('select count(*) from Available_Books')
                        h=mycursor.fetchone()   #h

                        h1=max(h)   #h1

                        if h1 !=0:
                            mycursor.execute('select * from Available_Books order by Bookname')
                            print('\n---DETAILS OF AVAILABLE BOOKS---')
                            print('''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
('BookName','Genre','Quantity','Author','Publication','Price')
''')
                            for i in mycursor:
                                print(i)
                            print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

                        else:
                            print('\nThere are no books in the database...!!!')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Option 7 : Total Income After Latest Reset
                    elif choice=='7':
                        print('\n---TOTAL INCOME---\n')

                        mycursor.execute('select sum(SalePrice) from Sale_Records')
                        j=mycursor.fetchone()   #j

                        j1=max(j)   #j1

                        if j1 is not None:
                            print('Total income in Rupees : Rs',j1)

                        else:
                            print('Total income in Rupees : Rs 0')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Option 8 : For help
                    elif choice=='8':
                        print('''
---HELP---

1. This is the Menu, where you can perform many tasks.
2. In Option 1, you can add books to the database.
3. In Option 2, you can sell books and record sale history.
4. In Option 3, you can search books according to your choices/requirements.
5. In Option 4, you can add/remove staff members, and can view existing staff details according to your choices/requirements.
6. In Option 5, you can view/reset sale history.
7. In Option 6, you can view the details of available books.
8. In Option 7, you can view total income.
9. In Option 8, you can get help, if you facing any trouble.
10. In Option 9, you can log out of the menu.

Hope this helps...!!!
''')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
#Option 9 : For log out
                    elif choice=='9':
                        print('\nYou have successfully logged out...!!!\n')
                        break

                    else:
                        print('\nERROR! Invalid input...!!!')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Login else part
            else:
                print('Incorrect Password...!!!')

        else:
            print('Invalid Username...!!!')

#Help (on home page)
    elif a=='3':
        print('''
---HELP---

1. Sign Up and Login enhances your data privacy.
2. For Sign Up, create a new username and password of your own.
3. Make your passwords strong and private. *DON'T SHARE YOUR PASSWORDS WITH ANYONE*
4. For Login, enter the correct username and password you have created when you signed up.
5. You will not be able to login if you have not signed up once.
6. You don't need to sign up everytime you login.
7. After successful login, you will be able to procees further.
8. To exit, enter 4.

Hope this helps...!!!
''')

#Exit
    elif a=='4':
        print('\nYou have exited ABC Bookstore...!!!')
        print('Thank You...!!!')
        break

    else:
        print('\nERROR! Invalid input...!!!')
