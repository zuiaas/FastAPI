import mysql.connector
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

def connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='1201599',
        database='ponto',
        port=3306
    )

@app.get("/usuarios")
def get_usuarios():
    db = connection()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM usuarios")
        res = cursor.fetchall()
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db.close()