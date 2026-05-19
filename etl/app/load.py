import psycopg2
from psycopg2 import errors


DB_CONFIG = {
    "host": "db",
    "database": "market_data_db",
    "user": "postgres",
    "password": "ashish",
    "port": 5432
}


def load_market_data(records):

    connection = None

    try:

        connection = psycopg2.connect(**DB_CONFIG)

        cursor = connection.cursor()

        insert_query = """
            INSERT INTO market_data (
                instrument_id,
                price,
                volume,
                timestamp
            )
            VALUES (%s, %s, %s, %s)
        """

        inserted_count = 0

        duplicate_count = 0

        for record in records:

            try:

                cursor.execute(
                    insert_query,
                    (
                        record.instrument_id,
                        record.price,
                        record.volume,
                        record.timestamp
                    )
                )

                inserted_count += 1

            except errors.UniqueViolation:

                connection.rollback()

                duplicate_count += 1

        connection.commit()

        print(f"\nInserted Records: {inserted_count}")

        print(f"Duplicate Records Skipped: {duplicate_count}")

    except Exception as error:

        print(f"Database error: {error}")

    finally:

        if connection:

            cursor.close()

            connection.close()