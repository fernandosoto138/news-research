class BaseModel(object):
    table = None

    def get_table(self):
        return table