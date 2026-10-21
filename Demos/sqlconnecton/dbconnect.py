import mysql.connector as connect 
try:
    con = None
    #step1 form a connection 
    con = connect.connect(host='localhost',
                    user = 'root',
                    password = 'Sanju@230411',
                    database = 'ABCD'
                    )
    # if con.is_connected():
    #     print("Success")
    # else:
    #     print("Fail")  
        
    
    ## step2- create cursor   
    cursor = con.cursor()                                                    #cursor is bridg between our file to sql sysytem 
    
    ## Step 3: run the SQL
    #cursor.execute("CREATE DATABASE IF NOT EXISTS ABCD")                    #execute fire the curry to datase 
    #print("Database ABCD is ready")
    #cursor.execute('CREATE TABLE Emp(eid int,ename varchar(20))')
    
    #It show how many tables have been created 
    # cursor.execute('show tables')
    # for i in cursor:
    #     print(i)#It show output in tuple form
    
    ##For insert into table
    query = "INSER INTO emp(eid,name) VALUES(%s,%s)"
    #value =("ABD",17)
    #cursor.execute(query,value)
    #print(cursor.rowcount,"Executed")
    #con.commit()

    ##For many input insert LIST
    value =[("Rahul",10),("Virat",18)]
    con.executemany(query,value)
    print(cursor.rowcount,"Affected")
    con.commit()


except Exception as e:
    print(e)
        
    
    