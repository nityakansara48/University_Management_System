import mysql.connector
import csv

mydb = mysql.connector.connect(host="acadmysqldb001p",user="nxk9794",password="Nhk@241098",database="nxk9794")
q = mydb.cursor()

with open('datafiles\EMPLOYEE.csv', newline='') as f1:
    reader = csv.reader(f1)
    for row in reader:
        q.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
        
with open('datafiles\DEPARTMENT.csv', newline='') as f1:
    reader = csv.reader(f1)
    for row in reader:
        q.execute("insert into department values(%s,%s,%s,%s)",row)

with open('datafiles\DEPENDENT.csv', newline='') as f1:
    reader = csv.reader(f1)
    for row in reader:
        q.execute("insert into dependent values(%s,%s,%s,%s,%s)",row)

with open('datafiles\DEPT_LOCATIONS.csv', newline='') as f1:
    reader = csv.reader(f1)
    for row in reader:
        q.execute("insert into dept_locations values(%s,%s)",row)
        
with open('datafiles\PROJECT.csv', newline='') as f1:
    reader = csv.reader(f1)
    for row in reader:
        q.execute("insert into project values(%s,%s,%s,%s)",row)

with open('datafiles\works_on.csv', newline='') as f1:
    reader = csv.reader(f1)
    for row in reader:
        q.execute("insert into works_on values(%s,%s,%s)",row)

mydb.commit()
q.close()
