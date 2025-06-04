import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sqlalchemy import create_engine


def clear_user_data(df_user_data):
    df_user_data_1 = pd.get_dummies(df_user_data, columns=["country", "city", "os"])
    df_user_data_1 = df_user_data_1.drop(["source"], axis=1)
    df_user_data_1 = df_user_data_1.set_index("user_id")
    df_user_data_1 = df_user_data_1.drop(["Unnamed: 0"], axis = 1)
    df_user_data_1 = df_user_data_1.drop(["exp_group"], axis = 1)
    df_user_data_1 = df_user_data_1.dropna()
    return df_user_data_1


def clear_post_data(df_post_data):

    df_post_data_1 = df_post_data.copy()
    df_post_data_1 = df_post_data_1.set_index("id")

    vectorizer = TfidfVectorizer()
    vect = vectorizer.fit_transform(df_post_data["text"])
    tfidf_sums = vect.sum(axis=1)
    df_post_data_1["tfidf_sum"] = np.array(tfidf_sums).flatten()

    df_post_data_1 = pd.get_dummies(df_post_data_1, columns=["topic"])
    df_post_data_1 = df_post_data_1.drop(["text"], axis=1)

    N = len(df_post_data_1)
    noise = np.random.normal(loc=0.0, scale=20.0, size=N)
    df_post_data_1["tfidf_sum_noisy"] = df_post_data_1["tfidf_sum"] + noise

    df_post_data_1 = df_post_data_1.drop(["Unnamed: 0"], axis = 1)
    df_post_data_1 = df_post_data_1.dropna()

    return df_post_data_1


def batch_load_sql(query: str) -> pd.DataFrame:
    CHUNKSIZE = 20000
    engine = create_engine(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"
    )
    conn = engine.connect().execution_options(stream_results=True)
    chunks = []
    for chunk_dataframe in pd.read_sql(query, conn, chunksize=CHUNKSIZE):
        chunks.append(chunk_dataframe)
    conn.close()
    return pd.concat(chunks, ignore_index=True)
