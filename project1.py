'''num=int(input("enter a number :"))
s=0
bkp=num
while num>0:
    t=num%10
    s=10*s+t
    num=num//10
print(s)
if s==bkp:
    print("pallendrome number")
else:
    print("not pallendrome number")'''

'''x=[1,2,3,4,5,6,7,8]
chunk_size=2
chunk=[]
for i in range (0,len(x),chunk_size):
    chunk.append(x[i:i+chunk_size])
print(chunk)'''

'''
num=int(input("enter a number :"))
while True:
    s=0
    while num>0:
        t=num%10
        s=s+t
        num=num//10
    if s>9:
        num=s
    else:
        print(s)
        break
'''
'''
s="python"
def reversestring(st):
    output=""
    for ch in st:
        output=ch+output
    return output
res=reversestring(s)
print(res)

#perfect number 
num=6
def perfect(n):
  s=0
  d=1
  while d<=num//2:
    if num%d==0:
        s=s+d
    d=d+1
  if num==s:
    return True
  else:
    return False
perfect(num)

x=["raju","rajukumar","rajguna"]
m_str=x[0]
for s in x:
    if len(s)<len(m_str):
        m_str=s
for i in range(len(m_str),0,-1):
    found=True
    for s in x:
        if m_str[:i] not in s:
            found=False
    if found==True:
            print(m_str[:i])
            break'''
'''
s="welcome to python"
def upperstring(st):
    output=""
    for ch in range(0,len(st)):
        a_code=ord(len[st])
        if a_code>=97 and a_code<=122:
            output=output+chr(a_code-32)
        else:
            output=output+ch
        return output
res=upperstring(s)
print(res)'''
'''
x={10,20,40,"vcube","python",True}
y={50,60,70,"java",1}
#output=x|y # union
#output=x&y #intersection
#output=x-y #difference
output=x^y #semitric difference
print(output)'''
'''
#anagram
x=set(input("enter a string :"))
y=set(input("enter another :"))
if len(x^y)==0:
    print("anagram")
else:
    print("not anagram")'''
'''
#hetrogram
st=input("enter a string :")
if len(st)==len(set(st)):
    print("hetrogram")
else:
    print("not hetrogram")'''

'''
import time
x = [i for i in range(1,100000)]
start=time.time
y=99999999999999999999
output=y in x
print(output)
end=time.time
print("time taken",end-start)'''
'''
s={1,2,3,4,5,6}
res=s.pop()
print(res)
'''
'''
x={10,20,30,"vcube",True}
y={40,50,"python",1}
x.update(y)
print(x)
print(y)'''
'''num=12345
s=0
while num>0:
    t=num%10
    s=s+t
    num=num//10
    if s>9:
        s=num
else:
    print(s)

num=int(input("enetr a number :"))
while num<=1000:
    d=2
    while d%num//2:
        if num%d==0:
            break
        d=d+1
    else:
        print(num)
    num=num+1'''
'''
num=int(input("enter a number :"))
d=1
cnt=0
while d<=num:
    if num%d==0:
       cnt=cnt+1
    d=d+1
if cnt==2:
     print("prime")
else:
    print("not prime")'''

'''
num=int(input("enter a number : "))
a=0
b=1
print(a,b)
i=1
while i<=num:
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1'''
'''
def isprime(num,d=2):
    if num%d==0:
        return False
    elif d<=num//2:
        return isprime(num,d+1)
    else:
        return True
res=isprime(11)
print(res)'''

'''
def sumofn(num):
    if num==1:
        return 1
    return num+sumofn(num-1)
res=sumofn(5)
print(res)
'''
'''
def splitfun(fun):
    def innerfun1():
        output=fun()
        return output.split()
    return innerfun1
def upper(fun):
    def innerfun():
        output=fun()
        return output.upper()
    return innerfun
@splitfun
@upper
def display():
    s="python is fun"
    return s
res=display()
print(res)'''

'''
s="python is good"

def revresefun(st):
    output=""
    for ch in st:
        output=ch+output
    return output
res=revresefun(s)
print(res)'''

'''
s="python is fun"

def upperfun(st):
    output=""
    for ch in st:
        a_code=ord(ch)
        if a_code>=97 and a_code<=122:
            output=output+chr(a_code-32)
        else:
            output=output+ch
    return output
res=upperfun(s)
print(res)'''
'''
num=153
s=0
while num>0:
    t=num%10
    s=s+t
    num=num//10
if s>9:
    num=s
else:
    print(s)'''
'''
class Student:
    institute="vcube"
    fees=[]
    def __init__(self,n,a,m1,m2,f):
        self.name=n
        self.age=a
        self.maths=m1
        self.english=m2
        Student.fees.append(f)
    def info(self):
        print(self.name,self.age)
    def isyoung(self):
        if self.age>30:
            return False
        else:
            return True
    def average(self):
        return(self.english+self.maths)/2
    def grade(self):
        grd=self.average()
        if grd>70:
            grade="A"
        elif grd>60:
            grade="B"
        else:
            grade="C"
        msg=(f"{self.name} is securd {grade}")
        return msg
    @classmethod
    def revanue(cls):
        amt=0
        for i in cls.fees:
            amt=amt+i
        msg=(f"{cls.institute} is generated {amt}")
        return msg


    
s1=Student("tej",23,76,56,45000)
s2=Student("him",34,78,89,50000)
s3=Student("raj",32,80,79,48000)
res=s1.average()
print(res)
print(s2.info)
print(s1.institute)
print(Student.fees)
print(Student.revanue())'''
'''        
x=[1,2,3,4,5,6]
#res=list(map(lambda a:a**2,x))
#res=list(filter(lambda a:a%2==0,x))
from functools import reduce
res=reduce(lambda a,b:a*b,x)
print(res)'''
'''
class Student:
    institute="vcube"
    std_fees=[]
    def __init__(self,n,a,m1,m2,f):
        self.name=n
        self.age=a
        self.maths_marks=m1
        self.english_marks=m2
        Student.std_fees=f
    def info(self):
        print(self.name,self.age)
    def total(self):
        return(self.english_marks+self.maths_marks)
    def average(self):
        grd=self.total()
        if grd>70:
            grade="A"
        else:
            grade="B"
        msg=f"{self.name} secured is {grade}"
        return msg
    @classmethod
    def revanue(cls):
        amt=0
        for i in cls.std_fees:
            amt=amt+i
        msg=f"{cls.institute} total revanue is  {amt}"
        return msg
    @classmethod
    def getstudent(cls,sinfo):
        n,a,m1,m2,f=sinfo.split(",")
        obj=Student(n,int(a),int(m1),int(m2),int(f))
        return obj
student=[
    "raj,32,78,99,45000",
    "him,23,67,89,46000",
    "tej,33,78,79,45600",
    "frank,27,67,60,44000",
     "raj,32,78,99,45000",
    "him,23,67,89,46000",
    "tej,33,78,79,45600",
    "frank,27,67,60,44000"
]
list_obj=[]
for st in student:
    obj=Student.getstudent(st)
    list_obj.append(obj)
for obj in list_obj:
    obj.info()'''
'''
class A:
    institute="vcube"
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a,self.b)
        print("this is A class")
class B(A):
    def __init__(self,e,f):
        super().__init__(e,f)
    def display(self):
        print("this is display")
        super().display()
    def show(self):
        print(self.a,self.b)
obj=B(10,20) 
obj.display()  
obj.show()    
print(A.institute)
B.institute="zcube"
print(B.institute)'''
'''
class BankAccount:
    def __init__(self,initial_amount):
        self.amount=initial_amount
    def deposite(self,amount):
        if amount>0:
            self.amount=amount+self.amount
            print(f"you deposite amount is {amount} and your current balance is {self.amount}")
        else:
            print("enter a positive amount to deposite")
    def withdraw(self,amount):
        if amount>0:7
            if amount<=self.amount:
                self.amount=self.amount-amount
                print(f"you withdraw amount is {amount} and your current balance is {self.amount}")
            else:
                print("amount is insuffient to withdraw")
        else:
            print("enter positive amount to withdraw")
    def checkbalance(self):
        print(f"your current balance in your account is {self.amount}")
        return self.amount
p1=BankAccount(3000)
p1.deposite(1000)
p1.withdraw(2000)
p1.checkbalance()'''

'''
def function(fun):
    def innerfun(s):
        output=fun(s)
        total=sum(ord(ch) for ch in output)
        return total
    return innerfun
@function
def display(s):
    return s
res=display("abcd")
print(res)'''

'''
class BankAccount:
    def __init__(self,initial_amount):
        self.amount=initial_amount
    def deposite(self,amount):
        if amount>0:
            self.amount=self.amount+amount
            print(f"{amount} is deposite and total amount is {self.amount} ")
        else:
            print("enter a positive amount")
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.amount:
                self.amount=self.amount-amount
            else:
                print("insuffient amount")
        else:
            print("enter positive amount")
    def checkbalance(self):
        print(f"your currentbalance is {self.amount}")
        return self.amount
obj=BankAccount(5000)
obj.checkbalance()
obj.withdraw(1000)
obj.deposite(500)
obj.checkbalance()  '''
'''
num=int(input("enter a number : "))
d=2
while d<=num//2:
    if num%d==0:
        print("not prime")
        break
    d=d+1
else:
    print("prime")'''
'''
n1=int(input("enetr a number :"))
n2=int(input("enetr a number : "))
if n1<n2:
    small=n1
else:
    small=n2
d=small
while d>=2:
    if n1%d==0 and n2%d==0:
        print(d)
        break
    d=d-1
    #
d=2
while d<=small:
    if n1%d==0 and n2%d==0:
        print(d)
        break
    d=d+1'''
'''
num=153
small=9
while num>0:
    t=num%10
    if t<small:
        small=t
    num=num//10
print(small)'''

'''
num=197
d=2
while d<=num//2:
    if num%d==0:
        print("not prime")
        break
    d=d+1
else:
    print("prime")
while True:
    bkp=num
    s=0
    while num>0:
        t=num%10
        s=s+t
        num=num//10
    print(s)
    num=bkp
    if s>9:
        num=s
    else:
        print(s)
        break'''
'''
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
a=set(list1)
b=set(list2)
res=a.union(b)
res1=a.intersection(b)
union=list(res)
intersetion=list(res1)
print(union)
print(intersetion)'''

'''
class Camera:
    def take_photo(self):
        print("take photo")
class Phone:
    def make_call(self):
        print("make call")
class Smart_phone(Camera,Phone):
    def browse_internet(self):
        print("browse internet")
obj=Smart_phone()
obj.make_call()
obj.take_photo()
obj.browse_internet()'''

'''
class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
    def display(self):
        super().display()
        print(self.salary)
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        super().display()
        print(self.department)
obj=Manager("raj",250000,"dip")
obj1=Employee("hima",45000)
obj1.display()'''
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def display(self):
        super().display()
        print(self.rollno)
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age) 
        self.subject=subject
    def display(self):
        super().display()
        print(self.subject)
a=Person("hima",23)
b=Student("tej",24,456)
c=Teacher("srinu",36,"maths")
list_obj=[a,b,c]
for i in list_obj:
    i.display()'''

'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def display(self):
        super().display()
        print(self.rollno)
obj=Student("raj",24,45)
obj.display()'''
'''
class Parent:
    def display(self):
        print("this is parent class display")
class Child(Parent):
    def display(self):
        super().display()
        print("this is child class display")
obj=Child()
obj.display()
'''
'''
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        print(self.a+self.b)
    def subtraction(self):
        print(self.a-self.b)
    def multiplication(self):
        print(self.a*self.b)
    def divison(self):
        print(self.a/self.b)
obj=Calculator(10,20)
obj.subtraction()
obj.multiplication()'''

'''
class BankAccount:
    def __init__(self,initial_amount):
        self.initial_amount=initial_amount
    def deposite(self,amount):
        if amount>0:
            self.initial_amount=self.initial_amount+amount
            print(f"you deposite in your account is {self.initial_amount}")
        else:
            print("enter positive amount to deposite")
    def withdraw(self,amount):
        if amount>0:
            if self.initial_amount>=amount:
                self.initial_amount=self.initial_amount-amount
                print(f"you withdraw from your bank account amount is  {self.initial_amount}")
            else:
                print("insuffient balance")
        else:
            print("enter positive number to withdraw")
    def checking(self):
        print(f"your current balance in your account is {self.initial_amount}")
        return self.initial_amount
c1=BankAccount(1000)
c1.deposite(1000)
c1.withdraw(500)
c1.checking()
'''
'''
class Calculator:
    def __init__(self,num):
        self.num=num
    def info(self):
        print(self.num)
    def __add__(self,other):
        obj=int(self.num+other.num)
        return obj
c1=Calculator(10)
c2=Calculator(20)
c3=c1+c2
print(c3)
'''
'''
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def info(self):
        print(self.name,self.age,self.marks)
    def __eq__(self, value):
        if (self.name==value.name) and (self.age==value.age) and (self.marks==value.marks):
            return True
        else:
            return False
s1=Student("raj",24,45)
s2=Student("raj",24,45)
if s1==s2:
    print("both are same")
else:
    print("both are not same")'''

'''
class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def display(self):
        print(self.__name,self.__marks)
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,m):
        if m>0 and m<100:
            self.__marks=m
            return m          
obj=Student("teja",89)
obj.display()
obj.marks=68
obj.display()'''
'''
#pip install mysql-connector-Python
import mysql.connector as db
cor=db.connect(local="root",password="u682389",host="local host",database="schema")
cur=cor.cursor()
insert_sql=
insert into employee values(%s,%s,%s,%s,%s,%s)
data=["teja",23,120000,"testing","male",1]
cur.excute(insert_sql,data)
cur.close()
cor.close()'''

'''
import mysql.connector as db
con=db.connect(user="root",password="7330870063",host="localhost",database="MySQL80")
cur=con.cursor()
insert_sql=
insert into employee values(%s,%s,%s,%s)
data=[6,"ranga",168000,"tirupati"]
cur.execute(insert_sql,data)
cur.close()
con.close()'''

'''
fobj=open("D://vcube.txt","w")
if fobj.writable:
    fobj.write("they are good")
fobj.close()'''

'''
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="bank_db"
    )

def create_account(acc_no, name, balance):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO accounts VALUES (%s, %s, %s)"
    cursor.execute(query, (acc_no, name, balance))
    db.commit()
    print("Account created.")
    db.close()

def deposit(acc_no, amount):
    db = connect_db()
    cursor = db.cursor()
    query = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
    cursor.execute(query, (amount, acc_no))
    db.commit()
    print(f"Deposited ₹{amount} into {acc_no}.")
    db.close()

def withdraw(acc_no, amount):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT balance FROM accounts WHERE account_number = %s"
    cursor.execute(query, (acc_no,))
    balance = cursor.fetchone()[0]
    if balance >= amount:
        query = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
        cursor.execute(query, (amount, acc_no))
        db.commit()
        print(f"Withdrew ₹{amount} from {acc_no}.")
    else:
        print("Insufficient balance.")
    db.close()

def check_balance(acc_no):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT balance FROM accounts WHERE account_number = %s"
    cursor.execute(query, (acc_no,))
    result = cursor.fetchone()
    if result:
        print(f"Balance for {acc_no}: ₹{result[0]}")
    else:
        print("Account not found.")
    db.close()

def main():
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Balance\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            acc_no = int(input("Account number: "))
            name = input("Name: ")
            bal = float(input("Initial balance: "))
            create_account(acc_no, name, bal)
        elif choice == '2':
            acc_no = int(input("Account number: "))
            amt = float(input("Deposit amount: "))
            deposit(acc_no, amt)
        elif choice == '3':
            acc_no = int(input("Account number: "))
            amt = float(input("Withdraw amount: "))
            withdraw(acc_no, amt)
        elif choice == '4':
            acc_no = int(input("Account number: "))
            check_balance(acc_no)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()'''

'''
import re
data=iam hima teja and am from tirupati i completed my graduation on btech in 2025 and my phone number is 6302562033 and +9173308700 and email is himatejahima032@gamil.com
#res=re.findall('\d',data)
#res=re.findall("\w",data)
#res=re.findall("[a-z]+",data)
#res=re.findall("[a-z 1-9]+",data)
#res=re.findall("[+91]*[0-9]{10}",data)
#res=re.findall("[a-z]+[0-9]+@[a-z]+\.com",data)b
#res=re.findall("[a-z]{.4}",data)
res=re.findall("n....r",data)
print(res)'''

'''
import re
data='vcube started on 21 june 2021 and it is succesfully running over 10000 students where join in it and it has 10 branchs in KBHP and the emil address is\
    vcube20@gmail.com and vcube204vcube@gmail.com and mobile number is 9898989898 and +919898989797 and it is succesfully runed'
#res=re.findall("\d",data)
#res=re.findall("[a-z]+[0-9]+[a-z]*@[a-z]+.com",data)
res=re.findall("[+91]*[0-9]{10}",data)
print(res)'''

'''
import mysql.connector as db
con=db.connect(user="root",password="7330870063",host="localhost",database="employee")

def createaccount(acc_no,name,balance):
    cur=con.cursor()
    quary='insert into account values(%s,%s,%s)'
    cur.execute(quary,(acc_no,name,balance))
    con.commit()
    print("Account successfully created")

def Deposite(acc_no,amount):
    cur=con.cursor()
    quary='update account set balance=balance+%s where acc_no=%s'
    cur.execute(quary,(amount,acc_no))
    con.commit()
    print(f"{amount} ruppes deposited in {acc_no}")

def withdraw(acc_no,amount):
    cur=con.cursor()
    quary='select balance from account where acc_no=%s'
    cur.execute(quary,(acc_no,))
    result=cur.fetchone()[0]
    if result>=amount:
        data='update account set balance=balance-%s where acc_no=%s'
        cur.execute(data,(amount,acc_no))
        con.commit()
        print(f"{amount} withdraw in {acc_no}")
    else:
        print("insufficent balance")
    cur.close()

def checkbalance(acc_no):
    cur=con.cursor()
    quary="SELECT balance FROM account WHERE acc_no = %s"
    cur.execute(quary,(acc_no,))
    result=cur.fetchone()
    if result:
        print(f"balance in {acc_no} is {result}")
    else:
        print("Account Not Found")
    con.close()

def main():
    while True:
        print("1.Create Account\n2.Deposite\n3.withdraw\n4.checkbalance\n5.exit")
        choice=int(input("enter your choice : "))
        if choice==1:
            acc_no=int(input("Account Number :"))
            name=input("Name :")
            balance=int(input("Balance :"))
            createaccount(acc_no,name,balance)
        elif choice==2:
            acc_no=int(input("Account No :"))
            balance=input("balance :")
            Deposite(acc_no,balance)
        elif choice==3:
            acc_no=(int(input("Account no :")))
            balance=int(input("balance :"))
            withdraw(acc_no,balance)
        elif choice==4:
            acc_no=int(input("Account Number :"))
            checkbalance(acc_no)
        elif choice==5:
            break
        else:
            print("Enter Invalid choice")
            
if __name__=="__main__":
    main()'''
'''
num=int(input("enter a number : "))
s=0
bkp=num
while num>0:
    t=num%10
    s=s*10+t
    num=num//10
if bkp==s:
    print("pallendrome")
else:
    print("not pallendrome")'''
'''
class Rectangle:
    def __init__(self,length,breath):
        self.len=length
        self.breath=breath
    def Area(self):
        print("AREA = ",self.len * self.breath,"square units")
    def Perimeter(self):
        print("PERIMETER = ",2*(self.len + self.breath),"units")
obj=Rectangle(5,3)
obj.Area()
obj.Perimeter()'''

'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Person name is {self.name} and the age is {self.age}")
obj=Person("hima",24)
obj.display()'''
'''
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def Addition(self):
        print(self.num1+self.num2)
    def Subtraction(self):
        print(self.num1-self.num2)
    def Multiplication(self):
        print(self.num1*self.num2)
    def Divison(self):
        print(self.num1/self.num2)
obj=Calculator(10,20)
obj.Addition()
obj.Subtraction()
obj.Multiplication()
obj.Divison()'''
'''
class Student:
    def __init__(self,name,rollno,m1,m2,m3):
        self.name=name
        self.rollno=rollno
        self.english=m1
        self.maths=m2
        self.social=m3
    def Average(self):
        print("AVERAGE MARKS ARE ",(self.english+self.maths+self.social)/3)
    def display(self):
        print(f"student name is {self.name} and rollno is {self.rollno}")
obj=Student("hima",45,80,85,79)
obj.display()
obj.Average()'''

'''
class BankAccount:
    def __init__(self,initial_amount):
        self.initial_amount=initial_amount
    def deposite(self,amount):
        if amount>0:
            self.initial_amount=self.initial_amount+amount
            print(f"you deposite amount is {amount}")
        else:
            print("enter positive amount to deposite")
    def withdrawal(self,amount):
        if amount>0:
            if self.initial_amount>=amount:
                self.initial_amount=self.initial_amount-amount
                print(f"you withdraw amount is {amount}")
            else:
                print("insuffient amount")
        else:
            print("enter positive amount to withdraw")
    def checking_amount(self):
        print(f"remaining amount in your account is {self.initial_amount}")
        return self.initial_amount
c1=BankAccount(2000)
c1.deposite(1000)
c1.withdrawal(2000)
c1.checking_amount()'''
'''
class Book:
    def __init__(self,title,author,publisher):
        self.title=title
        self.author=author
        self.publisher=publisher
    def display(self):
        print(f"the book title is {self.title}")
        print(f"the book author is {self.author}")
        print(f"the book publisher is {self.publisher}")
obj=Book("harrypotter","cris","2010")
obj.display()'''

'''
class Car:
    def __init__(self,make,model,current_speed):
        self.make=make
        self.model=model
        self.current_speed=current_speed
    def Accelarate(self,speed):
        self.current_speed=self.current_speed+speed
        print(f" the {self.make} {self.model} accelarate speed is {self.current_speed}")
    def Brake(self,speed):
        if self.current_speed>=0:
            self.current_speed=self.current_speed-speed
            print(f"the {self.make} {self.model} brake speed is {self.current_speed}")
        else:
            print(f"the {self.make} {self.model} has come to stop")
            self.current_speed=0
    def get_speed(self):
        return f" {self.current_speed},{self.model},{self.make}"
obj=Car("bmw","m5",0)
print(obj.get_speed())
obj.Accelarate(50)
obj.Brake(20)'''
'''
class Vechile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def type_of_vechile(self):
        print("this is vechile")
class Car(Vechile):
    def __init__(self,brand,model):
        super().__init__(brand,model)
    def type_of_vechile(self):
        print(self.brand,self.model)
class Bike(Vechile):
    def __init__(self,brand,model):
        super().__init__(brand,model)
    def type_of_vechile(self):
        print(self.brand,self.model)
obj=Car("bmw","m5")
obj.type_of_vechile()
obj1=Bike("kawasaki","s1000rr")
obj1.type_of_vechile()
'''
def greet(a,b):
    return a+b
obj=greet(10,20)
#print(obj)
print(obj)
obj()