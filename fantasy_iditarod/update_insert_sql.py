import mysql
from mysql.connector import Error

def test_connect():
    '''Connect to MySQL database'''
    connected = False
    try:
        conn = mysql.connector.connect(host='fantasy-iditarod.com',
                                        database='lexidela_iditarod',
                                        user='lexidela_caps',
                                        password='password123')
        if conn.is_connected():
            connected = True

    except Error as e:
        print(e)

    finally:
        conn.close()
        return connected

def start_race(musher_list):
    '''Initialize database values'''
    try:
        conn = mysql.connector.MySQLConnection(host='fantasy-iditarod.com',
                                        database='lexidela_iditarod',
                                        user='lexidela_caps',
                                        password='password123')

        cnx = conn.cursor()
        query = (
            "insert into stats(mush_id, num_dogs, tot_points, rank, rookie, checkpoint) " \
            "values(%s, %s, 0, 0, %s, %s)"
        )
        for mush in musher_list:
            cnx.execute(query, (mush.mush_id, mush.num_dogs, mush.is_rookie, mush.checkpoint))
    except Error as e:
        print(e)

    finally:
        conn.close()

def update_race(musher_list):
    '''Go through a list of musher objects and update table'''
    try:
        conn = mysql.connector.connect(host='fantasy-iditarod.com',
                                        database='lexidela_iditarod',
                                        user='lexidela_caps',
                                        password='password123')

        cnx = conn.cursor()
        query = (
            "update stats set num_dogs=%s, tot_points=tot_points+%s, rank=%s, checkpoint=%s "
            "where mush_id = %s and checkpoint !=%s"
        )
        for mush in musher_list:
            cnx.execute(query, (mush.num_dogs, mush.total_points, mush.pos, mush.checkpoint, mush.mush_id, mush.checkpoint))
    except Error as e:
        raise e

    finally:
        conn.close()

def clear_table():
    '''Clear the table when finished'''
    try:
        conn = mysql.connector.connect(host='fantasy-iditarod.com',
                                            database='lexidela_iditarod',
                                            user='lexidela_caps',
                                            password='password123')

        cnx = conn.cursor()
        query = (
            "delete from stats where mush_id in (select mush_id from stats)"
        )
        cnx.execute(query)
    except Error as e:
        raise e

    finally:
        conn.close()

if __name__ == '__main__':
    test_connect()