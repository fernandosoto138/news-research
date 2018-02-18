from sqlalchemy import Table, Column, MetaData, ForeignKey
from sqlalchemy.types import Text, Integer, String, TIMESTAMP, SMALLINT
from newsresearch.db_models.tables import BaseModel

class Links(BaseModel):

    def __init__(self, metadata, innerschema):
        self.table = Table('links', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('link', Text),
                     Column('is_post', SMALLINT),
                     Column('date_analyzed', TIMESTAMP),
                     schema=innerschema)