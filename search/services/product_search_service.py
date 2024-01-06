from elasticsearch_dsl import Q
from django.utils import timezone
from search.documents.product_document import ProductDocument


class ProductSearchService:

    @staticmethod
    def get_active_product_query():
        now = timezone.now()

        query = Q(
            Q("match", is_active=True)
            & Q("range", valid_from={"lte": now})
            & Q("range", valid_until={"gte": now})
        )
        return query

    def get_products(self, query_params):
        """
        Search product by name/code
        :param query_params: Dict data type, contain search keyword.
        :return:
        """
        keyword = query_params.get('keyword')
        es_query = ProductDocument.search()
        # get active products
        active_product_query = self.get_active_product_query()
        es_query = es_query.query(active_product_query)

        # get products according to search
        es_query = es_query.query(
            Q("match", name=keyword)
            | Q("term", code=keyword)
        )
        products = es_query.execute()
        return products
