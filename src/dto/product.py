"""Product Module

* 商品データの型定義モジュール

"""


class Product:
    """Product Class

    * 商品データの型定義クラス

    Attributes:
        id (str): 商品ID
        name (str): 商品名
        price (int): 金額
        on_sale (bool): 販売フラグ
        thumbnail (str): サムネイルURL
    """

    def __init__(self):
        """コンストラクタ
        * コンストラクタ
        """
        self.id = ""
        self.name = ""
        self.price = 0
        self.on_sale = True
        self.thumbnail = ""
