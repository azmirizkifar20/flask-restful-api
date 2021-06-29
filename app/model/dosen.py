from app import db

class Dosen(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nidn = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    
    def __repr__(self) -> str:
        return '<Dosen {}>'.format(self.name)