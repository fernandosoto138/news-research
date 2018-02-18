from sqlalchemy import Table, Column, MetaData, ForeignKey
from sqlalchemy.types import Text, Integer, String, TIMESTAMP, SMALLINT
from newsresearch.db_models.tables import BaseModel

class Categories(BaseModel):

    def __init__(self, metadata, innerschema):
        self.table = Table('categories', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('catname', String(255)),
                     schema=innerschema)

