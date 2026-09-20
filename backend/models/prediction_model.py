from database.db import get_connection

class PredictionModel:

    @staticmethod
    def save_prediction(
        animal,
        confidence,
        image_path
    ):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO predictions
            (
            animal_name,
            confidence,
            image_path
            )
            VALUES(?,?,?)
            """,
            (
                animal,
                confidence,
                image_path
            )
        )

        conn.commit()
        conn.close()