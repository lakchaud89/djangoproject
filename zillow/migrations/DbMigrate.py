import sqlalchemy
from connection.ConnectionManager import ConnectionManager

from models.Region import Region
from models.MedianRent import MedianRent

class CreateTables():

    def __init__(self, database_name):
        self.database_name = database_name

    def migrate(self):
        conn = ConnectionManager('lakshmi', 'metallica', 'localhost', 5432, self.database_name).get_connection()

        for m in [Region, MedianRent]:
            m.metadata.create_all(conn)
