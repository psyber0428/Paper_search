import mysql.connector

# データベース接続情報
db_host = "mysql-paper2"
db_user = "paper"
db_password = "paper"
db_name = "paper"


def candidate():
# データベースへの接続
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name, charset='utf8')

    cursor = conn.cursor()

    # 全データを取得する場合
    cursor.execute("SELECT search FROM articles GROUP BY search;")

    # 取得結果をフェッチ
    results = cursor.fetchall()

    candi_list = []

    for row in results:
        candi_list.append(row[0].split(':')[1])  # 各行のデータを出力

    cursor.close()
    conn.close()
    
    return candi_list


def select_output(select):
    # データベースへの接続
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name, charset='utf8')

    cursor = conn.cursor()

    name = '検索ワード:' + select

    # 全データを取得する場合
    cursor.execute("SELECT title, search, url, summary, keyword FROM articles WHERE search = %s;", (name,))

    # 取得結果をフェッチ
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results






