import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    
    def createAccount(self):
        self.accNo= int(input("\tEnter the New Accounter number : "))
        self.name = input("\tEnter the New Accounter holder name : ")
        self.deposit = int(input("\tEnter The Deposit amount : "))
        print("\n\t\t\t Account Created Successfully...")
    
    def showAccount(self):
        print("Accounter Number : ",self.accNo)
        print("Accounter Holder Name : ", self.name)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("\tAccount Number : ",self.accNo)
        self.name = input("\tModify Accounter Holder Name : ")
        self.deposit = int(input("\tModify Balance : "))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    
    def getAcccountHolderName(self):
        return self.name
    
    def getDeposit(self):
        return self.deposit
    
def intro():
    print("\t\t\t\t\t\t\t WELCOME TO BANKING PROCESS !!!")
    print()
    print("\t\t\t\t\t\t\t ---------------------")
    print("\t\t\t\t\t\t\t SELVARAJ MINI PROJECT")
    print("\t\t\t\t\t\t\t ---------------------")
    print()
    print("\t\t\t\t\t\t\t =======================================")
    print("\t\t\t\t\t\t\t PROJECT NAME : BANK MANAGEMENT SYSTEM")
    print("\t\t\t\t\t\t\t =======================================")
    print()
    print("\t\t\t\t\t\t\t BANKING NAME : indian overseas bank")


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print()
            print("\t","ACCOUNT NUMBER","                   ","ACCOUNT NAME","                              ","ACCOUNT BALANCE")
            print("\t=========================================================================================================")
            print("\t",item.accNo,     "                    ","\t"," ",item.name,"                             ","\t",item.deposit  )
            print("\t=========================================================================================================")
        infile.close()
        
def displayEnquiry(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print()
                print("\tYour name is = ",item.name)
                print()
                print("\tYour account Balance is = ",item.deposit)
                found = True
    if not found :
        print("\n")
        print("\tThis Account number Not Created..Pls Enter Correct Account Number !!!")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    print()
                    amount = int(input("\tEnter the amount to deposit : "))
                    item.deposit += amount
                    print()
                    print("\tDeposited Amount Successfully")
                    print()
                    print("\t\t\tYour Balance is Updted")
                   
                elif num2 == 2 :
                    print()
                    amount = int(input("\tEnter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                        print()
                        print("\tWithdrawal Amount Successfully")
                        print()
                        print("\t\t\tYour Balance is Updated")
                    else :
                        print()
                        print("\t\t\tYour Balance Insufficent")
                
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        print("\n\t\t\tAccount Deleted Successfully...")
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                print()
                item.name = input("\tEnter the Modified account holder name : ")
                print()
                item.deposit = int(input("\tEnter the Modified Amount : "))
                print("\n\t\t\tAccounter details Modified Successfully...")
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
    

            
# whole program running area...

ch=7
num=0
intro()
print("\n")

while ch != 8:
    print()
    print("\t MAIN MENU")
    print("\t============")
    print()
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. DELETE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print()
    print("\t\t\t\t (Select Your Option 1 to 8)")
    print("\t\t\t\t ===========================")
    print()
    choice=input("\tEnter Options : ")
    
    if choice == '1':
        writeAccount()
        
    elif choice =='2':
        print()
        num = int(input("\tEnter The Accounter number : "))
        depositAndWithdraw(num, 1)
        
    elif choice == '3':
        print()
        num = int(input("\tEnter The Accounter number : "))
        depositAndWithdraw(num, 2)
        
    elif choice == '4':
        print()
        num = int(input("\tEnter The Accounter number : "))
        displayEnquiry(num)
        
    elif choice == '5':
        displayAll();
        
    elif choice == '6':
        print()
        num =int(input("\tEnter The Accounter number : "))
        deleteAccount(num)
        
    elif choice == '7':
        print()
        num = int(input("\tEnter The Accounter number : "))
        modifyAccount(num)
        
    elif choice == '8':
        print()
        print("\t\t\t\t\t\t\t\t Your choice is Exit...Thank you !!!")
        break
    
    else :
        print()
        print("\t(Invalid choice)")
