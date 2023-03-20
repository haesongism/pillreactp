import pymysql
from elasticsearch import Elasticsearch
import json

# MySQL 데이터 추출
conn = pymysql.connect(user = 'root', host = 'localhost', passwd='root', port=3306, db='django')
cursor = conn.cursor()
cursor.execute('SELECT * FROM pharmacies_pharmacy')
results = cursor.fetchall()# 쿼리문 결과값 저장

# 엘라스틱에 저장
es = Elasticsearch()
for result in results:
    # 데이터를 색인할 인덱스 이름을 정의
    index_name = 'pharmacy'

    # Elasticsearch에 색인할 데이터를 정의.
    # MySQL 테이블의 각 행을 Python 딕셔너리로 변환
    data = {
       "id": result[0],
       "title": result[1],
       "callNumber": result[2],
       "address": result[3],
       "coordinate_X": result[4],
       "coordinate_Y": result[5],
       # 데이터 열 수에 따라 필드 추가.
    }
    es.index(index='pharmacy', body=data)

    res = es.search(
        index = 'pharmacy',
        body={
            'query':{'match_all':{}}
        }
    )

    print(json.dumps(res,ensure_ascii=False, indent=4))