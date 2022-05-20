from typing import Dict


from .base import BaseDBConnector
from .errors import DBConnectionError


class PostgresConnector(BaseDBConnector):
    """
    Connects to a Postgres database for reading and writing data.
    """

    name = "Postgres Connector"
    sql_params_output = "pyformat"

    def __init__(self, config, **options):
        super().__init__(config, **options)

    def _create_connection(self, database: Dict[str, str]):
        """
        Create database connection to the Postgres database
        :param database: Dict with database connection settings

        :return: Connection object
        """

        import psycopg2
        try:
            conn = psycopg2.connect(**database)
        except Exception:
            raise DBConnectionError()

        return conn

    def _get_cursor(self, conn):
        import psycopg2.extras
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return cur
