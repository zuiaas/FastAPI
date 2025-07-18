import pymysql
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='pontest',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/usuarios")
def usuarios():
    db = connection()
    try:
        with db.cursor() as cursor:
            sql = "SELECT * FROM usuarios"
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
    finally:
        db.close()