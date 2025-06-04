import pandas as pd

from fastapi import Depends, FastAPI

from .database import SessionLocal
from .model_proba import get_mode_list, predict
from .user_create import create_user

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


def get_mode():
    return get_mode_list


@app.get("/rec")
def get_test_recommend(gender: int,age: int, country: str, city: str, os_name: str, top_k: int = 20, mode_list=Depends(get_mode_list)):
    user = create_user(gender, age, country, city, os_name)
    print(user.head())

    ans = predict(list_model=mode_list, top_k=top_k, user = user)

    df_post_data = pd.read_csv("date/post_dataset", index_col=0)

    df_user_data = []
    for post_id, _ in ans:
        df_user_data.append(df_post_data.loc[post_id]["text"])

    return df_user_data
