import pymongo
from classes import Estudiante, DbMongo


def main():

    db = DbMongo.getDB()
    collection = db['estudiante']


    estudiante = Estudiante("andree2","vasquez","31487539")
    print(estudiante.__dict__)
    collection.insert_one( estudiante.__dict__ )

if __name__ == "__main__":
    main()



#collection.insert_one({ "nombre": "Ixchel", "telefono": "eeee" })

#for document in collection.find():
    #print(document)

