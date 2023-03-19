from django.apps import AppConfig
from elasticsearch import Elasticsearch

class MedicinesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medicines'

    def ready(self):
        # test3
        # Elasticsearch 인덱스 생성
        es = Elasticsearch("localhost:9200")
        #es.indices.create(index='id', ignore=400)

        # MySQL 데이터를 Elasticsearch에 저장
        from medicines.models import Medicine
        from django.db.models.signals import post_save
        from django.dispatch import receiver
        """
        @receiver(post_save, sender=Medicine)
        def save_to_elasticsearch(sender, instance, **kwargs):
            es.index(index='id', body={
                'name': instance.name,
                'effect': instance.effect,
            })
        
        def copy_to_elasticsearch():
            # 모든 MyModel 객체 가져오기
            mymodels = Medicine.objects.all()

            # Elasticsearch에 저장하기
            for mymodel in mymodels:
                es.index(index='medicine', body=mymodel)

        copy_to_elasticsearch()"""