# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:03:33 2020

@author: Bassat
"""

def test(critere1, critere2):
    
    mdict = {}
    
    fieldnames = ["author2","editor","title","booktitle","pages","year","address"
            ,"journal","volume","number","month","url","ee","cdrom","cite"
            ,"publisher","note","crossref","isbn","series","school","chapter"
            ,"publnr", "key", "mdate", "type"]
    
    nom_col = ["auteur", "titre", "date de publication", "type", "journal", "clef"]
    col_imp = ["author2","title","mdate","type","journal","key"]
    import os
    
    filename = "export.csv"
    filename2 = "export2.csv"
    
    import csv
    
    try:
        os.remove(filename2)
    except OSError:
        pass
    
    with open('../data/export2.csv', 'a', newline ='', encoding="utf-16") as csvfile:
        writer = csv.writer(csvfile, delimiter = ";")
        writer.writerow(nom_col)
    
    with open(filename, 'r', encoding = "utf-16") as f:
    
        reader = csv.DictReader(f, fieldnames = fieldnames, delimiter = ";")
        if critere1 == "author":
            for row in reader:
                if critere2 in row["author2"]:
                    for i in col_imp:
                        mdict[i] = row[i]
    
                    with open('../data/export2.csv', 'a', newline ='', encoding="utf-16") as csvfile:
                         writer = csv.DictWriter(csvfile, ["author2", "title", "mdate", "type", "journal", "key"]
                                                 , delimiter = ";")
                         writer.writerow(mdict)
        elif critere1 == "publ":
            for row in reader:
                if critere2 in row["title"]:
                    for i in col_imp:
                        mdict[i] = row[i]
    
                    with open('../data/export2.csv', 'a', newline ='', encoding="utf-16") as csvfile:
                         writer = csv.DictWriter(csvfile, ["author2", "title", "mdate", "type", "journal", "key"]
                                                 , delimiter = ";")
                         writer.writerow(mdict)
        elif critere1 == "venue":
            for row in reader:
                if critere2 in row["journal"]:
                    for i in col_imp:
                        mdict[i] = row[i]
    
                    with open('../data/export2.csv', 'a', newline ='', encoding="utf-16") as csvfile:
                         writer = csv.DictWriter(csvfile, ["author2", "title", "mdate", "type", "journal", "key"]
                                                 , delimiter = ";")
                         writer.writerow(mdict)
    

