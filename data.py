import requests
import json
import sqlite3
import time


def data():
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    # # sqlite_create_table='''CREATE TABLE monday (
    # #                               id INTEGER PRIMARY KEY,
    # #                               name TEXT NOT NULL,
    # #                               subtasks TEXT NOT NULL,
    # #                               contributor TEXT NOT NULL,
    # #                               status TEXT NOT NULL,
    # #                               timing TEXT NOT NULL,
    # #                               ref TEXT NOT NULL);'''
    apikey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE0MDk5OTY1OCwidWlkIjoyNzA5ODg5NiwiaWFkIjoiMjAyMi0wMS0xNVQxMTo0Nzo1MS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTA0MTgyNzYsInJnbiI6InVzZTEifQ.ae7AhCWsdxZ7Kseh3EYxzrd3e6u0HM6nmDDM1Gr3GWs"
    apiUrl = "https://api.monday.com/v2"
    headers = {"Authorization": apikey}
    query = 'query {  boards(ids:1921968816)   {     items    { id      name       subitems       {         name        }       column_values(ids:[person,status,_____________,_____,__________])       {         text         title        value              }     }  } }'
    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    data = json.loads(r.text)
    delete = ''' DELETE FROM monday_data; '''
    cursor.execute(delete)
    sqlite_connection.commit()
    for kek in data['data']['boards'][0]['items']:

        temp = ""
        if kek['subitems'] == None:
            temp = "None"
        else:
            for t in kek['subitems']:
                temp = temp + t['name'] + "; "
        temp = temp[:-2]
        # n = kek['name']
        # c = kek['column_values'][0]['text']
        # s = kek['column_values'][1]['text']
        # t = kek['column_values'][2]['text']
        if kek['column_values'][3]['text'] != "":
            r = kek['column_values'][3]['text'].split(' ')[2]
        else:
            r = "None"
        insert = ''' INSERT INTO monday_data (task_id,name,subtasks,contributor,people,status,timing) VALUES (?,?,?,?,?,?,?); '''
        dtuple = (kek['id'], kek['name'], temp, kek['column_values'][0]['text'], kek['column_values'][1]['text'],
                  kek['column_values'][2]['text'], r)
        cursor.execute(insert, dtuple)
        sqlite_connection.commit()
    cursor.close()
