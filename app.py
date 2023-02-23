import pymongo
from classes import Estudiante, DbMongo
from dotenv import load_dotenv


def main():

    client,db = DbMongo.getDB()

    #estudiante1 = Estudiante ("jonatn", "tradeo", "343")
    estudiante2 = Estudiante ("pitagoras", "tradeo", "555")
    estudiante2.save(db)
    #estudiante1.save(db)    

    #estudiante1.nombre = "atenancio"
    #estudiante2.nombre = "aparicio"

    #estudiante1.update(db)
    estudiante2.update(db)

    
   

    



if __name__ == "__main__":
    load_dotenv()
    main()



#collection.insert_one({ "nombre": "Ixchel", "telefono": "eeee" })

#for document in collection.find():
    #print(document)

