import pickle
import pandas as pd
import numpy as np
from model.clear_date import clear_post_data, batch_load_sql

def get_mode_list():
    list_model = []
    for i in range(1, 3 + 1):
        with open(f"model/{i}_model.pkl", "rb") as f:
            list_model.append(pickle.load(f))

    return list_model


def predict(list_model, top_k: int, user):
    df_post_data = batch_load_sql("SELECT * FROM post LIMIT 10000")
    X = pd.read_csv("date/X").drop(["Unnamed: 0"], axis=1)

    df_post_data_1 = clear_post_data(df_post_data)
    post = df_post_data_1.reset_index(drop=True)
    print(post.head())
    users_block = pd.concat([user] * len(post), ignore_index=True)
    X_cand = pd.concat([users_block.reset_index(drop=True),
                        post.reset_index(drop=True)], axis=1)
    X_cand = X_cand[X.columns]

    proba_list = []
    for model in list_model:
        proba = model.predict_proba(X_cand)[:, 1]
        proba_list.append(proba)

    proba_matrix = np.vstack(proba_list)
    avg_proba = proba_matrix.mean(axis=0)

    top_indices = np.argsort(avg_proba)[::-1][:top_k]
    print(top_indices)

    top_probs = avg_proba[top_indices]
    print(top_probs)

    return top_indices.tolist(), top_probs
