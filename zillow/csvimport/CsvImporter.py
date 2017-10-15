import pandas as pd
from connection.ConnectionManager import SessionManager,ConnectionManager
#
#

class DataImporter():
    #def import_region(self):
    #    df = pd.read_csv("/Users/lakshmichaudhari/Documents/djangoproject/zillow/City_MedianRentalPrice_2Bedroom.csv")
    #    conn = ConnectionManager('lakshmi', 'metallica', 'localhost', 5432,'zdata').get_connection()
    #    session_manager = SessionManager()
    #    session = session_manager.get_session(conn)

    #    for index, row in df.iterrows():
    #        r = Region(region_name = row['RegionName'],state = row['State'],metro =row['Metro'],county=row['CountyName'])
    #        session.add(r)

    #    session.commit()
    def import_region_rent(self):
        from models.Region import Region
        from models.MedianRent import MedianRent

        df = pd.read_csv("/Users/lakshmichaudhari/Documents/djangoproject/zillow/City_MedianRentalPrice_2Bedroom.csv")
        df.fillna(0)
        header_list = list(df.columns.values)[5:]
        #yyyymm_list =[d.replace('-','') for d in header_list]
        #l = len(yyyymm_list)
        l1 = len(header_list)
        conn = ConnectionManager('lakshmi', 'metallica', 'localhost', 5432,'zdata').get_connection()
        session_manager = SessionManager()
        session = session_manager.get_session(conn)

        for index, row in df.iterrows():
            r = Region(region_name = row['RegionName'],state = row['State'],metro =row['Metro'],county=row['CountyName'])
            for d in header_list:
                r.rents.extend(MedianRent(yyyymm = d.replace('-',''),medianrent = row[d]))
            session.add(r)
            session.commit()
