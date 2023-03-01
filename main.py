import pymysql


def getinfo():
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="111111",
                           db="Geno")
    cursor = conn.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    info = cursor.fetchall()
    for row in info:
        print(row)


if __name__ == '__main__':
    getinfo()
