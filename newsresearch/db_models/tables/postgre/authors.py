from sqlalchemy import Table, Column, MetaData, ForeignKey
from sqlalchemy.types import Text, Integer, String, TIMESTAMP, SMALLINT


class Authors(object):
    @staticmethod
    def get_table(self, metadata, innerschema):
        return Table('authors', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('fullname', String(255)),
                     schema=innerschema)

