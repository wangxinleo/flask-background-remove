from app import sqlalchemy


class dbKey(sqlalchemy.Model):
    __tablename__ = 'UG_KEYBOX'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    Rkey = sqlalchemy.Column(sqlalchemy.String(32), unique=True)
    num = sqlalchemy.Column(sqlalchemy.Integer)

    def __init__(self, Rkey, num):
        self.Rkey = Rkey
        self.num = num

    def __repr__(self):
        return '%r:%r' %(self.Rkey, self.num)


class dbMac(sqlalchemy.Model):
    __tablename__ = 'UG_MACBOX'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    userMac = sqlalchemy.Column(sqlalchemy.String(32), unique=True)

