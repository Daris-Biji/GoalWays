import jwt
from datetime import datetime, timedelta, timezone
from typing import Optional


SECRET_KEY = "Nikita Stenin"
ALGORITHM = "HS256"

def create_token(data:dict,expires_delta:Optional[timedelta] = None)->str:
    """
    Создает JWT токен
    1. Копируем данные
    2. Добавляем exp (время истечения)
    3. jwt.encode(данные, ключ, алгоритм) -> токен
    """

    copy_of_our_dict = data.copy() # создаем копию нашего словаря с данными
    
    if expires_delta:
        expire = datetime.now(timezone.utc)+ expires_delta    
        """
        время сейчас + столько сколько указали в expires_delta
        """
    else:
          expire = datetime.now(timezone.utc) + timedelta(minutes=15)
          """
          если время не прописано при создании токена то он дейсвтует 15 минут от 
            время сейчас + 15 минут
        """
    copy_of_our_dict.update({"exp":expire})
    token = jwt.encode(copy_of_our_dict,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_token(token:str):
     try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
     except jwt.ExpiredSignatureError:
        print("Токен истек")
        return None
     except jwt.InvalidTokenError:
        print("Невалидный токен")
        return None
     
if __name__=="__main__":
    userData = {
        "user_id": 123, 
        "username": "john"
    }
    time = timedelta(minutes=15)
    token = create_token(userData, time)





    



