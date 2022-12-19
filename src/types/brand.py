"""Brand Module

* ブランドの型定義モジュール

"""


class Brand:
    """Brand Class

    * ブランドの型定義クラス

    Attributes:
        id (int): ID
        name (str): ブランド名
        subname (str): 英記号表記のブランド名
    """

    def __init__(self, id: int, name: str, subname: str) -> None:
        """コンストラクタ
        Args:
            id (int): ID
            name (str): ブランド名
            subname (str): 英記号表記のブランド名
        """
        self.id = id
        self.name = name
        self.subname = subname
