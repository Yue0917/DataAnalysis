import csv
import MySQLdb


mydb = MySQLdb.connect("127.0.0.1","root","Wanqing0930","Baseball" )
rowcount=0
print 'connected to data base'
cursor = mydb.cursor()

csv_data = csv.reader(file('Batting.csv'),quoting=csv.QUOTE_NONE)

print 'file opened'
for row in csv_data:
    #print rowcount
    print row
    if rowcount > 0:
        cursor.execute('INSERT INTO Batting(playerID,yearID,teamID,Games,Atbats,Runscored,Hits,Homeruns,Runbattedln,Walks,strikeOuts)' \
                                     'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            row)
    rowcount += 1
#commit all insert transactions here
,%s,%s,%s,%smydb.commit()
#close the connection to the database.
cursor.close()
print "Done"
