"""WebClient Module
* ウェブをクロールするクライアントモジュール
"""

from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


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
        # self.options.add_argument("--no-sandbox")  # 仮想環境下では、sandboxで起動すると失敗するので無効にする
        self.options.add_argument("--disable-gpu")  # ヘッドレスモードで起動するときに必要
        self.options.add_argument("--window-size=1280,1024")  # 画面サイズの指定
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.implicitly_wait(10)  # サイト開くまで10秒待機

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
        """FindElementByClassName
        * 指定したIdの要素をリストで取得する

        Args:
            class_name (str): 取得したい要素のクラス名
        """
        return self.driver.find_elements(By.CLASS_NAME, class_name)

    def find_elements_by_xpath(self, xpath: str) -> List[WebElement]:
        """FindElementByXPath
        * 指定したXPathの要素をリストで取得する

        Args:
            xpath (str): 取得したい要素のXPath
        """
        return self.driver.find_elements(By.XPATH, xpath)

    def find_elements_by_tag_name(self, tag_name: str) -> List[WebElement]:
        """FindElementByTagName
        * 指定したタグの要素をリストで取得する

        Args:
            tag_name (str): 取得したい要素のタグ
        """
        return self.driver.find_elements(By.TAG_NAME, tag_name)

    def find_element_by_id(self, id: str) -> WebElement:
        """FindElementById
        * 指定したIDの要素を取得する

        Args:
            tag_name (str): 取得したい要素のタグ
        """
        return self.driver.find_element(By.ID, id)

    def find_element_by_tag_name(self, tag_name: str) -> WebElement:
        """FindElementByTagName
        * 指定したタグの要素を取得する

        Args:
            tag_name (str): 取得したい要素のタグ
        """
        return self.driver.find_element(By.TAG_NAME, tag_name)

    def find_element_by_tag_name_with_wait(self, tag_name: str, sec: int) -> WebElement:
        """FindElementByTagNameWithWait
        * 指定したタグが読み込まれるまで待つ

        Args:
            tag_name (str): 取得したい要素のタグ
            sec (int): 待つ秒数
        """
        return WebDriverWait(self.driver, timeout=sec).until(
            lambda d: d.find_element(By.TAG_NAME, tag_name)
        )
