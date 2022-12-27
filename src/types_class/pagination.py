"""Pagination Module
* ページネーション用型定義モジュール
"""


from types_class.query import Query


class Pagination:
    """Pagination Class
    * ページネーション用型定義クラス

    Attributes:
        query (Query): リクエストクエリ
        page (int): 現在のページ
        page_from (int): 取得を開始するページ
        page_to (int): 取得を終了するページ
        size (int): ページサイズ
        total (int): すべての要素数
    """

    def __init__(
        self,
        query: Query,
        page: int = 0,
        page_from: int = 0,
        page_to: int = 50,
        size: int = 0,
        total: int = 0,
    ) -> None:
        """コンストラクタ
        Args:
            query (Query): リクエストクエリ
            page (int): 現在のページ
            page_from (int): 取得を開始するページ
            page_to (int): 取得を終了するページ
            size (int): ページサイズ
            total (int): すべての要素数
        """
        self.query = query
        self.page = page
        self.page_from = page_from
        self.page_to = page_to
        self.size = size
        self.total = total
        self.query = query
