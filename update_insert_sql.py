import mysql
from mysql.connector import Error

def test_connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='fantasy-iditarod.com',
                                        database='lexidela_iditarod_code_test',
                                        user='lexidela_caps',
                                        password='password123') #password='ezu40B48lE'
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()

def start_race(musher_list):
    try:
        conn = mysql.connector.MySQLConnection(host='fantasy-iditarod.com',
                                        database='lexidela_iditarod_code_test',
                                        user='lexidela_caps',
                                        password='password123')

        cnx = conn.cursor()
        query = (
            "insert into stats(mush_id, num_dogs, tot_points, rank, rookie) " \
            "values(%s, %s, 0, 0, %s)"
        )
        for mush in musher_list:
            print(mush.name, mush.mush_id, mush.num_dogs, mush.is_rookie)
            cnx.execute(query, (mush.mush_id, mush.num_dogs, mush.is_rookie))
    except Error as e:
        print(e)

    finally:
        conn.close()

def update_race(musher_list):
    try:
        conn = mysql.connector.connect(host='fantasy-iditarod.com',
                                        database='lexidela_iditarod_code_test',
                                        user='lexidela_caps',
                                        password='password123')

        cnx = conn.cursor()
        query = (
            "update stats set num_dogs=%s, tot_points=tot_points+%s, rank=%s "
            "where mush_id = %s"
        )
        for mush in musher_list:
            cnx.execute(query, (mush.get_stats()))
    except Error as e:
        raise e

    finally:
        conn.close()

if __name__ == '__main__':
    test_connect()