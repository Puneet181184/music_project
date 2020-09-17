# add import statements
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import string
import json
import csv
import musicbrainzngs


# create ssl certifications
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#Reading csv file to read tracktitle and artistname
csvfile=open("project1.csv","r")
reader=csv.DictReader(csvfile)
title=[]
artist=[]
for row in reader:
	#print(row["Track Title"])
     title.append(row["Track Title"])
     artist.append(row["Artist Name"])
     #print(artist)

# setting up useragent for musicbrainzngs API
musicbrainzngs.set_useragent("MyTrial","0.0","chemical.puneet@gmail.com")
#musicbrainzngs.set_format("json")
#artist=["bruno mars","taylor swift"]

name=[]
ipi=[]
isni=[]
alias=[]
isrc=[]
album=[]
for i in range(0,len(title)):
   #print(x)
# using musicbrainzngs search API for artists   
   result=musicbrainzngs.search_artists(artist=artist[i])
# using musicbrainzngs search API for tracks   
   result1=musicbrainzngs.search_recordings(recording=title[i],artist=artist[i])
#print (result)
   try:
        list=result["artist-list"][0]
   except:
        print(artist[i])     
   #print("name=",list["name"])
   #print("ipi=",list["ipi-list"])
   #print("isni=",list["isni-list"])
# reading artistname and appending into name array   
   try:
        name.append(list["name"])
   except:
        name.append("not found")
# reading ipi list and appending into ipi array        
   try:          
        ipi.append(list["ipi-list"])
   except:
        ipi.append("not found")
# reading isni list and appending into isni array        
   try:          
        isni.append(list["isni-list"])
   except:
        isni.append("not found")
# reading alias list and appending into alias array        
   try:     
        alias.append(list["alias-list"][0]["alias"])
   except: 
        alias.append("not found")  
        #print("entry not found")
        #print("artist=",artist[i])
# reading isrc value and appending into isrc array        
   try:
   	    isrc.append(result1["recording-list"][0]["id"])
   except:
        isrc.append("not found")
# reading album name and appending into album array        
   try:
   	    album.append(result1["recording-list"][0]["release-list"][0]["title"])
   except:
        album.append("not found")


# open a csv file list.csv
csvfile=open("list.csv","wt",newline="")
writer=csv.writer(csvfile)
#writing headings for csv file
writer.writerow(("Tracktitle","Artistname","Othername","ISNI code","IPI code","ISRC","album"))
for i in range(0,len(title)):
# writing values into csv file
   try:
   	    writer.writerow((title[i],artist[i],alias[i],isni[i],ipi[i],isrc[i],album[i]))
   except:
   	    writer.writerow((title[i],artist[i],"not found",isni[i],ipi[i],isrc[i],"not found"))







