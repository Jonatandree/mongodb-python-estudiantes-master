import pymongo
from classes import Estudiante


def main():
    
    user = "AndreeVasquez"
    password = "cocorasta"
    cluster ="cluster0.hfac6vs.mongodb.net"
    query_string = "retryWrites=true&w=majority"

    ## Connection String
    uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
        user
        , password
        , cluster
        , query_string
    )

    client = pymongo.MongoClient(uri)
    db = client['unah']
    collection = db['estudiante']
    estudiante = Estudiante("andree","vasquez","31487539")
    print(estudiante.__dict__)
    collection.insert_one( estudiante.__dict__ )

if __name__ == "__main__":
    main()



#collection.insert_one({ "nombre": "Ixchel", "telefono": "eeee" })

#for document in collection.find():
    #print(document)

