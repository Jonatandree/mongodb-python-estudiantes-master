from classes.DbMongo import DbMongo

class Estudiante:

    def __init__(self, nombre, apellido, telefono, id=""):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__id = id
        self.__collection = "PorEgresar"
        

    def save(self, db):
        cliente, db = DbMongo.getDB()
        collection = db["PorEgresar"]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id
        
    def update(self, db):
        client, db = DbMongo.getDB()
        collection = db["PorEgresar"]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )
        print("hola de update")



