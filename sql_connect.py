import mysql.connector


def db_connection_insert(string):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='12451245',
            database='fantasy'
        )
        with connection.cursor() as mycursor:
            mycursor.execute(string)
            connection.commit()
            print('данные успешно записаны')
    except Exception as ex:
        print('Ошибка ', ex)


def db_connection_select(string):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='12451245',
            database='fantasy'
        )
        with connection.cursor() as mycursor:
            mycursor.execute(string)
            result = mycursor.fetchall()
            for x in result:
                return x
    except Exception as ex:
        print('Ошибка ', ex)


def db_connection_select_tuple(string):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='12451245',
            database='fantasy'
        )
        with connection.cursor() as mycursor:
            mycursor.execute(string)
            result = mycursor.fetchall()
            return result
    except Exception as ex:
        print('Ошибка ', ex)
