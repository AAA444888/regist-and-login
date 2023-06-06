import pymysql
import db_dict  # 前面設的字典
id = "F12"
name = "mike"
gender = "male"
weight = "77"
height = "177"
age = "20"
db_settings = db_dict.dict()
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()
try:
    cursor.execute(f"UPDATE bmr_chart SET gender='{gender}',weight = '{weight}',height='{height}',age='{age}' WHERE name='{name}' AND id='{id}'")
    conn.commit()
    conn.close()
except Exception as e:
    conn.close()
    print(e)
