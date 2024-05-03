import pymysql.cursors

connection = pymysql.connect(host='172.20.128.79',
                            user='karsten',
                            password='123Akademiet',
                            database='BrukerRegister',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


