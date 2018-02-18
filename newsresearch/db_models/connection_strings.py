class ConnectionStrings(object):
    user = "fernando"
    password = "fernando"
    host = "localhost"
    db = "news_research"

    @staticmethod
    def get_postgreconnstring(self):
        return "postgresql://"+self.user+":"
            +self.password+"@"
            +self.host+"/"
            +self.db
