import pandas as pd
from sqlalchemy import create_engine


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


df = batch_load_sql("SELECT * FROM user_data LIMIT 10")
print("---")
print(df.head())
