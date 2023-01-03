"""ReadProduct Flow
* メルカリの商品データ取得のFlowモジュール
"""

from prefect import flow
from typing import List
import urllib.parse

from infra.client.web_client import WebClient
from dto.pagination import Pagination
from dto.product import Product
import tasks.mercari_tasks as mercari_tasks


@flow(validate_parameters=False)
def read_product(base_url: str, req: Pagination):
    """
    メルカリのデータ取得Flow

    Args:
        base_url (str): メルカリのBASE_URL
        req (Pagination): ページとクエリ関連のリクエスト
    """

    search_query = f"&keyword={req.query.keyword}"

    web_client = WebClient()
    for page in range(req.page_to):
        page_query = f"page_token=v1:{page}"
        q = f"{page_query}{search_query}"
        encoded_q = urllib.parse.quote(q, safe="?&=")

        web_client.open_site(f"{base_url}/search?{encoded_q}")
        els = mercari_tasks.get_page_data(web_client)
        products: List[Product] = []
        for el in els:
            products.append(mercari_tasks.convert_els_to_class(el))
