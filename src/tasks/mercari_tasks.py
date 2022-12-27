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
from types_class import product


@task
def get_page_data(web_client: WebClient) -> WebElement:
    """
    ページの商品要素リストの親要素を取得する関数

    Args:
        page (int): 検索するページ番号
        keyword (str): 検索のキーワード

    Returns:
        el (WebElement): 要素リストの親要素
    """
    WebDriverWait(web_client.driver, timeout=10).until(
        lambda d: d.find_element(By.TAG_NAME, "mer-item-thumbnail")
    )
    els = web_client.find_element_by_id("item-grid")
    return els


@task
def convert_els_to_class(el: WebElement) -> List[product.Product]:
    """
    メルカリのリスト親Web要素からクラスへデータ変換する関数

    Args:
        page (int): 検索するページ番号
        keyword (str): 検索のキーワード

    Returns:
        el (WebElement): 要素リストの親要素
    """

    els = el.find_elements(By.TAG_NAME, "li")

    products: List[product.Product] = []

    for e in els:
        # 必要な要素の取得
        product_el = e.find_element(By.TAG_NAME, "mer-item-thumbnail")
        sticker = product_el.get_attribute("sticker")
        a_el = e.find_element(By.TAG_NAME, "a")

        # href = /item/mXXXXXX
        detail_url = a_el.get_attribute("href")
        p_id = re.search(r"(m\d{5,11})", detail_url)

        p = product.Product()
        p.name = product_el.get_attribute("item-name")
        p.price = int(product_el.get_attribute("price"))
        p.thumbnail = product_el.get_attribute("src")
        if p_id != None:
            p.id = p_id.group(1)
        if sticker == "sold":
            p.on_sale = False
        else:
            p.on_sale = True

        products.append(p)

    return products
