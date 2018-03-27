import csv
import MySQLdb


mydb = MySQLdb.connect("127.0.0.1","root","Wanqing0930","Baseball" )
rowcount=0
print 'connected to data base'
cursor = mydb.cursor()

cursor.execute('CREATE TABLE HallOfFame (HOF_id int primary key auto increment, playerID varchar(45), yearid year(4) , votedBy varchar(45) , ballots varchar(45) , needed varchar(45) , votes varchar(45) , inducted varchar(45) , category varchar(45))')
#commit all insert transactions here
mydb.commit()
#close the connection to the database.
cursor.close()

print "Done"
