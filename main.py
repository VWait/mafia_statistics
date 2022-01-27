import sqlite3


class DBWriter:
    def __init__(self, db_name):
        self.db_name = db_name

    def execute_request_and_get_value(self, request):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        value = cur.execute(request)
        con.commit()
        con.close()
        return value

    def add_player(self, nickname):
        self.execute_request_and_get_value(f"INSERT INTO Players(nickname) VALUES('{nickname}')")

    def save_game(self, tournament, stage, date, table, number, type_game, referee):
        pass


writer = DBWriter('seasonRating.db')
