import pymysql
import db_dict  # 前面設的字典
id = "F12"
name = "mike"
gender = "male"
weight = "71"
height = "174"
age = "20"
db_settings = db_dict.dict()
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()
try:
    cursor.execute(f"SELECT * FROM bmr_chart WHERE name = '{name}' AND id = '{id}'")
    line = cursor.fetchall()
    print(line[0])
    conn.commit()
    conn.close()
except Exception as e:
    conn.close()
    print(e)