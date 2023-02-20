import pymongo
from classes import Estudiante, DbMongo
from dotenv import load_dotenv


def main():

    db = DbMongo.getDB()

    estudiante = Estudiante ("andree8", "vasquez", "34323434")
    estudiante.save()


if __name__ == "__main__":
    load_dotenv()
    main()



#collection.insert_one({ "nombre": "Ixchel", "telefono": "eeee" })

#for document in collection.find():
    #print(document)

