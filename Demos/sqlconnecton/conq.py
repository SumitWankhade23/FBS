import mysql.connector as ct
con = None
try:
    con = ct.connect(host='localhost',
                    user = 'root',
                    password = 'Sanju@230411',
                    database = 'FirstBit')
    #Everything we wil do in exception block for database connectivity
    # It will comes under try block

    ##1st Qury to CREATE datbase    
    cursor = con.cursor()
    #cursor.execute("CREATE DATABASE FirstBit")

    ##2nd Query to CREATE TABLE
    #cursor.execute("CREATE TABLE student(rollno int, Name varchar(30))")

    ##3rd Query to SHOW TABLES
    # cursor.execute("SHOW TABLES ")
    # for i in cursor:
    #     print(i)

    ##4rth INSERT INTO TABLE
    # cursor.execute("insert into student(rollno,Name) values(%s,%s)",(101,"Sachin"))
    # print(cursor.rowcount,"Affected")
    # con.commit()                               #This is DML query so we have to commit()

    ##Insert single element into table

    ##5th Insert multiple data line in table
    # query = "insert into student(rollno,Name) values(%s,%s)"
    # values = [(100,"Sakshi"),(102,"Uday"),(103,"Rahul"),(104,"Shubham")]  
    # cursor.executemany(query,values)             #executemany execute all the tuple values
    # print(cursor.rowcount,"Affected")
    # con.commit()

    ##6th SELECT command
    # cursor.execute("SELECT * FROM Student")
    # d = cursor.fetchall()
    #d = cursor.fetchone()
    #print(d)
    # for i in d:
    #     print(i)


    ##7th UPDATE command
    ##UPDATE
    # q ='UPDATE Student SET rollno = %s WHERE Name=%s'
    # val = [("Smriti",18),("Kranti",45)]
    
    q ='UPDATE Student SET rollno = %s WHERE Name=%s'
    val = [(109,"Surya",)]
    #cursor.execute(q,val)
    cursor.executemany(q,val)
    print(cursor.rowcount,"is Afected")
    con.commit() 
        
    ##8th DELETE
    # qd = 'DELETE FROM Student WHERE rollno = %s'
    # val = (45,)
    # cursor.execute(qd,val)
    # con.commit()
    # print(f"{cursor.rowcount}Row is Affected")
        
    ##9th TRUNCATE 
    # tq = "TRUNCATE TABLE Student"
    # cursor.execute()
    # con.close()



except Exception as e:
    print(e)    

# if con is not None:
#     print("Successfully connected, Enjoy!")
# else:
#     print("Somethong went wrong met, please check your credencial")  

    