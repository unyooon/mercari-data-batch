"""Query Module

* 商品検索時のクエリ型定義モジュール

"""


class Query:
    """Query Class

    商品検索時のクエリ型定義

    Attributes:
        keyword (str): 検索文字列
        category (int): カテゴリ
        brand (int): ブランド
        price_min (int): 最低価格
        price_max (int): 最高価格
        goods_status (int): 商品の状態
        sales_status (int): 販売状況
    """

    def __init__(
        self,
        keyword: str = "",
        goods_status: int = 0,
        sales_status: int = 0,
        category: int = 0,
        brand: int = 0,
        price_min: int = 0,
        price_max: int = 999999,
    ) -> None:
        """コンストラクタ
        Args:
            keyword (str): 検索文字列
            category (int): カテゴリ
            brand (int): ブランド
            price_min (int): 最低価格
            price_max (int): 最高価格
            goods_status (int): 商品の状態
            sales_status (int): 販売状況
        """
        self.keyword = keyword
        self.category = category
        self.brand = brand
        self.goods_status = goods_status
        self.sales_status = sales_status
        self.price_min = price_min
        self.price_max = price_max
