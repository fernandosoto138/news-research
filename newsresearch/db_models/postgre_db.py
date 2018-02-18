from sqlalchemy import create_engine
from sqlalchemy import MetaData
from .connection_strings import ConnectionStrings 


class PostgreDB(object):
    @staticmethod
    def CreateConnection():
        ''' Returns a tuple with (Engine, Connection, Metadata)
        '''
        cs = ConnectionStrings()
        engine = create_engine(cs.get_postgreconnstring(), echo=True)
        conn = engine.connect()
        metadata = MetaData()
        return (engine, conn, metadata)
