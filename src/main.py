"""Main
* メインモジュール
"""

from types_class.pagination import Pagination
import flow
from types_class.query import Query

BASE_URL = "https://jp.mercari.com"


def main():
    """Main Function
    * メイン関数
    """
    q = Query(keyword="ティファニー")
    req = Pagination(q, page_to=2)

    flow.read_product(BASE_URL, req)


if __name__ == "__main__":
    main()
