from time import gmtime, strftime


class PostgreHelpers(object):
    @staticmethod
    def get_timestamp(self):
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())
