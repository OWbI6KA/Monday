import requests
import json
import sqlite3

if __name__ == '__main__':
    sqlite_connection = sqlite3.connect('monday1.db')
    cursor = sqlite_connection.cursor()
    # # sqlite_create_table='''CREATE TABLE monday (
    # #                               id INTEGER PRIMARY KEY,
    # #                               name TEXT NOT NULL,
    # #                               subtasks TEXT NOT NULL,
    # #                               contributor TEXT NOT NULL,
    # #                               status TEXT NOT NULL,
    # #                               timing TEXT NOT NULL,
    # #                               ref TEXT NOT NULL);'''
    # cursor = sqlite_connection.cursor()
    # sqlite_connection.commit()
    # cursor.close()
    apikey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE0MDk5OTY1OCwidWlkIjoyNzA5ODg5NiwiaWFkIjoiMjAyMi0wMS0xNVQxMTo0Nzo1MS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTA0MTgyNzYsInJnbiI6InVzZTEifQ.ae7AhCWsdxZ7Kseh3EYxzrd3e6u0HM6nmDDM1Gr3GWs"
    apiUrl = "https://api.monday.com/v2"
    headers = {"Authorization": apikey}
    query = '{ boards(ids:1921968816) { items { name subitems { name  } column_values(ids:[person,status,_____________,__________]) { text title value } } } }'
    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    data = json.loads(r.text)
    for kek in data['data']['boards'][0]['items']:

        temp = ""
        if kek['subitems'] == None:
            temp = "None"
        else:
            for t in kek['subitems']:
                temp = temp + t['name'] + "; "
        temp = temp[:-2]
        n = kek['name']
        c = kek['column_values'][0]['text']
        s = kek['column_values'][1]['text']
        t = kek['column_values'][2]['text']
        if kek['column_values'][3]['value'] != None:
            r = kek['column_values'][3]['value'].split(',')[-1]
        else:
            r = "None"
        insert = ''' INSERT INTO monday (name,subtasks,contributor,status,timing,ref)
        VALUES (?,?,?,?,?,?); '''
        dtuple = (n,temp,c,s,t,r)
        cursor.execute(insert,dtuple)
        sqlite_connection.commit()
    cursor.close()
