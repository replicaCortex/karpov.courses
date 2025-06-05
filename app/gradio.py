import gradio as gr
import pandas as pd
from model_proba import predict, get_mode_list
from user_create import create_user
from model.clear_date import batch_load_sql

def _swap_colums(column1, column2, df):
    cols = list(df.columns)
    i, j = cols.index(column1), cols.index(column2)
    cols[i], cols[j] = cols[j], cols[i]
    df = df[cols]
    return df

def main(Name, gender, age,country,city, os_name, top_k: int =  200):
    _ = Name 
    mode_list = get_mode_list()

    if gender == "Male":
        gender = 1
    else:
        gender = 0

    user = create_user(gender, age, country, city, os_name)
    print(user.head())

    ans, proba = predict(list_model=mode_list, top_k=top_k, user = user)

    placeholders = ','.join(map(str, ans))
    df_post_data = batch_load_sql(f"SELECT * FROM post WHERE id IN ({placeholders})")

    df_post_data['id'] = df_post_data['id'].astype(int)
    df_post_data['id'] = pd.Categorical(df_post_data['id'], categories=ans, ordered=True)
    df_post_data = df_post_data.sort_values('id')

    df_post_data["proba"] = proba[:len(df_post_data)]

    df_post_data = _swap_colums("text", "proba", df_post_data)
    df_post_data = _swap_colums("text", "topic", df_post_data)


    return df_post_data

demo = gr.Interface(
    main,
    [
        "text",
        gr.Radio(["Male", "Female"], label = "Gender"),
        gr.Slider(18, 100, label = "Age", randomize = True, step = 1),
        # "number",
        gr.Dropdown(['Azerbaijan', 'Belarus', 'Cyprus', 'Estonia', 'Finland', 'Kazakhstan', 'Latvia', 'Russia', 'Switzerland', 'Turkey', 'Ukraine'], label = "Country"),
        gr.Dropdown(['Abakan', 'Abaza', 'Abdulino', 'Abinsk', 'Achinsk', 'Achkhoy-Martan', 'Adana', 'Adygeysk', 'Adıyaman', 'Afanasyevo', 'Aglobi', 'Agryz', 'Agvali', 'Akhtubinsk', 'Akhty', 'Aksay', 'Alagir', 'Alakurtti', 'Alapayevsk', 'Alchevsk', 'Aldan', 'Aleksandrov', 'Aleksandrovka', 'Alekseyevka', 'Aleksin', 'Aleysk', 'Alkhazurovo', 'Alleroy', 'Almak', 'Almaty', 'Almetyevsk', 'Alzamay', 'Al’mukhametovo', 'Amursk', 'Anadyr', 'Anapa', 'Andreapol', 'Angarsk', 'Aniskino', 'Ankara', 'Antalya', 'Antipovka', 'Antratsyt', 'Anzhero-Sudzhensk', 'Apatity', 'Apostolove', 'Apsheronsk', 'Aqsū', 'Aqtaū', 'Aqtöbe', 'Aral'], label = "City"),
        gr.Radio(["Android", "iOS"], label = "Platform"),
    ],
    "dataframe",
    examples=[
        ["Mr. Freak","Male", 19, "Russia", "Abakan", "Android"],
        ["Mrs. Freak","Female", 22, "Latvia","Abinsk", "iOS"],
    ]
)

if __name__ == "__main__":
    
    demo.launch()
