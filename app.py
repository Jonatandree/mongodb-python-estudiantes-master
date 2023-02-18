from classes import Estudiante
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("Uayeb 3","Caballero","31487539")
    estudiante.save()
    
if __name__ == "__main__":
    load_dotenv()
    main()




