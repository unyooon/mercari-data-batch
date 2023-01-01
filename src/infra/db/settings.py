"""Settings
* DB情報の定義モジュール
"""

import os
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base


class DbContext:
    """DbContext
    * DB情報の定義クラス

    Attribute:
        engine (Engine): DB接続するためのEngineインスタンス
        session (scoped_session): DBとやり取りをするためのインスタンス
        base (Type[_DeclarativeBase]): ClassとDBをMappingするために利用
    """

    entity_base = declarative_base()

    def __init__(self) -> None:
        """__init__
        * DBインスタンスの生成コンストラクタ
        """
        dialect = "mssql"
        driver = "pyodbc"
        username = os.getenv("DB_USER_NAME")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST_IP")
        port = "1433"  # Azure SQL Database サービスは TCP ポート 1433 経由でのみ利用できます
        database = os.getenv("DB_NAME")
        charset_type = "utf8"
        db_url = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset={charset_type}&driver=ODBC+Driver+17+for+SQL+Server"
        print(db_url)

        # DB接続するためのEngineインスタンス
        self.engine = create_engine(db_url, echo=True)

        # DBに対してORM操作するときに利用
        # Sessionを通じて操作を行う
        self.session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
