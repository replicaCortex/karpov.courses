```python
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
```


```python
df_user_data = batch_load_sql("SELECT * FROM user_data LIMIT 10000")
df_post_data = batch_load_sql("SELECT * FROM post LIMIT 10000")
df_feed_data = batch_load_sql("SELECT * FROM feed_data LIMIT 10000")
```


```python
df_user_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>gender</th>
      <th>age</th>
      <th>country</th>
      <th>city</th>
      <th>exp_group</th>
      <th>os</th>
      <th>source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>200</td>
      <td>1</td>
      <td>34</td>
      <td>Russia</td>
      <td>Degtyarsk</td>
      <td>3</td>
      <td>Android</td>
      <td>ads</td>
    </tr>
    <tr>
      <th>1</th>
      <td>201</td>
      <td>0</td>
      <td>37</td>
      <td>Russia</td>
      <td>Abakan</td>
      <td>0</td>
      <td>Android</td>
      <td>ads</td>
    </tr>
    <tr>
      <th>2</th>
      <td>202</td>
      <td>1</td>
      <td>17</td>
      <td>Russia</td>
      <td>Smolensk</td>
      <td>4</td>
      <td>Android</td>
      <td>ads</td>
    </tr>
    <tr>
      <th>3</th>
      <td>203</td>
      <td>0</td>
      <td>18</td>
      <td>Russia</td>
      <td>Moscow</td>
      <td>1</td>
      <td>iOS</td>
      <td>ads</td>
    </tr>
    <tr>
      <th>4</th>
      <td>204</td>
      <td>0</td>
      <td>36</td>
      <td>Russia</td>
      <td>Anzhero-Sudzhensk</td>
      <td>3</td>
      <td>Android</td>
      <td>ads</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9995</th>
      <td>10198</td>
      <td>1</td>
      <td>28</td>
      <td>Russia</td>
      <td>Orekhovo-Borisovo Yuzhnoye</td>
      <td>0</td>
      <td>Android</td>
      <td>ads</td>
    </tr>
    <tr>
      <th>9996</th>
      <td>10199</td>
      <td>0</td>
      <td>18</td>
      <td>Ukraine</td>
      <td>Simferopol</td>
      <td>4</td>
      <td>iOS</td>
      <td>ads</td>
    </tr>
    <tr>
      <th>9997</th>
      <td>10200</td>
      <td>1</td>
      <td>21</td>
      <td>Russia</td>
      <td>Moscow</td>
      <td>1</td>
      <td>Android</td>
      <td>ads</td>
    </tr>
    <tr>
      <th>9998</th>
      <td>10201</td>
      <td>1</td>
      <td>26</td>
      <td>Russia</td>
      <td>Minusinsk</td>
      <td>3</td>
      <td>Android</td>
      <td>ads</td>
    </tr>
    <tr>
      <th>9999</th>
      <td>10202</td>
      <td>1</td>
      <td>28</td>
      <td>Russia</td>
      <td>Kursk</td>
      <td>4</td>
      <td>iOS</td>
      <td>ads</td>
    </tr>
  </tbody>
</table>
<p>10000 rows × 8 columns</p>
</div>




```python
df_feed_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>user_id</th>
      <th>post_id</th>
      <th>action</th>
      <th>target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-12-29 11:56:22</td>
      <td>124844</td>
      <td>2338</td>
      <td>view</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-12-29 11:58:14</td>
      <td>124844</td>
      <td>2585</td>
      <td>view</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-12-29 12:00:36</td>
      <td>124844</td>
      <td>2927</td>
      <td>view</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2021-12-29 12:03:08</td>
      <td>124844</td>
      <td>3994</td>
      <td>view</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-12-29 12:03:44</td>
      <td>124844</td>
      <td>3439</td>
      <td>view</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9995</th>
      <td>2021-11-10 21:24:46</td>
      <td>30025</td>
      <td>7191</td>
      <td>view</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9996</th>
      <td>2021-11-11 10:12:22</td>
      <td>30025</td>
      <td>4253</td>
      <td>view</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9997</th>
      <td>2021-11-11 10:14:14</td>
      <td>30025</td>
      <td>1218</td>
      <td>view</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9998</th>
      <td>2021-11-11 10:15:06</td>
      <td>30025</td>
      <td>3630</td>
      <td>view</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9999</th>
      <td>2021-11-11 10:15:40</td>
      <td>30025</td>
      <td>645</td>
      <td>view</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>10000 rows × 5 columns</p>
</div>




```python
marge_df = pd.merge(df_feed_data, df_user_data, left_on="user_id", right_on = "user_id", how="left")
marge_df = pd.merge(marge_df, df_post_data, left_on="post_id", right_on = "id", how="left")
```


```python
marge_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>user_id</th>
      <th>post_id</th>
      <th>action</th>
      <th>target</th>
      <th>gender</th>
      <th>age</th>
      <th>country</th>
      <th>city</th>
      <th>exp_group</th>
      <th>os</th>
      <th>source</th>
      <th>id</th>
      <th>text</th>
      <th>topic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>309</th>
      <td>2021-10-24 19:12:37</td>
      <td>9235</td>
      <td>1732</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>1732</td>
      <td>SA return to Mauritius\n\nTop seeds South Afri...</td>
      <td>sport</td>
    </tr>
    <tr>
      <th>310</th>
      <td>2021-10-24 19:15:07</td>
      <td>9235</td>
      <td>7272</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>7272</td>
      <td>This is a prime example of uninhibited filmmak...</td>
      <td>movie</td>
    </tr>
    <tr>
      <th>311</th>
      <td>2021-10-24 19:17:33</td>
      <td>9235</td>
      <td>6444</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>6444</td>
      <td>An aging Roger Moore is back yet again as Bond...</td>
      <td>movie</td>
    </tr>
    <tr>
      <th>312</th>
      <td>2021-10-24 19:20:15</td>
      <td>9235</td>
      <td>3247</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>3247</td>
      <td>Hyderabad International Airport has reconfigur...</td>
      <td>covid</td>
    </tr>
    <tr>
      <th>313</th>
      <td>2021-10-24 19:23:10</td>
      <td>9235</td>
      <td>6720</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>6720</td>
      <td>This movie needs to come out on DVD cause that...</td>
      <td>movie</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9524</th>
      <td>2021-11-30 15:35:14</td>
      <td>9238</td>
      <td>1033</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>1033</td>
      <td>Conservative backing for ID cards\n\nThe Torie...</td>
      <td>politics</td>
    </tr>
    <tr>
      <th>9525</th>
      <td>2021-11-30 15:36:26</td>
      <td>9238</td>
      <td>3211</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>3211</td>
      <td>Terrifying how #Tories #IDS speak about #Benef...</td>
      <td>covid</td>
    </tr>
    <tr>
      <th>9526</th>
      <td>2021-11-30 15:39:20</td>
      <td>9238</td>
      <td>5444</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>5444</td>
      <td>The recent history of Hollywood remakes of gho...</td>
      <td>movie</td>
    </tr>
    <tr>
      <th>9527</th>
      <td>2021-11-30 15:40:56</td>
      <td>9238</td>
      <td>162</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>162</td>
      <td>Alfa Romeos to get GM engines\n\nFiat is to st...</td>
      <td>business</td>
    </tr>
    <tr>
      <th>9528</th>
      <td>2021-11-30 15:42:59</td>
      <td>9238</td>
      <td>3292</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>ads</td>
      <td>3292</td>
      <td>Dear VP @ProfOsinbajo, this fee proposed by @N...</td>
      <td>covid</td>
    </tr>
  </tbody>
</table>
<p>1774 rows × 15 columns</p>
</div>




```python
def summarize(DataFrame):
    summary = pd.DataFrame()
    
    # Data Type
    summary['Data Type'] = DataFrame.dtypes
    # The Number of Missing Values
    summary['# of NAs'] = DataFrame.isna().sum()
    # The Percentage of Missing Values
    summary['% of NAs'] = round((DataFrame.isna().sum() / DataFrame.shape[0]) * 100, 2)
    # The Number of Unique Values
    summary['# of Unique'] = DataFrame.apply(lambda x: x.nunique())
    # Max
    summary['Max'] = DataFrame.apply(lambda x: x.max() if pd.api.types.is_numeric_dtype(x) else '-')
    # Min
    summary['Min'] = DataFrame.apply(lambda x: x.min() if pd.api.types.is_numeric_dtype(x) else '-')
    
    # Measures of Central Tendency: Mean, Median, Mode 
    summary['Mean'] = DataFrame.apply(lambda x: round(x.mean(), 2) if pd.api.types.is_numeric_dtype(x) else '-')
    summary['Median'] = DataFrame.apply(lambda x: x.median() if pd.api.types.is_numeric_dtype(x) else '-')
    summary['Mode'] = DataFrame.apply(lambda x: x.mode().iloc[0] if not x.mode().empty else '-')
    
    # Measures of Dispersion: Range, Variance, Standard Deviation
    summary['Range'] = DataFrame.apply(lambda x: x.max() - x.min() if pd.api.types.is_numeric_dtype(x) else '-')
    summary['Variance'] = DataFrame.apply(lambda x: x.var() if pd.api.types.is_numeric_dtype(x) else '-')
    summary['Standard Deviation'] = DataFrame.apply(lambda x: x.std() if pd.api.types.is_numeric_dtype(x) else '-')
    
    # Measures of Shape: Skewness, Kurtosis
    summary['Skewness'] = DataFrame.apply(lambda x: round(x.skew(), 2) if pd.api.types.is_numeric_dtype(x) else '-')
    summary['Kurtosis'] = DataFrame.apply(lambda x: round(x.kurt(), 2) if pd.api.types.is_numeric_dtype(x) else '-')
    
    return summary


summary = summarize(marge_df)
summary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Data Type</th>
      <th># of NAs</th>
      <th>% of NAs</th>
      <th># of Unique</th>
      <th>Max</th>
      <th>Min</th>
      <th>Mean</th>
      <th>Median</th>
      <th>Mode</th>
      <th>Range</th>
      <th>Variance</th>
      <th>Standard Deviation</th>
      <th>Skewness</th>
      <th>Kurtosis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>timestamp</th>
      <td>datetime64[ns]</td>
      <td>0</td>
      <td>0.0</td>
      <td>1774</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>2021-10-05 11:38:48</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>user_id</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
      <td>4</td>
      <td>9238</td>
      <td>9235</td>
      <td>9236.38</td>
      <td>9236.0</td>
      <td>9235</td>
      <td>3</td>
      <td>1.422541</td>
      <td>1.192703</td>
      <td>0.17</td>
      <td>-1.49</td>
    </tr>
    <tr>
      <th>post_id</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
      <td>1402</td>
      <td>7315</td>
      <td>1</td>
      <td>3574.36</td>
      <td>3603.0</td>
      <td>5239</td>
      <td>7314</td>
      <td>4794373.898149</td>
      <td>2189.605877</td>
      <td>0.04</td>
      <td>-1.29</td>
    </tr>
    <tr>
      <th>action</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>view</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>target</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>0.11</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.098333</td>
      <td>0.313581</td>
      <td>2.49</td>
      <td>4.19</td>
    </tr>
    <tr>
      <th>gender</th>
      <td>float64</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.77</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.176277</td>
      <td>0.419854</td>
      <td>-1.3</td>
      <td>-0.32</td>
    </tr>
    <tr>
      <th>age</th>
      <td>float64</td>
      <td>0</td>
      <td>0.0</td>
      <td>3</td>
      <td>27.0</td>
      <td>20.0</td>
      <td>23.52</td>
      <td>23.0</td>
      <td>23.0</td>
      <td>7.0</td>
      <td>7.369971</td>
      <td>2.714769</td>
      <td>0.11</td>
      <td>-1.36</td>
    </tr>
    <tr>
      <th>country</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Russia</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>city</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>4</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Ulan-Ude</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>exp_group</th>
      <td>float64</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.99</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>1.000381</td>
      <td>1.00019</td>
      <td>0.03</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>os</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Android</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>source</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>ads</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>id</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
      <td>1402</td>
      <td>7315</td>
      <td>1</td>
      <td>3574.36</td>
      <td>3603.0</td>
      <td>5239</td>
      <td>7314</td>
      <td>4794373.898149</td>
      <td>2189.605877</td>
      <td>0.04</td>
      <td>-1.29</td>
    </tr>
    <tr>
      <th>text</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>1398</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>This film is terrible. I was really looking fo...</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>topic</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>7</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>movie</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
</div>




```python
marge_df = marge_df.dropna()
```


```python
summary = summarize(marge_df)
summary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Data Type</th>
      <th># of NAs</th>
      <th>% of NAs</th>
      <th># of Unique</th>
      <th>Max</th>
      <th>Min</th>
      <th>Mean</th>
      <th>Median</th>
      <th>Mode</th>
      <th>Range</th>
      <th>Variance</th>
      <th>Standard Deviation</th>
      <th>Skewness</th>
      <th>Kurtosis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>timestamp</th>
      <td>datetime64[ns]</td>
      <td>0</td>
      <td>0.0</td>
      <td>1774</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>2021-10-05 11:38:48</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>user_id</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
      <td>4</td>
      <td>9238</td>
      <td>9235</td>
      <td>9236.38</td>
      <td>9236.0</td>
      <td>9235</td>
      <td>3</td>
      <td>1.422541</td>
      <td>1.192703</td>
      <td>0.17</td>
      <td>-1.49</td>
    </tr>
    <tr>
      <th>post_id</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
      <td>1402</td>
      <td>7315</td>
      <td>1</td>
      <td>3574.36</td>
      <td>3603.0</td>
      <td>5239</td>
      <td>7314</td>
      <td>4794373.898149</td>
      <td>2189.605877</td>
      <td>0.04</td>
      <td>-1.29</td>
    </tr>
    <tr>
      <th>action</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>view</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>target</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>0.11</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.098333</td>
      <td>0.313581</td>
      <td>2.49</td>
      <td>4.19</td>
    </tr>
    <tr>
      <th>gender</th>
      <td>float64</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.77</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.176277</td>
      <td>0.419854</td>
      <td>-1.3</td>
      <td>-0.32</td>
    </tr>
    <tr>
      <th>age</th>
      <td>float64</td>
      <td>0</td>
      <td>0.0</td>
      <td>3</td>
      <td>27.0</td>
      <td>20.0</td>
      <td>23.52</td>
      <td>23.0</td>
      <td>23.0</td>
      <td>7.0</td>
      <td>7.369971</td>
      <td>2.714769</td>
      <td>0.11</td>
      <td>-1.36</td>
    </tr>
    <tr>
      <th>country</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Russia</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>city</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>4</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Ulan-Ude</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>exp_group</th>
      <td>float64</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.99</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>1.000381</td>
      <td>1.00019</td>
      <td>0.03</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>os</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>2</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>Android</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>source</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>1</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>ads</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>id</th>
      <td>int64</td>
      <td>0</td>
      <td>0.0</td>
      <td>1402</td>
      <td>7315</td>
      <td>1</td>
      <td>3574.36</td>
      <td>3603.0</td>
      <td>5239</td>
      <td>7314</td>
      <td>4794373.898149</td>
      <td>2189.605877</td>
      <td>0.04</td>
      <td>-1.29</td>
    </tr>
    <tr>
      <th>text</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>1398</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>This film is terrible. I was really looking fo...</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <th>topic</th>
      <td>object</td>
      <td>0</td>
      <td>0.0</td>
      <td>7</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>movie</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = marge_df.drop(['user_id', 'post_id', "id", 'source'], axis = 1)
```


```python
df 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>action</th>
      <th>target</th>
      <th>gender</th>
      <th>age</th>
      <th>country</th>
      <th>city</th>
      <th>exp_group</th>
      <th>os</th>
      <th>text</th>
      <th>topic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>309</th>
      <td>2021-10-24 19:12:37</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>SA return to Mauritius\n\nTop seeds South Afri...</td>
      <td>sport</td>
    </tr>
    <tr>
      <th>310</th>
      <td>2021-10-24 19:15:07</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>This is a prime example of uninhibited filmmak...</td>
      <td>movie</td>
    </tr>
    <tr>
      <th>311</th>
      <td>2021-10-24 19:17:33</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>An aging Roger Moore is back yet again as Bond...</td>
      <td>movie</td>
    </tr>
    <tr>
      <th>312</th>
      <td>2021-10-24 19:20:15</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>Hyderabad International Airport has reconfigur...</td>
      <td>covid</td>
    </tr>
    <tr>
      <th>313</th>
      <td>2021-10-24 19:23:10</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>27.0</td>
      <td>Russia</td>
      <td>Ulan-Ude</td>
      <td>0.0</td>
      <td>Android</td>
      <td>This movie needs to come out on DVD cause that...</td>
      <td>movie</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9524</th>
      <td>2021-11-30 15:35:14</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>Conservative backing for ID cards\n\nThe Torie...</td>
      <td>politics</td>
    </tr>
    <tr>
      <th>9525</th>
      <td>2021-11-30 15:36:26</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>Terrifying how #Tories #IDS speak about #Benef...</td>
      <td>covid</td>
    </tr>
    <tr>
      <th>9526</th>
      <td>2021-11-30 15:39:20</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>The recent history of Hollywood remakes of gho...</td>
      <td>movie</td>
    </tr>
    <tr>
      <th>9527</th>
      <td>2021-11-30 15:40:56</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>Alfa Romeos to get GM engines\n\nFiat is to st...</td>
      <td>business</td>
    </tr>
    <tr>
      <th>9528</th>
      <td>2021-11-30 15:42:59</td>
      <td>view</td>
      <td>0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>Russia</td>
      <td>Zavetnoye</td>
      <td>2.0</td>
      <td>Android</td>
      <td>Dear VP @ProfOsinbajo, this fee proposed by @N...</td>
      <td>covid</td>
    </tr>
  </tbody>
</table>
<p>1774 rows × 11 columns</p>
</div>




```python
df = pd.get_dummies(df, columns = ['action', 'gender', 'country', 'city', 'os', 'topic'])
```


```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
vect = vectorizer.fit_transform(df['text'])

```


```python
import numpy as np

tfidf_sums = vect.sum(axis=1)
df['tfidf_sum'] = np.array(tfidf_sums).flatten()
```


```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
df = vectorizer.fit_transform(df['text'])

```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>target</th>
      <th>age</th>
      <th>exp_group</th>
      <th>action_like</th>
      <th>action_view</th>
      <th>gender_0.0</th>
      <th>gender_1.0</th>
      <th>country_Russia</th>
      <th>city_Moscow</th>
      <th>city_Ulan-Ude</th>
      <th>city_Vologda</th>
      <th>city_Zavetnoye</th>
      <th>os_Android</th>
      <th>os_iOS</th>
      <th>topic_business</th>
      <th>topic_covid</th>
      <th>topic_entertainment</th>
      <th>topic_movie</th>
      <th>topic_politics</th>
      <th>topic_sport</th>
      <th>topic_tech</th>
      <th>tfidf_sum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>309</th>
      <td>2021-10-24 19:12:37</td>
      <td>0</td>
      <td>27.0</td>
      <td>0.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>8.496549</td>
    </tr>
    <tr>
      <th>310</th>
      <td>2021-10-24 19:15:07</td>
      <td>0</td>
      <td>27.0</td>
      <td>0.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>9.633701</td>
    </tr>
    <tr>
      <th>311</th>
      <td>2021-10-24 19:17:33</td>
      <td>0</td>
      <td>27.0</td>
      <td>0.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>9.987580</td>
    </tr>
    <tr>
      <th>312</th>
      <td>2021-10-24 19:20:15</td>
      <td>0</td>
      <td>27.0</td>
      <td>0.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>3.748610</td>
    </tr>
    <tr>
      <th>313</th>
      <td>2021-10-24 19:23:10</td>
      <td>0</td>
      <td>27.0</td>
      <td>0.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>6.787106</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9524</th>
      <td>2021-11-30 15:35:14</td>
      <td>0</td>
      <td>20.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>10.809886</td>
    </tr>
    <tr>
      <th>9525</th>
      <td>2021-11-30 15:36:26</td>
      <td>0</td>
      <td>20.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>3.824327</td>
    </tr>
    <tr>
      <th>9526</th>
      <td>2021-11-30 15:39:20</td>
      <td>0</td>
      <td>20.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>11.060152</td>
    </tr>
    <tr>
      <th>9527</th>
      <td>2021-11-30 15:40:56</td>
      <td>0</td>
      <td>20.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>8.183604</td>
    </tr>
    <tr>
      <th>9528</th>
      <td>2021-11-30 15:42:59</td>
      <td>0</td>
      <td>20.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>3.907761</td>
    </tr>
  </tbody>
</table>
<p>1774 rows × 23 columns</p>
</div>




```python
df = df.drop(['timestamp'],axis=1)
```


```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

X = df.drop("target", axis=1)
y = df["target"]

rf_pipe = Pipeline([
    ("scal", MinMaxScaler()),
    ("clf", RandomForestClassifier())
])

gb_pipe = Pipeline([
    ("scal", MinMaxScaler()),
    ("clf", GradientBoostingClassifier())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

rf_pipe.fit(X_train, y_train)
gb_pipe.fit(X_train, y_train)
```




<style>#sk-container-id-1 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: #000;
  --sklearn-color-text-muted: #666;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-1 {
  color: var(--sklearn-color-text);
}

#sk-container-id-1 pre {
  padding: 0;
}

#sk-container-id-1 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-1 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-1 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-1 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-1 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-1 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-1 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-1 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-1 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-1 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-1 label.sk-toggleable__label {
  cursor: pointer;
  display: flex;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
  align-items: start;
  justify-content: space-between;
  gap: 0.5em;
}

#sk-container-id-1 label.sk-toggleable__label .caption {
  font-size: 0.6rem;
  font-weight: lighter;
  color: var(--sklearn-color-text-muted);
}

#sk-container-id-1 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-1 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-1 div.sk-label label.sk-toggleable__label,
#sk-container-id-1 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-1 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-1 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-1 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-1 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 0.5em;
  text-align: center;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-1 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-1 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-1 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-1 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;scal&#x27;, MinMaxScaler()),
                (&#x27;clf&#x27;, GradientBoostingClassifier())])</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" ><label for="sk-estimator-id-1" class="sk-toggleable__label fitted sk-toggleable__label-arrow"><div><div>Pipeline</div></div><div><a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.6/modules/generated/sklearn.pipeline.Pipeline.html">?<span>Documentation for Pipeline</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></div></label><div class="sk-toggleable__content fitted"><pre>Pipeline(steps=[(&#x27;scal&#x27;, MinMaxScaler()),
                (&#x27;clf&#x27;, GradientBoostingClassifier())])</pre></div> </div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" ><label for="sk-estimator-id-2" class="sk-toggleable__label fitted sk-toggleable__label-arrow"><div><div>MinMaxScaler</div></div><div><a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.MinMaxScaler.html">?<span>Documentation for MinMaxScaler</span></a></div></label><div class="sk-toggleable__content fitted"><pre>MinMaxScaler()</pre></div> </div></div><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-3" type="checkbox" ><label for="sk-estimator-id-3" class="sk-toggleable__label fitted sk-toggleable__label-arrow"><div><div>GradientBoostingClassifier</div></div><div><a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html">?<span>Documentation for GradientBoostingClassifier</span></a></div></label><div class="sk-toggleable__content fitted"><pre>GradientBoostingClassifier()</pre></div> </div></div></div></div></div></div>




```python
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

rf_probs = rf_pipe.predict_proba(X_test)[:, 1]
gb_probs = gb_pipe.predict_proba(X_test)[:, 1]

# ROC curve
rf_fpr, rf_tpr, _ = roc_curve(y_test, rf_probs)
gb_fpr, gb_tpr, _ = roc_curve(y_test, gb_probs)

plt.figure(figsize=(8,6))
plt.plot(rf_fpr, rf_tpr, label=f'Random Forest (AUC = {roc_auc_score(y_test, rf_probs):.2f})')
plt.plot(gb_fpr, gb_tpr, label=f'Gradient Boosting (AUC = {roc_auc_score(y_test, gb_probs):.2f})')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
```




    <matplotlib.legend.Legend object at 0x7ffd9260b140>




```python

```
