import mysql
from mysql.connector import Error

def test_connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(database='lexidela_lexidela_iditarod_code_test',
                                        user='lexidela',
                                        password='23march1996')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()

def start_race(musher_list):
    try:
        conn = mysql.connector.connect(database='lexidela_lexidela_iditarod_code_test',
                                            user='lexidela',
                                            password='23march1996')

        cnx = conn.cursor()
        query = (
            "insert into stats mush_id, num_dogs, tot_points, rank, rookie "
            "values (%s, %s, 0, 0, %s )"
        )
        for mush in musher_list:
            cnx.execute(query, (mush.init_stats()))
    except Error as e:
        raise e

    finally:
        conn.close()

def update_race(musher_list):
    try:
        conn = mysql.connector.connect(database='lexidela_lexidela_iditarod_code_test',
                                            user='lexidela',
                                            password='23march1996')

        cnx = conn.cursor()
        query = (
            "update stats set num_dogs = %s, tot_points = %s, rank=%s "
            "where mush_id = %s "
        )
        for mush in musher_list:
            cnx.execute(query, (mush.get_stats()))
    except Error as e:
        raise e

    finally:
        conn.close()

if __name__ == '__main__':
    test_connect()