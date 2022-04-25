from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from elasticsearch import Elasticsearch


class SearchView(APIView):

    def get(self, request):
        es = Elasticsearch(hosts='localhost',port=9200)

        # 검색어
        search_word = request.query_params.get('search')

        if not search_word:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})
        docs = es.search(index='dictionary',
                         body={
                             "query": {
                                 "multi_match": {
                                     "query": search_word,
                                     "fields": ["name", "info"]
                                 }
                             }
                         })

        data_list = docs['hits']

        return Response(data_list)