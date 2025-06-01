from model.clear_date import batch_load_sql


df_user_data = batch_load_sql(
    "SELECT * FROM user_data WHERE user_id >= 20000 and user_id <= 30000 LIMIT 10000"
)
df_post_data = batch_load_sql("SELECT * FROM post LIMIT 10000")


df_user_data.to_csv("date/user_dataset")
df_post_data.to_csv("date/post_dataset")
