"""WebClient Module
* ウェブをクロールするクライアントモジュール
"""

from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class WebClient:
    """WebClient Class
    * ウェブをクロールするクライアントクラス
    """

    def __init__(self) -> None:
        """コンストラクタ
        * クライアントの定義
        """
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")  # ヘッドレスで起動
        self.options.add_argument("--no-sandbox")  # 仮想環境下では、sandboxで起動すると失敗するので無効にする
        self.options.add_argument("--disable-gpu")  # ヘッドレスモードで起動するときに必要
        self.options.add_argument("--window-size=1280,1024")  # 画面サイズの指定
        self.driver = webdriver.Chrome(options=self.options)

    def __del__(self) -> None:
        """ファイナライザ
        * クライアントの接続を切断
        """
        self.driver.close()

    def open_site(self, url: str) -> None:
        """OpenSite Func
        * 指定したURLのWebサイトを開く

        Args:
            url (str): 開きたいWebサイトのURL
        """
        self.driver.get(url)

    def find_elements_by_class_name(self, class_name: str) -> List[WebElement]:
        """FindElementById
        * 指定したIdの要素をリストで取得する

        Args:
            id (str): 取得したい要素のId
        """
        return self.driver.find_elements(By.CLASS_NAME, class_name)
