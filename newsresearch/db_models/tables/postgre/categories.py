from sqlalchemy import Table, Column, MetaData, ForeignKey
from sqlalchemy.types import Text, Integer, String, TIMESTAMP, SMALLINT


class Categories(object):
    @staticmethod
    def get_table(self, metadata, innerschema):
        return Table('categories', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('catname', String(255)),
                     schema=innerschema)

