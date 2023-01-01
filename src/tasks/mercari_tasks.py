"""Tasks Module
* メルカリのデータを取得するタスクのモジュール
"""

import re
from typing import List
from prefect import task
from selenium.webdriver.remote.webelement import WebElement
from infra.client.web_client import WebClient
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from dto.product import Product


@task
def get_page_data(web_client: WebClient) -> List[WebElement]:
    """
    ページの商品要素リストの取得する関数

    Args:
        page (int): 検索するページ番号
        keyword (str): 検索のキーワード

    Returns:
        el (List[WebElement]): 要素リスト
    """
    WebDriverWait(web_client.driver, timeout=10).until(
        lambda d: d.find_element(By.TAG_NAME, "mer-item-thumbnail")
    )
    el = web_client.find_element_by_id("item-grid")
    els = el.find_elements(By.TAG_NAME, "li")
    return els


@task
def convert_els_to_class(el: WebElement) -> Product:
    """
    メルカリのWeb要素リストからクラスへデータ変換する関数

    Args:
        page (int): 検索するページ番号
        keyword (str): 検索のキーワード

    Returns:
        (Product): 商品データクラス
    """
    # 必要な要素の取得
    product_el = el.find_element(By.TAG_NAME, "mer-item-thumbnail")
    sticker = product_el.get_attribute("sticker")
    a_el = el.find_element(By.TAG_NAME, "a")
    # href = /item/mXXXXXX
    detail_url = a_el.get_attribute("href")
    p_id = re.search(r"(m\d{5,11})", detail_url)
    p = Product()
    p.name = product_el.get_attribute("item-name")
    p.price = int(product_el.get_attribute("price"))
    p.thumbnail = product_el.get_attribute("src")
    if p_id != None:
        p.id = p_id.group(1)
    if sticker == "sold":
        p.on_sale = False
    else:
        p.on_sale = True

    return p
