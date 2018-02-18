from sqlalchemy import Table, Column, MetaData, ForeignKey
from sqlalchemy.types import Text, Integer, String, TIMESTAMP, SMALLINT, DATE
from newsresearch.db_models.tables import BaseModel

class Posts(BaseModel):

    def __init__(self, metadata, innerschema):
        self.table = Table('posts', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('title', String(255), nulleable=False),
                     Column('body', Text, nulleable=False),
                     Column('publication_date', DATE ),
                     Column('link_id', Integer, nulleable=False),
                     Column('category_id', Integer, nulleable=False),
                     Column('author_id', Integer, nulleable=False),
                     schema=innerschema)
