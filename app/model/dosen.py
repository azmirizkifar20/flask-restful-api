from app import db

class Dosen(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nidn = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Dosen {}>'.format(self.name)

    def formatArray(listData):
        array = []
        for data in listData:
            dosen = {
            'id': data.id,
            'nidn': data.nidn,
            'name': data.name,
            'phone': data.phone,
            'address': data.address
            }
            array.append(dosen)
        
        return array

    def formatObject(data):
        return {
            'id': data.id,
            'nidn': data.nidn,
            'name': data.name,
            'phone': data.phone,
            'address': data.address
        }