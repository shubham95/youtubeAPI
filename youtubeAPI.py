#Given a youtube ID extract its Description,like,dislikes,viewcount,Comment ,etc
# i m writing it in csv file for latter use

# im using list of all vedio ID in allid[]

import pandas as pd
import numpy as np
import requests
import csv
import json

import re
import time
start_time=time.clock()
#count=0
with open('data_point_part2.csv','w',newline='') as obj:
    thewriter =csv.writer(obj)
    thewriter.writerow(["ID","publishedAt","description","viewCount","likeCount","dislikeCount","favoriteCount","title","comment_top_50"])
    for i in range(b,d):
        try:
            
            url="https://www.googleapis.com/youtube/v3/videos?key="+"Copy your own API key"+"&part=snippet,statistics&id="+allid[i]
            
            result=requests.get(url).json()
            try:
                publishedAt=result["items"][0]["snippet"]["publishedAt"]
            except:
                publishedAt=""
            try:
                title=result["items"][0]["snippet"]["title"]
#                 title=re.sub(r'[?|!|\'|"|#]',r'',title)
#                 title=re.sub(r'[.|,|)|(|\|/]',r' ',title)
                title=title.replace(',',' ')
                title="%r"%title
            except:
                publishedAt=""
            try:
                description=result["items"][0]["snippet"]["description"]
#                 description=re.sub(r'[?|!|\'|"|#]',r'',description)
#                 description=re.sub(r'[.|,|)|(|\|/]',r' ',description)
                description=description.replace(',',' ')
                description="%r"%title
            except:
                description=""
            try:
                viewCount=result["items"][0]["statistics"]["viewCount"]
            except:
                viewCount=""
            try:
                likeCount=result["items"][0]["statistics"]["likeCount"]
            except:
                likeCount=""
            try:
                dislikeCount=result["items"][0]["statistics"]["dislikeCount"]
            except:
                dislikeCount=""
            try:
                favoriteCount=result["items"][0]["statistics"]["favoriteCount"]
            except:
                favoriteCount=""
            #for 50 comment
            
            url2="https://www.googleapis.com/youtube/v3/commentThreads?key="+"Copy your own API key"+"&textFormat=plainText&part=snippet&videoId="+allid[i]+"&maxResults=50"
            
            cmt=requests.get(url2).json()
            try:
                ssl=len(cmt["items"])
                comment=""
                for j in range(0,ssl):
                    comment+=cmt["items"][j]["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            except:
                comment=""
#             comment=comment.replace("\n", "\\\\")
            
#             comment=comment.replace("\\", "\\\\")
#             comment=comment.replace("\\", "\\\\")
            
#             comment=re.sub(r'[|?|!|\'|"|#]',r'',comment)
#             comment=re.sub(r'[.|,|)|(|\|/]',r' ',comment)
            comment=comment.replace(',','')
            comment="%r"%comment
            #count+=1
#             print(allid[i],publishedAt,description,viewCount,likeCount,dislikeCount,favoriteCount,title,comment)
            thewriter.writerow([allid[i],publishedAt,description,viewCount,likeCount,dislikeCount,favoriteCount,title,comment])
        except:
            continue
            
        

print(time.clock()-start_time)