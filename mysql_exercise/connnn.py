import pymysql
import db_dict  # 前面設的字典

db_settings = db_dict.dict()
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()
try:
    sql = "" #要執行的指令
    cursor.execute(sql)
    conn.commit()
    conn.close()
except Exception as e:
    conn.close()
    print(e)