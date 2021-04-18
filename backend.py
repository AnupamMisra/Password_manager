import MySQLdb
import pyperclip as pc
import random   
import hashlib
import time
import pandas as pd

hostName = 'remotemysql.com'      # place your own credentials here
userName = 'UDReedbczU'           # place your own credentials here
passWord = 'EzCB9vazqz'           # place your own credentials here
dbName =  userName                # place your own credentials here
DBConn= MySQLdb.connect(hostName,userName,passWord,dbName)

user=hashlib.sha224("anupam".encode()).hexdigest()
pw=hashlib.sha224("Raichu".encode()).hexdigest()

def check_pwd(pwdd):
    pwd = r("SELECT pwd from Password").iloc[0,0]
    pwd_hash=hashlib.sha224(pwd.encode()).hexdigest()

    if (pwd_hash==hashlib.sha224(pwdd.encode()).hexdigest()):
        return True
    else:
        return False  

def check_user(a,b):
    if (a==user):
        if (b==pw):
            return 1
    else: return 0
  
def s224(msg):
    return hashlib.sha224(msg.encode()).hexdigest()

def s512(msg):
    return hashlib.sha512(msg.encode()).hexdigest()

def s384(msg):
    return hashlib.sha384(msg.encode()).hexdigest()

def smd5(msg):
    return hashlib.md5(msg.encode()).hexdigest()

def ssha1(msg):
    return hashlib.sha1(msg.encode()).hexdigest()

def s256(msg):
    return hashlib.sha256(msg.encode()).hexdigest()

def shak_128(msg):  
    return hashlib.shake_128(msg.encode()).hexdigest()

def blak_2s(msg):
    return hashlib.blake2s(msg.encode()).hexdigest()

def blak_2b(msg):
    return hashlib.blake2b(msg.encode()).hexdigest()

def s3_384(msg):
    return hashlib.sha3_384(msg.encode()).hexdigest()

def s3_512(msg):
    return hashlib.sha3_512(msg.encode()).hexdigest()

def s3_256(msg):
    return hashlib.sha3_256(msg.encode()).hexdigest()

def s3_224(msg):
    return hashlib.sha3_224(msg.encode()).hexdigest()

def shak_256(msg):
    return hashlib.shake_256(msg.encode()).hexdigest()    

def runCMD (DDL):
    DBConn= MySQLdb.connect(hostName,userName,passWord,dbName)
    myCursor = DBConn.cursor()
    retcode = myCursor.execute(DDL) 
    print (retcode)
    DBConn.commit()
    DBConn.close()

def runSELECT (CMD):
    DBConn= MySQLdb.connect(hostName,userName,passWord,dbName)
    df_mysql = pd.read_sql(CMD, con=DBConn)    
    DBConn.close()
    return df_mysql

def r(msg):
    if msg[0:6]=="SELECT" or msg[0:6]=="select":
        return runSELECT(msg)
    else:
        runCMD(msg)


'''
r("DROP TABLE IF EXISTS Storage")
r("CREATE TABLE Storage( \
website varchar(70) not null, \
url varchar(70) not null primary key, \
user_id varchar(70) not null, \
password varchar(70) not null)")
'''

'''
r("DROP TABLE IF EXISTS Counter")
r("CREATE TABLE Counter(ctr INT not null)")
r("INSERT INTO Counter(ctr) VALUES(1)")
'''
'''
r("DROP TABLE IF EXISTS Password")
r("CREATE TABLE Password(pwd varchar(50) not null)")
r('INSERT INTO Password(pwd) VALUES("Pikachu")')
'''

pwd = ""
gospel=hashlib.sha224("okay".encode()).hexdigest()

def funcz(func,param):
    return func(param)

def randomalpha():
    return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")    

def hash(pp):
    
    d = {1:'s224', 2:'s512', 3:'s384',4:'smd5', 5:'ssha1', 6:'s3_256', 7:'blak_2s', 8:'blak_2b', 9:'s3_384', 10:'s3_512', 11:'s256', 12:'s3_224'}


    ct = int(r(f'SELECT ctr from Counter').iloc[0,0])  #count of hashing algo
    p=funcz(eval(d[ct]),pp) #Sends to appropriate hashing algo and gets the hashed code

    if ct==12:
        ct=1
    else:
        ct=ct+1    

    r(f'UPDATE Counter SET ctr={ct}') #So that the next algorithm is used the next time
    _ =randomalpha()
    passp = p[0:14] + _ + "*" + p[15:29] #returns hashed value
    return passp

def insert_pass(website,url,user_id,choice,*v):
    try:
        if (r(f'select user_id from Storage where website="{website}"').iloc[0,0]!=""):   
            print("Stop, it already exists")

    except:

        #generate new pass
        #2 random no.s
        if choice==1:
            z=hash(*v)
        elif choice==2:
            randomlist = []
            for i in range(0,10):
                n = str(random.randint(1,30))
                randomlist.append(n)
            passx=int("".join(randomlist))
            z=hash(str(passx))
        else:
            print("Wrong choice Padawan")    
        #Finally insert the password    
        r(f'INSERT into Storage(website,url,user_id,password) VALUES ("{website}","{url}","{user_id}","{z}") ')
        print("The password has been setup!")
        return z

def fetch_pass(websit):
    try:
        if(r(f'select user_id from Storage where website="{websit}"').iloc[0,0]!=""):
            #pc.copy(r(f'SELECT password from Storage where website="{websit}"').iloc[0,0])
            jk = r(f'SELECT password from Storage where website="{websit}"').iloc[0,0]
            return 1, jk
    except:
        print("Hey! That website's login credentials don't exist. Create one?") 
        return 2, "no" 

def update_pass(i,otp,website,url,user_id,choice,*v):
 #Validate OTP

    try:
        if (r(f'select user_id from Storage where website="{website}"').iloc[0,0]!=""): 
            if i=="okay":
                #Send OTP
                r(f'DELETE FROM Storage where website="{website}"')
                insert_pass(website,url,user_id,choice,*v)
    except:
        print(f"{website} doesn't exist.")                

def console():

    print("\t\t\t\t\t\t\t\t\t PASSWORD MANAGER ")

    print("_____________________________________________________________________________________________________________________________________________________________________")
    print(time.asctime(),"\t\t\t\t\t\t\t\t\t\t\t\t\t\t", "developed by Anupam Misra")

    print("_____________________________________________________________________________________________________________________________________________________________________")
    print("Hello Anupam!")
    print("What do you wanna do today?")
    ink = input("1. Access a website \n 2. Create new login \n 3. Change credentials for a website")
    print("_____________________________________________________________________________________________________________________________________________________________________")
    if ink=="1":
        ik=input("Which website do you wanna visit?")
        jj=fetch_pass(ik)
        if jj==1:
            print("Please visit the website! The password has been copied")

    elif ink=="2":
        a=input("Which website do you wanna create a login for?")
        b=input("Please paste the website URL")
        c=input("Please enter login ID")
        d=input("How do you want to set up the password? \n 1. Enter keyphrase \n 2. Let us do it")
        if d=="1":
            e=input("Please enter keyphrase")
            insert_pass(a,b,c,int(d),e)
        elif d=="2":
            insert_pass(a,b,c,int(d))
        else:
            print("Please enter a valid choice")
    elif ink=="3":
        a=input("Please enter the website")
        b=input("Please paste the website URL")
        c=input("Please enter the login ID")
        d=input("How do you want to set up the password? \n 1. Enter keyphrase \n 2. Let us do it")
        if d=="1":
            e=input("Please enter keyphrase")
            update_pass(a,b,c,int(d),e)
        elif d=="2":
            update_pass(a,b,c,int(d))    
        else:
            print("Please enter a valid choice")  
    else:
        print("Please enter a valid choice") 
    print("_____________________________________________________________________________________________________________________________________________________________________")                                   
 
def forgot_passwd(answer, otp, passa):
    #Validate OTP
    #gospel is the security answer
    if(hashlib.sha224(answer.encode()).hexdigest()==gospel):
        r(f'UPDATE Password set pwd="{passa}"')
        print("Password was changed")
        _ = check_pwd(passa)
    
                    