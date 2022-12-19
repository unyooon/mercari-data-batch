"""MercariTasks Module
* メルカリのデータを取得するタスクのモジュール
"""

from prefect import task


@task
def get_page_data(page: int, keyword: str):
    """
    指定したキーワードとページのデータを取得する関数

    Args:
        page (int): 検索するページ番号
        keyword (str): 検索のキーワード
    """
