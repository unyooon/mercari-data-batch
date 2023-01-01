"""Product
* 商品データの型定義モジュール
"""

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
from infra.db.settings import DbContext


class Product(DbContext.entity_base):
    """Product Class

    * 商品データの型定義クラス

    Attributes:
        id (str): 商品ID
        name (str): 商品名
        price (int): 金額
        on_sale (bool): 販売フラグ
        thumbnail (str): サムネイルURL
    """

    __tablename__ = "product"
    id = Column(String(12), primary_key=True)
    name = Column(String(255))
    price = Column(Integer)
    on_sale = Column(Boolean)
    thumbnail = Column(String(255))
