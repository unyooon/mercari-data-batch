"""ReadProduct Flow
* メルカリの商品データ取得のFlowモジュール
"""

from prefect import flow
from infra.client.web_client import WebClient
from types_class.pagination import Pagination
import tasks.mercari_tasks as mercari_tasks
import urllib.parse

from selenium.webdriver.common.by import By


@flow(validate_parameters=False)
def read_product(base_url: str, req: Pagination):
    """
    メルカリのデータ取得Flow
    """

    print("keyword", req.query.keyword)
    search_query = f"&keyword={req.query.keyword}"

    web_client = WebClient()
    for page in range(req.page_to):
        page_query = f"page_token=v1:{page}"
        q = f"{page_query}{search_query}"
        encoded_q = urllib.parse.quote(q, safe="?&=")

        print("open ", f"{base_url}/search?{encoded_q}")
        web_client.open_site(f"{base_url}/search?{encoded_q}")
        el = mercari_tasks.get_page_data(web_client)
        products = mercari_tasks.convert_els_to_class(el)
