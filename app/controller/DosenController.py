from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa

from app import response, db
from flask import request

# get all data
def index():
    try:
        listData = []
        getAll = Dosen.query.all()
        
        for data in getAll:
            dosen = {
                'id': data.id,
                'nidn': data.nidn,
                'name': data.name,
                'phone': data.phone,
                'address': data.address
            }
            listData.append(dosen)
        
        return response.success(listData, 'Success')
    except Exception as e:
        print(e)


# get detail
def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter(
                        (Mahasiswa.first_lecturer == id) | 
                        (Mahasiswa.second_lecturer == id))
        
        if not dosen:
            return response.badRequest([], 'Tidak ada data dosen')
        
        dataMahasiswa = formatMahasiswa(mahasiswa)
        data = {
            'id': dosen.id,
            'nidn': dosen.nidn,
            'name': dosen.name,
            'phone': dosen.phone,
            'address': dosen.address,
            'mahasiswa': dataMahasiswa
        }
        
        return response.success(data, 'Success')
    except Exception as e:
        print(e)

def formatMahasiswa(datas):
    array = []
    for data in datas:
        mhs = {
            'id': data.id,
            'nim': data.nim,
            'name': data.name,
            'phone': data.phone,
            'address': data.address
        }
        array.append(mhs)
    
    return array

# add data
def save():
    try:
        # if using form data
        nidn = request.form.get('nidn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        
        # if using raw data
        # rawData = json.loads(request.get_data())
        # nidn = rawData['nidn']
        # name = rawData['name']
        # phone = rawData['phone']
        # address = rawData['address']
        
        dosen = Dosen(nidn=nidn, name=name, phone=phone, address=address)
        print(dosen)
        
        # push data
        db.session.add(dosen)
        db.session.commit()
        
        return response.success('', "success to add lecture data!")
    except Exception as e:
        print(e)

# update data
def update(lectureId):
    try:
        # if using form data
        nidn = request.form.get('nidn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        
        input = [
            {
                'nidn': nidn,
                'name': name,
                'phone': phone,
                'address': address
            }
        ]
        
        # get data
        getById = Dosen.query.filter_by(id=lectureId).first()
        
        # set data
        getById.nidn = nidn
        getById.name = name
        getById.phone = phone
        getById.address = address
        
        # commit
        db.session.commit()
        
        return response.success(input, "Sucess to update data")
    except Exception as e:
        print(e)

# delete data
def delete(lectureId):
    try:
        # get data
        getById = Dosen.query.filter_by(id=lectureId).first()
        
        if not getById:
            return response.badRequest([], "The data is invalid")
        
        # delete data
        db.session.delete(getById)
        db.session.commit()
        
        return response.success("", "Sucess to delete data")
    except Exception as e:
        print(e)