from app import db
from app.model.dosen import Dosen

class Mahasiswa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nim = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    first_lecturer = db.Column(db.BigInteger, db.ForeignKey(Dosen.id, ondelete='CASCADE'))
    second_lecturer = db.Column(db.BigInteger, db.ForeignKey(Dosen.id, ondelete='CASCADE'))
    
    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.name)
    
    def formatArray(listData):
        array = []
        for data in listData:
            dosen = {
            'id': data.id,
            'nim': data.nim,
            'name': data.name,
            'phone': data.phone,
            'address': data.address
            }
            array.append(dosen)
        
        return array

    def formatObject(data):
        return {
            'id': data.id,
            'nim': data.nim,
            'name': data.name,
            'phone': data.phone,
            'address': data.address
        }