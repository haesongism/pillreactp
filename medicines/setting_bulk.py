from elasticsearch import Elasticsearch
import json


es = Elasticsearch()

es.indices.create(
    index='medicine',
    body={
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "nori_tokenizer"
                        }
                    }
                }
            }
        },
        "mappings": {
            "medicines_data": {
                "properties": {
                    "id": {
                        "type": "long"
                    },
                    "name": {
                        "type": "text",
                        "analyzer": "my_analyzer"
                    },
                    "etcChoices": {
                        "type": "text",
                        "analyzer": "my_analyzer"
                    },
                    "rating": {
                        "type": "text",
                        "analyzer": "my_analyzer"
                    }
                }
            }
        }
    }
)

with open("D:/db/elastic.json", encoding='utf-8') as json_file:
    json_file = json.load(json_file.read())

body = ""
for i in json_file:
    body = body + json.dumps({"index": {"_index": "medicine", "_type": "medicines_data"}}) + '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'

es.bulk(body)


