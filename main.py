from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get('/user')
async def info(username: str = 'Lilo', age: int = 37) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8005)