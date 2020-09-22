#add imports
import sqlite3
import csv



#open csv file
csvfile=open("music_titles.csv","r")
reader=csv.DictReader(csvfile)
title=[]
artist=[]
album=[]
writer=[]
othername=[]
isni=[]
ipi=[]
isrc=[]
sesac_id=[]
sesac_pub=[]
ascap_id=[]
ascap_pub=[]
ascap_ipi=[]
bmi_id=[]
bmi_pub=[]
gmr_id=[]
gmr_pub=[]
gmr_ipi=[]


#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     title.append(row["Track Title"])
     artist.append(row["Artist Name"])
     album.append(row["Album"])
     writer.append(row["Writer"])
     othername.append(row["Othername"])
     isni.append(row["ISNI code"])
     ipi.append(row["IPI code"])
     isrc.append(row["ISRC"])
     sesac_id.append(["SESAC Work ID"])
     sesac_pub.append(["SESAC Publisher"])
     ascap_id.append(["ASCAP Work ID"])
     ascap_pub.append(["ASCAP Publisher"])
     ascap_ipi.append(["ASCAP Publisher' IPI"])
     bmi_id.append(["BMI Work ID"])
     bmi_pub.append(["BMI Publisher"])
     gmr_id.append(["GMR Work ID"])
     gmr_pub.append(["GMR Publisher"])
     gmr_ipi.append(["GMR Publisher' IPI"])







#create new database

conn=sqlite3.connect('music_db.sqlite')
cur=conn.cursor()

#delete table if it exist
cur.execute("DROP TABLE IF EXISTS Music")

#creating table
cur.execute("""CREATE TABLE Music(title TEXT,artist TEXT,album TEXT,writer TEXT,
                                  othername TEXT,isni TEXT,ipi TEXT,isrc TEXT,
                                  sesac_id TEXT,sesac_pub TEXT,ascap_id TEXT,ascap_pub TEXT,
                                  ascap_ipi TEXT,bmi_id TEXT,bmi_pub TEXT,gmr_id TEXT,gmr_pub TEXT,gmr_ipi TEXT)""")
#inserting values into the Table
for i in range(0,len(title)):
	cur.execute("""INSERT INTO Music(title,artist,album,writer,othername,isni,ipi,
		                             isrc,
		                             sesac_id,sesac_pub,ascap_id,ascap_pub,ascap_ipi,
		                             bmi_id,bmi_pub,gmr_id,gmr_pub,gmr_ipi) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
		                             (title[i],artist[i],album[i],writer[i],
		                             othername[i],isni[i],ipi[i],"check",sesac_id[i],sesac_pub[i],ascap_id[i],
		                             ascap_pub[i],ascap_ipi[i],bmi_id[i],bmi_pub[i],gmr_id[i],gmr_pub[i],gmr_ipi[i]))
	conn.commit()





#display values from the database
sqlstr="SELECT title,artist FROM Music ORDER BY title"
for row in cur.execute(sqlstr):
	print(row[0],row[1])


cur.close()
















