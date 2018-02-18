from sqlalchemy import Table, Column, MetaData, ForeignKey
from sqlalchemy.types import Text, Integer, String, TIMESTAMP, SMALLINT


class Links(object):
    @staticmethod
    def get_table(self, metadata, innerschema):
        return Table('links', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('link', Text),
                     Column('is_post', SMALLINT),
                     Column('date_analyzed', TIMESTAMP),
                     schema=innerschema)

