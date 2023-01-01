"""Main
* メインモジュール
"""
import flow
from dotenv import load_dotenv

from infra.db.settings import DbContext
from dto.pagination import Pagination
from dto.query import Query

BASE_URL = "https://jp.mercari.com"


def main():
    """Main Function
    * メイン関数
    """

    load_dotenv()

    db = DbContext()

    q = Query(keyword="ティファニー")
    req = Pagination(q, page_to=2)

    flow.read_product(db, BASE_URL, req)


if __name__ == "__main__":
    main()
