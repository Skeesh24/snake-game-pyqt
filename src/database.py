from os.path import join
from sqlite3 import connect
from sqlite3.dbapi2 import IntegrityError

DB_PATH = join("db", "leaderboard.db")
CREATE_SCHEMA = """
    CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY,
        player TEXT UNIQUE NOT NULL,
        score INTEGER NOT NULL
    )
"""
GET_LEADERBOARD = (
    "SELECT player, score FROM leaderboard GROUP BY player ORDER BY score DESC"
)
ADD_SCORE = "INSERT INTO leaderboard (player, score) VALUES (?, ?)"
UPDATE_SCORE = """
    UPDATE leaderboard 
    SET score = ? 
    WHERE player = (
        SELECT player FROM leaderboard WHERE player = ? AND score < ?
    )
"""


def init_database():
    with connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_SCHEMA)
        cursor.close()
        conn.commit()


def get_leaderboard_data():
    with connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(GET_LEADERBOARD)
        leaderboard_data = cursor.fetchall()
        cursor.close()
        return leaderboard_data


def add_to_leaderboard(player, score):
    with connect(DB_PATH) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                ADD_SCORE,
                (player, score),
            )
        except IntegrityError:
            cursor.execute(UPDATE_SCORE, (score, player, score))
        cursor.close()
        conn.commit()


def select_all():
    with connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leaderboard")
        leaderboard_data = cursor.fetchall()
        cursor.close()
        return leaderboard_data
