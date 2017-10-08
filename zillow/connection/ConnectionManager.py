import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ConnectionManager:

    def __init__(self, username, password, host, port, database):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.conn = None

    def get_connection(self):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(self.username, self.password, self.host, self.port, self.database)
        self.conn = sqlalchemy.create_engine(url, client_encoding='utf8')
        return self.conn


class SessionManager:
    def get_session(self,conn):
        Session = sessionmaker(bind = conn)
        session = Session()
        return session
