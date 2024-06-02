import mysql.connector
#LLMの出力をキーごとに分けてデータベースに入れる
def input_arrange(text,word):
    divide = text.split('\n')
    n = (len(divide)+1)//5
    if n >= 1:
        for i in range(n):
            title = divide[0+i*5]
            search = '検索ワード: ' + word
            url = divide[1+i*5]
            summary = divide[2+i*5]
            keyword = divide[3+i*5]
            #print(f'{title}\n{search}\n{url}\n{summary}\n{keyword}\n\n')
            deta_add(title, search, url, summary, keyword)


def deta_add(title, search, url, summary, keyword):

    # データベース接続情報
    db_host = "mysql-paper"
    db_user = "paper"
    db_password = "paper"
    db_name = "paper"

    # データベースへの接続
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name, charset='utf8')

    # カーソルの取得
    cursor = conn.cursor()

    # SQL文の作成
    sql = """
    INSERT INTO articles (title, search, url, summary, keyword)
    VALUES (%s, %s, %s, %s, %s)
    """

    # データのバインド
    cursor.execute(sql, (title, search, url, summary, keyword))

    # コミット
    conn.commit()

    # カーソルのクローズ
    cursor.close()

    # データベース接続のクローズ
    conn.close()


