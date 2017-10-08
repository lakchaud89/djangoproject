import pandas as pd
from connection.ConnectionManager import SessionManager,ConnectionManager
from models.Region import Region

class CsvImporter():
    def import_region(self):
        df = pd.read_csv("/Users/lakshmichaudhari/Documents/djangoproject/zillow/City_MedianRentalPrice_2Bedroom.csv")
        conn = ConnectionManager('lakshmi', 'metallica', 'localhost', 5432,'zdata').get_connection()
        session_manager = SessionManager()
        session = session_manager.get_session(conn)

        for index, row in df.iterrows():
            r = Region(region_name = row['RegionName'],state = row['State'],metro =row['Metro'],county=row['CountyName'])
            session.add(r)

        session.commit()
