
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
    print(f"{amount} ruppes deposited in {acc_no} account")

def withdraw(acc_no,amount):
    cur=con.cursor()
    quary='select balance from account where acc_no=%s'
    cur.execute(quary,(acc_no,))
    result=cur.fetchone()[0]
    if result>=amount:
        data='update account set balance=balance-%s where acc_no=%s'
        cur.execute(data,(amount,acc_no))
        con.commit()
        print(f"{amount} amount withdraw in {acc_no} number")
    else:
        print("insufficent balance")
    cur.close()

def checkbalance(acc_no):
    cur=con.cursor()
    quary="SELECT balance FROM account WHERE acc_no = %s"
    cur.execute(quary,(acc_no,))
    result=cur.fetchone()
    if result:
        print(f"balance in {acc_no} account is {result} ruppes")
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
            checkbalance(acc_no,)
        elif choice==5:
            break
        else:
            print("Enter Invalid choice")
            
if __name__=="__main__":
    main()

print("comment")