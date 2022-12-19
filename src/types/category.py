"""Category Module

* カテゴリーの型定義モジュール

"""


class Category:
    """Category Class
    * カテゴリーの型定義

    Attributes:
        id (int): ID
        level (int): カテゴリの階層
        name (str): カテゴリ名
        parent_id (int): 親カテゴリのID
    """

    def __init__(self, id: int, level: int, name: int, parent_id: int) -> None:
        """コンストラクタ
        Args:
            id (int): ID
            level (int): カテゴリの階層
            name (str): カテゴリ名
            parent_id (int): 親カテゴリのID
        """
        self.id = id
        self.level = level
        self.name = name
        self.parent_id = parent_id
