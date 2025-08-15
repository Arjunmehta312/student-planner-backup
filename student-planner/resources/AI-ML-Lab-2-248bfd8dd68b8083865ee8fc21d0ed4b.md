
> 💡 Reference to [AI/ML Lecture 9](https://www.notion.so/24dbfd8dd68b8098af36de34a0d7e6a8) & [AI/ML Lecture 10](https://www.notion.so/24fbfd8dd68b801a9421e4886c905eec) 


### Dataset


[Car.csv](https://prod-files-secure.s3.us-west-2.amazonaws.com/cb8bfd8d-d68b-81fa-ac15-000328a0aab4/d024a51f-2217-4516-b4f9-369e6bbd57c6/Car.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXKUVEXI%2F20250815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250815T064756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIAODd%2BG2%2FgfVgLSVqlOGcWX%2FbFwZVZ8wmZKB67iIdSyuAiEA1s6yfS5e7cuxbAtMghiEe6QAGpo929uzgFDKCbkjWy4q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGnzOniFw4aZbiEYySrcA%2FMUdRoDWNLmDx3rq6XfltWuSEI4lVb52uZFyBaqEHhF%2B%2F5h%2FJvla1cYAfTW7BDCYdM4H4ED4Rah0DuvOqDxe5mlhIECexV4pT89PEhJr8ZDLlXRWg93a4%2BeTk8FrB0quC0rJmHVAR%2FS4d%2FrfKMBs%2FaMFZfh%2FtzK4fg83igZExgHG8KRF%2F7jWa%2FxZ%2BEqviWssAeAz%2B%2FIAxqURz9cE44omboWLLTxZRg7zrBkB4DLeSmsP8S7l3EdYrZX0TgVWI%2BOov2Q1tkrV8e42jaT40oTX%2BWM4yWSJvhrpZArDRRB305LU3H3HVw3xYyhlyx714RI2%2Bshnt894v1SJ04JjHYDRSpUdAXL%2F9j6fHkLF0W43U5olYAhvzVGjuJsguZxUq%2BG7t0y6cqLD4V0I9rpLHw3A0YsMcPw4Wduy5J2vckFsitay7dEV3b8Bw7M%2Bz3ZCOaQM56ANRr0%2FlC6ySrAcW%2B%2FXS5ApBFl1CCfMSAE%2FP%2FxmCSmp4Ab2uNVjtWADpgb5kecVDT%2B4M2yS4Xq0rqjQWp3723wEFWaqok24h4GTpiHe5esfp8t8IqGPxpCTzF%2B2%2BW4f8dII%2Fwyrry3GChWixGQu5SyXIFjEiqtEfYR33NBHx4FAASoJ1N4m744JRkrMOej%2B8QGOqUBunuO7OchPk0VkIIEuDLWc1KVx1Ky%2B8hWIfaus%2Bqvj9txVhWxCYq%2BFdvq1SgodZpiEa0KQNrMIE3dGDJSfc0tS%2BsGX9AkJS%2Bb4%2F%2BUwPJBqT5TtiyM9n%2FlBuh3Vihnq2p8pvjNxAlYH7LagW8sevr2HcJ%2FTaUCRXX9R%2FeJrkVkc9j4%2F%2F6zstlNtEpFMGU6kbW8IBT7Yp8VVTihOfHkxDbr59QBvIOh&X-Amz-Signature=1051525cb379754cee6344edee45efc069851951db566d2297ed25d1b779e91f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


### Code Snippets


Prerequisites


```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
```

1. Read the Car.csv file into a DataFrame

```python
df = pd.read_csv('Car.csv')
df.head()
```

1. Explore size, shape, data types of each column

```python
df.size, df.shape, df.dtypes
```

1. List down the columns of dataset

```python
df.columns.tolist()
```

1. Display the info of dataset and state your observations

```python
info_str = df.info()
```

1. Rename “Engine Fuel Type”→“Fuel Type” and “No. of Doors”→“Doors”

```python
df = df.rename(columns={'Engine Fuel Type':'Fuel Type','No. of Doors':'Doors'})
df.columns.tolist()
```

1. Find out ‘Fuel Type’ for the 4th row

```python
df.loc[3,'Fuel Type']
```

1. Find out value of second column for the 4th row

```python
df.iloc[3,1]
```

1. Select all rows for column “Fuel Type”

```python
df['Fuel Type']
```

1. Select all rows for columns “Make” and “Transmission Type”

```python
df[['Make','Transmission Type']]
```

1. Display 1 to 5 rows for columns 2 to 4 (excluding row 5 and column 4)

```python
df.iloc[0:4,1:3]
```

1. Identify unique values for “Make”, “Transmission Type”, “Vehicle Size”

```python
uniq_make = df['Make'].unique()
uniq_trans = df['Transmission Type'].unique()
uniq_size = df['Vehicle Size'].unique()
uniq_make, uniq_trans, uniq_size
```

1. Create a new data frame by replacing “??” with NaN

```python
df2 = df.replace('??', np.nan)
df2.head()
```

1. Check duplicates and delete those rows

```python
dup_count = df2.duplicated().sum()
df2 = df2.drop_duplicates()
dup_count, df2.shape
```

1. Identify total number of null values in each column

```python
df2.isnull().sum()
```

1. Drop rows with null values

```python
df3 = df2.dropna()
df3.shape
```

1. Convert dtypes of “Doors”, “Engine HP”, “Engine Cylinder” to int

```python
cols = ['Doors','Engine HP','Engine Cylinders']
df3[cols] = df3[cols].astype(int)
df3[cols].dtypes
```

1. Check numerical values and normalize if required

```python
num_cols = df3.select_dtypes(include=[np.number]).columns
scaler = MinMaxScaler()
df_norm = df3.copy()
df_norm[num_cols] = scaler.fit_transform(df3[num_cols])
df_norm[num_cols].head()
```

1. Label encode “Vehicle Size” and one-hot encode “Transmission Type”

```python
df_enc = df_norm.copy()
le = LabelEncoder()
df_enc['Vehicle Size'] = le.fit_transform(df_enc['Vehicle Size'])
df_enc = pd.get_dummies(df_enc, columns=['Transmission Type'], drop_first=False)
df_enc.head()
```

1. Identify total number of cars that run on “diesel” and “electric”

```python
diesel_count = (df3['Fuel Type'].str.lower()=='diesel').sum()
electric_count = (df3['Fuel Type'].str.lower()=='electric').sum()
diesel_count, electric_count
```

1. Mean of “highway MPG” for cars that run on “diesel”

```python
diesel_mean_hwy = df3.loc[df3['Fuel Type'].str.lower()=='diesel','highway MPG'].mean()
diesel_mean_hwy
```

1. Scatter plot “highway MPG” vs “city mpg” with color and title + inference

```python
plt.figure(figsize=(6,4))
sns.scatterplot(data=df3, x='highway MPG', y='city mpg', hue='Fuel Type', s=30)
plt.title('Highway MPG vs City mpg')
plt.tight_layout()
plt.show()
```


![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cb8bfd8d-d68b-81fa-ac15-000328a0aab4/e9850857-96cd-43b6-8186-2eea6032b517/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXKUVEXI%2F20250815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250815T064757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIAODd%2BG2%2FgfVgLSVqlOGcWX%2FbFwZVZ8wmZKB67iIdSyuAiEA1s6yfS5e7cuxbAtMghiEe6QAGpo929uzgFDKCbkjWy4q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGnzOniFw4aZbiEYySrcA%2FMUdRoDWNLmDx3rq6XfltWuSEI4lVb52uZFyBaqEHhF%2B%2F5h%2FJvla1cYAfTW7BDCYdM4H4ED4Rah0DuvOqDxe5mlhIECexV4pT89PEhJr8ZDLlXRWg93a4%2BeTk8FrB0quC0rJmHVAR%2FS4d%2FrfKMBs%2FaMFZfh%2FtzK4fg83igZExgHG8KRF%2F7jWa%2FxZ%2BEqviWssAeAz%2B%2FIAxqURz9cE44omboWLLTxZRg7zrBkB4DLeSmsP8S7l3EdYrZX0TgVWI%2BOov2Q1tkrV8e42jaT40oTX%2BWM4yWSJvhrpZArDRRB305LU3H3HVw3xYyhlyx714RI2%2Bshnt894v1SJ04JjHYDRSpUdAXL%2F9j6fHkLF0W43U5olYAhvzVGjuJsguZxUq%2BG7t0y6cqLD4V0I9rpLHw3A0YsMcPw4Wduy5J2vckFsitay7dEV3b8Bw7M%2Bz3ZCOaQM56ANRr0%2FlC6ySrAcW%2B%2FXS5ApBFl1CCfMSAE%2FP%2FxmCSmp4Ab2uNVjtWADpgb5kecVDT%2B4M2yS4Xq0rqjQWp3723wEFWaqok24h4GTpiHe5esfp8t8IqGPxpCTzF%2B2%2BW4f8dII%2Fwyrry3GChWixGQu5SyXIFjEiqtEfYR33NBHx4FAASoJ1N4m744JRkrMOej%2B8QGOqUBunuO7OchPk0VkIIEuDLWc1KVx1Ky%2B8hWIfaus%2Bqvj9txVhWxCYq%2BFdvq1SgodZpiEa0KQNrMIE3dGDJSfc0tS%2BsGX9AkJS%2Bb4%2F%2BUwPJBqT5TtiyM9n%2FlBuh3Vihnq2p8pvjNxAlYH7LagW8sevr2HcJ%2FTaUCRXX9R%2FeJrkVkc9j4%2F%2F6zstlNtEpFMGU6kbW8IBT7Yp8VVTihOfHkxDbr59QBvIOh&X-Amz-Signature=ba5522bd432ab7e15b8f3c0cecb1c84b9a32d4a628684a4afedc8068f295442f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Correlation matrix + inference

```python
plt.figure(figsize=(8,6))
sns.heatmap(df3.select_dtypes(include=[np.number]).corr(), annot=False, cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()
```


![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cb8bfd8d-d68b-81fa-ac15-000328a0aab4/d740a77f-dedf-4352-9152-fd6842d7399b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXKUVEXI%2F20250815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250815T064757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIAODd%2BG2%2FgfVgLSVqlOGcWX%2FbFwZVZ8wmZKB67iIdSyuAiEA1s6yfS5e7cuxbAtMghiEe6QAGpo929uzgFDKCbkjWy4q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGnzOniFw4aZbiEYySrcA%2FMUdRoDWNLmDx3rq6XfltWuSEI4lVb52uZFyBaqEHhF%2B%2F5h%2FJvla1cYAfTW7BDCYdM4H4ED4Rah0DuvOqDxe5mlhIECexV4pT89PEhJr8ZDLlXRWg93a4%2BeTk8FrB0quC0rJmHVAR%2FS4d%2FrfKMBs%2FaMFZfh%2FtzK4fg83igZExgHG8KRF%2F7jWa%2FxZ%2BEqviWssAeAz%2B%2FIAxqURz9cE44omboWLLTxZRg7zrBkB4DLeSmsP8S7l3EdYrZX0TgVWI%2BOov2Q1tkrV8e42jaT40oTX%2BWM4yWSJvhrpZArDRRB305LU3H3HVw3xYyhlyx714RI2%2Bshnt894v1SJ04JjHYDRSpUdAXL%2F9j6fHkLF0W43U5olYAhvzVGjuJsguZxUq%2BG7t0y6cqLD4V0I9rpLHw3A0YsMcPw4Wduy5J2vckFsitay7dEV3b8Bw7M%2Bz3ZCOaQM56ANRr0%2FlC6ySrAcW%2B%2FXS5ApBFl1CCfMSAE%2FP%2FxmCSmp4Ab2uNVjtWADpgb5kecVDT%2B4M2yS4Xq0rqjQWp3723wEFWaqok24h4GTpiHe5esfp8t8IqGPxpCTzF%2B2%2BW4f8dII%2Fwyrry3GChWixGQu5SyXIFjEiqtEfYR33NBHx4FAASoJ1N4m744JRkrMOej%2B8QGOqUBunuO7OchPk0VkIIEuDLWc1KVx1Ky%2B8hWIfaus%2Bqvj9txVhWxCYq%2BFdvq1SgodZpiEa0KQNrMIE3dGDJSfc0tS%2BsGX9AkJS%2Bb4%2F%2BUwPJBqT5TtiyM9n%2FlBuh3Vihnq2p8pvjNxAlYH7LagW8sevr2HcJ%2FTaUCRXX9R%2FeJrkVkc9j4%2F%2F6zstlNtEpFMGU6kbW8IBT7Yp8VVTihOfHkxDbr59QBvIOh&X-Amz-Signature=e83906a4f51d3040e527726dc5a83b02ed871ea3a2bca00fe4a0924a20e0a4c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


### File Exports


[AIML_Lab_02.html](https://prod-files-secure.s3.us-west-2.amazonaws.com/cb8bfd8d-d68b-81fa-ac15-000328a0aab4/9e482127-a1f1-460e-ba16-bdf20b4547a3/AIML_Lab_02.html?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXKUVEXI%2F20250815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250815T064757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIAODd%2BG2%2FgfVgLSVqlOGcWX%2FbFwZVZ8wmZKB67iIdSyuAiEA1s6yfS5e7cuxbAtMghiEe6QAGpo929uzgFDKCbkjWy4q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGnzOniFw4aZbiEYySrcA%2FMUdRoDWNLmDx3rq6XfltWuSEI4lVb52uZFyBaqEHhF%2B%2F5h%2FJvla1cYAfTW7BDCYdM4H4ED4Rah0DuvOqDxe5mlhIECexV4pT89PEhJr8ZDLlXRWg93a4%2BeTk8FrB0quC0rJmHVAR%2FS4d%2FrfKMBs%2FaMFZfh%2FtzK4fg83igZExgHG8KRF%2F7jWa%2FxZ%2BEqviWssAeAz%2B%2FIAxqURz9cE44omboWLLTxZRg7zrBkB4DLeSmsP8S7l3EdYrZX0TgVWI%2BOov2Q1tkrV8e42jaT40oTX%2BWM4yWSJvhrpZArDRRB305LU3H3HVw3xYyhlyx714RI2%2Bshnt894v1SJ04JjHYDRSpUdAXL%2F9j6fHkLF0W43U5olYAhvzVGjuJsguZxUq%2BG7t0y6cqLD4V0I9rpLHw3A0YsMcPw4Wduy5J2vckFsitay7dEV3b8Bw7M%2Bz3ZCOaQM56ANRr0%2FlC6ySrAcW%2B%2FXS5ApBFl1CCfMSAE%2FP%2FxmCSmp4Ab2uNVjtWADpgb5kecVDT%2B4M2yS4Xq0rqjQWp3723wEFWaqok24h4GTpiHe5esfp8t8IqGPxpCTzF%2B2%2BW4f8dII%2Fwyrry3GChWixGQu5SyXIFjEiqtEfYR33NBHx4FAASoJ1N4m744JRkrMOej%2B8QGOqUBunuO7OchPk0VkIIEuDLWc1KVx1Ky%2B8hWIfaus%2Bqvj9txVhWxCYq%2BFdvq1SgodZpiEa0KQNrMIE3dGDJSfc0tS%2BsGX9AkJS%2Bb4%2F%2BUwPJBqT5TtiyM9n%2FlBuh3Vihnq2p8pvjNxAlYH7LagW8sevr2HcJ%2FTaUCRXX9R%2FeJrkVkc9j4%2F%2F6zstlNtEpFMGU6kbW8IBT7Yp8VVTihOfHkxDbr59QBvIOh&X-Amz-Signature=c1dbbd8759571756db4f2faddca05c84d9dda7d0e347670ba35113954cc4ce51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/cb8bfd8d-d68b-81fa-ac15-000328a0aab4/42ba88fe-3fdd-4cb3-94d1-7395b259185e/AIML_Lab_02.ipynb?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXKUVEXI%2F20250815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250815T064757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIAODd%2BG2%2FgfVgLSVqlOGcWX%2FbFwZVZ8wmZKB67iIdSyuAiEA1s6yfS5e7cuxbAtMghiEe6QAGpo929uzgFDKCbkjWy4q%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDGnzOniFw4aZbiEYySrcA%2FMUdRoDWNLmDx3rq6XfltWuSEI4lVb52uZFyBaqEHhF%2B%2F5h%2FJvla1cYAfTW7BDCYdM4H4ED4Rah0DuvOqDxe5mlhIECexV4pT89PEhJr8ZDLlXRWg93a4%2BeTk8FrB0quC0rJmHVAR%2FS4d%2FrfKMBs%2FaMFZfh%2FtzK4fg83igZExgHG8KRF%2F7jWa%2FxZ%2BEqviWssAeAz%2B%2FIAxqURz9cE44omboWLLTxZRg7zrBkB4DLeSmsP8S7l3EdYrZX0TgVWI%2BOov2Q1tkrV8e42jaT40oTX%2BWM4yWSJvhrpZArDRRB305LU3H3HVw3xYyhlyx714RI2%2Bshnt894v1SJ04JjHYDRSpUdAXL%2F9j6fHkLF0W43U5olYAhvzVGjuJsguZxUq%2BG7t0y6cqLD4V0I9rpLHw3A0YsMcPw4Wduy5J2vckFsitay7dEV3b8Bw7M%2Bz3ZCOaQM56ANRr0%2FlC6ySrAcW%2B%2FXS5ApBFl1CCfMSAE%2FP%2FxmCSmp4Ab2uNVjtWADpgb5kecVDT%2B4M2yS4Xq0rqjQWp3723wEFWaqok24h4GTpiHe5esfp8t8IqGPxpCTzF%2B2%2BW4f8dII%2Fwyrry3GChWixGQu5SyXIFjEiqtEfYR33NBHx4FAASoJ1N4m744JRkrMOej%2B8QGOqUBunuO7OchPk0VkIIEuDLWc1KVx1Ky%2B8hWIfaus%2Bqvj9txVhWxCYq%2BFdvq1SgodZpiEa0KQNrMIE3dGDJSfc0tS%2BsGX9AkJS%2Bb4%2F%2BUwPJBqT5TtiyM9n%2FlBuh3Vihnq2p8pvjNxAlYH7LagW8sevr2HcJ%2FTaUCRXX9R%2FeJrkVkc9j4%2F%2F6zstlNtEpFMGU6kbW8IBT7Yp8VVTihOfHkxDbr59QBvIOh&X-Amz-Signature=90e7b2d6ed0e15115a2a1a7a63c72255a2636144174c90c568ee63e7446b9684&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

