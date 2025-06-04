import pickle
import pandas as pd
import numpy as np
from model.clear_date import clear_post_data


def get_mode_list():
    list_model = []
    for i in range(1, 3 + 1):
        with open(f"model/{i}_model.pkl", "rb") as f:
            list_model.append(pickle.load(f))

    return list_model


def predict(list_model, top_k: int, user):

    df_post_data = pd.read_csv("date/post_dataset")
    X = pd.read_csv("date/X")
    X = X.drop(["Unnamed: 0"], axis=1)

    df_post_data_1 = clear_post_data(df_post_data)

    p = df_post_data_1.reset_index()
    users_block = pd.concat([user] * len(p), ignore_index=True)
    X_cand = pd.concat(
        [users_block.reset_index(drop=True), p.reset_index(drop=True)], axis=1
    )
    X_cand = X_cand[X.columns]


    list_proba = []

    for model in list_model:
        list_proba.append(model.predict_proba(X_cand)[:, 1])

    print(list_proba)

    avg = sum(list_proba) / len(list_proba)
    top_idx = np.argsort(avg)[::-1][:top_k]

    return list(zip(p.loc[top_idx, "id"], avg[top_idx]))
