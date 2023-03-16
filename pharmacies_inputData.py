import pandas as pd
import pymysql
from sqlalchemy import create_engine

df = pd.read_csv('D:/db/phamacies_noCreatedupdated.csv', index_col=0)#,encoding='cp949' 

db = pymysql.connect(user = 'root', host = 'localhost', passwd='root', port=3306, db='django')
cursor = db.cursor()

engine = create_engine("mysql+pymysql://root:"+"root"+"@localhost:3306/django?charset=utf8")
conn = engine.connect()
df.to_sql(name = "pharmacies_pharmacy", con=engine, if_exists='append', index=False)#, index_label="id"
conn.close()

# admin 에서 같이 활용하려면 제공하는 속성과 column의 일체화가 필요하다.