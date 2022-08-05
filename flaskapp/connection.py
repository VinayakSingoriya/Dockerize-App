import pymysql

try:

    # conn = pymysql.connect(
    #         host= 'record-testing.cmjf6xf1uo4z.us-east-1.rds.amazonaws.com', 
    #         port = '3306',
    #         user = 'admin', 
    #         password = 'vinayak123',
    #         db = 'vinayakRecord',          
    #         )

    db = pymysql.connect(
            host='record-testing.cmjf6xf1uo4z.us-east-1.rds.amazonaws.com',
            user='admin',
            password='vinayak123',
            database='vinayakRecord',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)



    print("Connection is established")

    cursor=db.cursor()
    # sql = """
    #     CREATE TABLE record (
    #     id int NOT NULL AUTO_INCREMENT,
    #     title varchar(255) NOT NULL,
    #     complete BOOLEAN,
    #     PRIMARY KEY (id)
    #     )
    #     """

    cursor.execute("show tables")
    myresult = cursor.fetchall()
 
    for x in myresult:
        print(x)
    


    db.close()
    print("connection is closed")
except Exception as e:
    print(e)
    print("Connection Not Established")