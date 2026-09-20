from database.db import get_connection

class UserModel:

    @staticmethod
    def create_user(username,email,password):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO users
            (username,email,password)
            VALUES(?,?,?)
            """,
            (username,email,password)
        )

        conn.commit()
        conn.close()