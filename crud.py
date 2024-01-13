# import mysql.connector
#
# # connect to the database server
#
# try:
#     print('waiting for connection ... ')
#     conn=mysql.connector.connect(
#     host = '127.0.0.1',
#     user = 'root',
#     password = "#define cse 2018331032;",
#     port= '3306',
#     database='indigo'
#     )
#     mycursor=conn.cursor()
#     print('\t and connection done ___ ')
#
# except:
#
#     print('connection error')
#
# # create a database on the db server
#
#
# # mycursor.execute("CREATE DATABASE indigo")
# # conn.commit()
#
# # Create table
# # airport-> airport_id|code|name
#
# # mycursor.execute("""
# # Create table if not exists airport (
# #       airport_id integer primary key,
# #       code varchar(10) NOT NULL,
# #       city varchar(50) NOT NULL,
# #       name varchar(255) NOT NULL
# #       )
# # """)
# # conn.commit()
#
#
# #search /Retrieve
# # mycursor.execute("""
# #     INSERT INTO airport VALUES
# # (1,'DHA','DHAKA','HSIA'),
# # (2,'CHT','CHATTAGRAM','CIA'),
# # (3,'SYL','SYLHET','GOIA'),
# # (4,'CXB','COXSBAZAR','COXIA')
# # """)
# # conn.commit()
#
# mycursor.execute("select * from airport where airport_id>1")
# data=mycursor.fetchall()
#
# for i in data :
#     print(i[3])
#
# #updata
#
# # mycursor.execute("""
# # UPDATE airport
# # set name ='CHITTAGONG'
# # WHERE airport_id=2
# # """)
# # conn.commit()
#
# #print(data)
#
# #Delete
#
# mycursor.execute("""DELETE FROM AIRPORT WHERE AIRPORT_ID =4""")
# conn.commit()
#
# mycursor.execute(""" select * from airport where airport_id>1 """)
# data=mycursor.fetchall()
# print(data)
