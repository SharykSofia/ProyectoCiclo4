from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo")
def root():
    return {
        "Message": "Hola Mision TIC 2022"
        }

#@app.get("/usuarios/{user_id}")
#def read_user(user_id: int):
#    return {
#        "user_id": user_id
#        }

#cursos = [
#    {"Cursos": "Fundamentos de programación"},
#    {"Cursos": "Programacion Basica"},
#    {"Cursos": "Desarrollo de software"},
#    {"Cursos": "Desarrollo Apps web"}
#  ]

#@app.get("/cursos")
#def read_item(skip: int = 0, limit: int = 10):
#    return cursos [skip: skip + limit]