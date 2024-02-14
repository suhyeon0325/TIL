```python
import pycaret
pycaret.__version__
```




    '3.2.0'




```python
import lightgbm
lightgbm.__version__
```




    '4.3.0'




```python
import pandas as pd

titanic_df = pd.read_csv("data/titanic_train.csv")
titanic_df.head(3)
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



## 데이터 확인


```python
print(type(titanic_df))
```

    <class 'pandas.core.frame.DataFrame'>



```python
# shape, 행과 열을 튜플 형태로 반환
print(titanic_df.shape)
```

    (891, 12)



```python
# info, 결측치와 유형 확인
print(titanic_df.info())
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 12 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   PassengerId  891 non-null    int64  
     1   Survived     891 non-null    int64  
     2   Pclass       891 non-null    int64  
     3   Name         891 non-null    object 
     4   Sex          891 non-null    object 
     5   Age          714 non-null    float64
     6   SibSp        891 non-null    int64  
     7   Parch        891 non-null    int64  
     8   Ticket       891 non-null    object 
     9   Fare         891 non-null    float64
     10  Cabin        204 non-null    object 
     11  Embarked     889 non-null    object 
    dtypes: float64(2), int64(5), object(5)
    memory usage: 83.7+ KB
    None



```python
titanic_df.head(3)
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df.describe()
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>714.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>446.000000</td>
      <td>0.383838</td>
      <td>2.308642</td>
      <td>29.699118</td>
      <td>0.523008</td>
      <td>0.381594</td>
      <td>32.204208</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.353842</td>
      <td>0.486592</td>
      <td>0.836071</td>
      <td>14.526497</td>
      <td>1.102743</td>
      <td>0.806057</td>
      <td>49.693429</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.420000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>223.500000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>20.125000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.910400</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>446.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>28.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>14.454200</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>668.500000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>38.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>891.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>80.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>512.329200</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df['Pclass'].value_counts()
```




    3    491
    1    216
    2    184
    Name: Pclass, dtype: int64




```python
type(titanic_df['Pclass'].value_counts())
```




    pandas.core.series.Series




```python
temp = titanic_df['Pclass'].value_counts()
temp
```




    3    491
    1    216
    2    184
    Name: Pclass, dtype: int64




```python
print(temp.index)
print(temp.values)
```

    Int64Index([3, 1, 2], dtype='int64')
    [491 216 184]



```python
titanic_df['Embarked'].value_counts(dropna=False)
```




    S      644
    C      168
    Q       77
    NaN      2
    Name: Embarked, dtype: int64




```python
titanic_df['Embarked'].value_counts(dropna=True)
```




    S    644
    C    168
    Q     77
    Name: Embarked, dtype: int64




```python
titanic_df['Cabin'].value_counts(dropna=False)
```




    NaN            687
    C23 C25 C27      4
    G6               4
    B96 B98          4
    C22 C26          3
                  ... 
    E34              1
    C7               1
    C54              1
    E36              1
    C148             1
    Name: Cabin, Length: 148, dtype: int64




```python
titanic_df['Cabin'].value_counts(dropna=True)
```




    B96 B98        4
    G6             4
    C23 C25 C27    4
    C22 C26        3
    F33            3
                  ..
    E34            1
    C7             1
    C54            1
    E36            1
    C148           1
    Name: Cabin, Length: 147, dtype: int64



## 교재 50~53p
- numpy, list, dictionary와 DataFrame으로 상호 변환이 가능하다


```python
# to_numpy() ==> 굳이 필요 없음
titanic_df.values  # numpy 변환
```




    array([[1, 0, 3, ..., 7.25, nan, 'S'],
           [2, 1, 1, ..., 71.2833, 'C85', 'C'],
           [3, 1, 3, ..., 7.925, nan, 'S'],
           ...,
           [889, 0, 3, ..., 23.45, nan, 'S'],
           [890, 1, 1, ..., 30.0, 'C148', 'C'],
           [891, 0, 3, ..., 7.75, nan, 'Q']], dtype=object)




```python
# 리스트로 변환
# titanic_df.values.tolist()
# temp.values.tolist()
```


```python
# 데이터 프레임을 딕셔너리로 변환
# titanic_df.to_dict('list')
```

## DataFrame의 칼럼 데이터 세트 생성과 수정


```python
# data['새로운컬럼명'] = 연산
```

## DataFrame 삭제
- axis = 1  ==>  지정된 컬럼 삭제
- axis = 0  ==>  지정된 index(=행) 삭제
- 57p, inplace = True
- temp2 = temp....

## set_option()
- streamlit 활용해서 깔끔하게 테이블 보여주고 싶을 때, 활용가치가 있음
- data_editor()


```python
titanic_df
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
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
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.0000</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.4500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.0000</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>



## 데이터 셀렉션 및 필터링
- .loc 문법만 잘 기억해도 큰 문제가 안됨!
- keyError  ==>  해당 데이터 프레임의 컬럼명이 현재 없는 상태 or Dictionary의 key값이 존재하지 않는 상태

## 결손 데이터 처리하기


```python
titanic_df.isna().head(3)
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df.isna().sum()
```




    PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age            177
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    dtype: int64



## fillna()로 결손데이터 대체하기


```python
# p.78
titanic_df['Cabin'] = titanic_df['Cabin'].fillna('C000')
titanic_df.head(3)
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>C000</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>C000</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
titanic_df.isna().sum()
```




    PassengerId    0
    Survived       0
    Pclass         0
    Name           0
    Sex            0
    Age            0
    SibSp          0
    Parch          0
    Ticket         0
    Fare           0
    Cabin          0
    Embarked       0
    dtype: int64



## apply lambda 식으로 데이터 가공
- 1회성 사용자 정의 함수


```python
def get_square(a):
    return a**2

print('3의 제곱은:', get_square(3))
```

    3의 제곱은: 9



```python
lambda_square = lambda x : x ** 2
print('3의 제곱은:', lambda_square(3))
```

    3의 제곱은: 9



```python
a=[1,2,3,4,5,6]
squares = map(lambda x : x**2, a)
list(squares)
```




    [1, 4, 9, 16, 25, 36]




```python
titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x : len(x))
titanic_df[['Name', 'Name_len']].head(3)
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
      <th>Name</th>
      <th>Name_len</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Braund, Mr. Owen Harris</td>
      <td>23</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>51</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Heikkinen, Miss. Laina</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x: len(x))
titanic_df[['Name', 'Name_len']].head(3)
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
      <th>Name</th>
      <th>Name_len</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Braund, Mr. Owen Harris</td>
      <td>23</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>51</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Heikkinen, Miss. Laina</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>



## apply()
- 행 단위로 연산을 할 때, apply() 사용
  + lambda: : 간단한 연산을 할 때는 lambda
  + udf(사용자 정의 함수) : if 조건절이 여러번 사용될 것 같은 상황이면 udf 사용한다.


```python
# 나이에 따라 세분화된 분류를 수행하는 함수 생성
def get_category(age):
    cat = ''
    if age <= 5: cat = 'Baby'
    elif age <= 12: cat = 'Child'
    elif age <= 18: cat = 'Teenager'
    elif age <= 25: cat = 'Student'
    elif age <= 35: cat = 'Young Adult'
    elif age <= 60: cat = 'Adult'
    else : cat = 'Elderly'
    
    return cat

# lambda 식 위에서 생성한 get_category() 함수를 반환값으로 지정
# get_category(X)는 입력값으로 'Age' 칼럼을 받아서 해당하는 cat 반환
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
titanic_df[['Age', 'Age_cat']].head()
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
      <th>Age</th>
      <th>Age_cat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22.0</td>
      <td>Student</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38.0</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>2</th>
      <td>26.0</td>
      <td>Young Adult</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.0</td>
      <td>Young Adult</td>
    </tr>
    <tr>
      <th>4</th>
      <td>35.0</td>
      <td>Young Adult</td>
    </tr>
  </tbody>
</table>
</div>



## 사이킷런 (Scikit-Learn)
- Python 머신러닝 라이브러리
- 엑셀 데이터  =>  정형 데이터  ==>  머신러닝 디폴트 라이브러리
   + 텐서플로, 케라스, 파이토치 등 딥러닝 전문 라이브러리 등장 (비정형 데이터)
   + 이미지 (비디오 영상), 자연어 (텍스트 데이터)
- 파이썬 기반의 다른 머신러닝 패키지도 사이킷런 스타일의 api를 지향한다
  + XGBoost, LightGBM, CatBoost 이런 종류의 알고리즘은 사이킷런 라이브러리 알고리즘 아님
  + XGBoost, LightGBM, CatBoost 알고리즘도 마치 사이킷런 클래스처럼 사용이 가능하도록 지원
 
- 가장 큰 단점
  + GPU 연산을 못함 / CPU 연산만 함


```python
import sklearn
```


```python
sklearn.__version__
```




    '1.2.2'



### 불꽃 품종 예측하기
- 3가지 중 한개를 예측


```python
# scikit-learn 라이브러리에서 붓꽃(iris) 데이터 세트를 불러오는 함수를 임포트
from sklearn.datasets import load_iris

# scikit-learn 라이브러리에서 결정 트리(Decision Tree) 분류기를 임포트
# 결정 트리는 분류와 회귀 문제에 널리 사용되는 모델로, 데이터의 특성(Feature)에 따라 트리 기반의 구조를 사용하여 예측을 수행
from sklearn.tree import DecisionTreeClassifier

# 데이터를 훈련 세트와 테스트 세트로 분리하는 함수를 임포트
# 모델을 학습시킬 때 사용하는 데이터(훈련 세트)와 모델의 성능을 평가하기 위해 사용하는
# 별도의 데이터(테스트 세트)로 데이터를 나누는 작업이 필요
# 이 함수는 데이터를 자동으로 나누어주며, 비율을 조정 가능
from sklearn.model_selection import train_test_split
```


```python
import pandas as pd
```


```python
# 붓꽃 데이터 세트 로딩
iris = load_iris()
# iris
```


```python
# iris.data는 Iris 데이터 세트에서 피처(feature)만으로 된 데이터를 numpy로 가짐
iris_data = iris.data
# iris_data
```


```python
# iris.target은 붓꽃 데이터 세트에서 레이블 (결정 값) 데이터를 numpy로 가짐
iris_label = iris.target
print('iris_target값:', iris_label)
print('iris_target명:', iris.target_names) # 0은 setosa, 1은 versicolor, 2는 virginica 품종
```

    iris_target값: [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
     2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
     2 2]
    iris_target명: ['setosa' 'versicolor' 'virginica']


## 생각해야 하는 것
- 종속변수가 문자로 되어있다.
  + 수단과 방법을 가리지 않고, 종속변수를 숫자로 변형을 해야겠다!!


```python
# 붓꽃 데이터를 자세히 보기 위해 DataFrame으로 변환
iris_df = pd.DataFrame(data=iris_data, columns = iris.feature_names)  # 독립변수의 컬럼명
iris_df['label'] = iris.target
iris_df.head(3)
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
      <th>sepal length (cm)</th>
      <th>sepal width (cm)</th>
      <th>petal length (cm)</th>
      <th>petal width (cm)</th>
      <th>label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## 훈련데이터와 테스트 데이터로 분리
- 정석 : 훈련(train) / 검증(validation) / 테스트(test)


```python
# X_train : 훈련데이터의 독립변수 (설명변수)
# X_test : 테스트데이터의 독립변수
# y_train : 훈련데이터의 종속변수
# y_test : 테스트데이터의 종속변수

# iris_data : 전체 데이터 독립 변수
# iris_label : 전체 데이터 종속 변수
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size = 0.2, random_state=11)
```

## 모델 학습
- DecisionTreeClassfier 객체 생성


```python
# DecisionTreeClassifier 객체를 생성
# 이 객체는 결정 트리 알고리즘을 사용하여 데이터를 분류하는 모델을 구현
# random_state 매개변수는 모델의 초기 상태를 결정하는 난수 생성기의 시드를 설정
# 이 값이 같으면 코드를 실행할 때마다 동일한 결과를 얻을 수 있어 결과의 재현성을 보장
dt_clf = DecisionTreeClassifier(random_state=11)

# fit 메소드를 사용하여 모델을 학습
# 이 과정에서 모델은 주어진 훈련 데이터(X_train)의 패턴을 학습
# 이를 기반으로 주어진 훈련 데이터의 레이블(y_train)을 예측
# X_train은 모델이 예측을 수행하기 위해 사용하는 특성(독립 변수)을 포함하고 있으며,
# y_train은 각 훈련 데이터 포인트에 대한 실제 레이블(종속 변수)을 포함합니다.
dt_clf.fit(X_train, y_train)  # 훈련 데이터의 독립변수와 종속변수

```




<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-2" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>DecisionTreeClassifier(ccp_alpha=0.0, class_weight=None, criterion=&#x27;gini&#x27;,
                       max_depth=None, max_features=None, max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_samples_leaf=1,
                       min_samples_split=2, min_weight_fraction_leaf=0.0,
                       random_state=11, splitter=&#x27;best&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" checked><label for="sk-estimator-id-2" class="sk-toggleable__label sk-toggleable__label-arrow">DecisionTreeClassifier</label><div class="sk-toggleable__content"><pre>DecisionTreeClassifier(ccp_alpha=0.0, class_weight=None, criterion=&#x27;gini&#x27;,
                       max_depth=None, max_features=None, max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_samples_leaf=1,
                       min_samples_split=2, min_weight_fraction_leaf=0.0,
                       random_state=11, splitter=&#x27;best&#x27;)</pre></div></div></div></div></div>




```python
# 학습이 완료된 dtc 객체에서 테스트 데이터 세트로 예측 수행
pred = dt_clf.predict(X_test)  # 테스트 데이터의 독립변수만 예측
pred
```




    array([2, 2, 1, 1, 2, 0, 1, 0, 0, 1, 1, 1, 1, 2, 2, 0, 2, 1, 2, 2, 1, 0,
           0, 1, 0, 0, 2, 1, 0, 1])




```python
y_test
```




    array([2, 2, 2, 1, 2, 0, 1, 0, 0, 1, 2, 1, 1, 2, 2, 0, 2, 1, 2, 2, 1, 0,
           0, 1, 0, 0, 2, 1, 0, 1])




```python
from sklearn.metrics import accuracy_score
print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test, pred)))
```

    예측 정확도: 0.9333


## 사이킷런 코드 형식
- sklearn.pipeline 방식대로 작성하는 것을 매우 강력하게 추천
   + 공식문서에서 매우 권장하는 사항
   + 빅데이터 분석기사 : 머신러닝 관련된 시험 (30/40점은 나옴)
 
- 수많은 머신러닝 교재에서 pipeline 잘 소개하는 책은 거의 없음
   + 빅데이터 분석기사 교재 (x)

## Model Selection 모듈 소개


```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
dt_clf = DecisionTreeClassifier()
train_data = iris.data
train_label = iris.target
dt_clf.fit(train_data, train_label)

# 학습 데이터 셋으로 예측 수행
pred = dt_clf.predict(train_data)
print('예측 정확도:',accuracy_score(train_label,pred))
```

    예측 정확도: 1.0


- 답을 알고 있는 상태에서 문제를 풀었다!
- 그래서, 훈련데이터와 테스트 데이터를 분리하는 이유


```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

dt_clf = DecisionTreeClassifier( )
iris_data = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, 
                                                    test_size=0.3, random_state=121)

dt_clf.fit(X_train, y_train)
pred = dt_clf.predict(X_test)
print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test,pred)))
```

    예측 정확도: 0.9556


### K-폴드 교차 검증
- k=5 개인 경우에는, 5번의 모델 학습
   + 훈련데이터와 검증 데이터의 샘플은 각각 다르다!
   + 평가 5번, 평균을 뽑는 것이 목적


```python
from sklearn.tree import DecisionTreeClassifier  # 결정 트리 분류기
from sklearn.metrics import accuracy_score  # 정확도 계산 함수
from sklearn.model_selection import KFold  # K-폴드 교차 검증
import numpy as np  

iris = load_iris()  
features = iris.data  # 독립 변수, 붓꽃의 특성 데이터
label = iris.target  # 종속 변수, 붓꽃의 종류 레이블
dt_clf = DecisionTreeClassifier(random_state=156)  # 결정 트리 분류기 인스턴스화, 고정된 난수

# KFold 객체 생성, 5개의 폴드로 분리
kfold = KFold(n_splits=5)
cv_accuracy = []  # 폴드별 정확도를 저장할 리스트
print('붓꽃 데이터 세트 크기:', features.shape[0])  # 데이터 세트 크기 출력
```

    붓꽃 데이터 세트 크기: 150



```python
n_iter = 0
# KFold로 분할된 인덱스를 통해 학습 및 검증 데이터 분리 및 평가
for train_index, test_index in kfold.split(features):
    # 학습용, 검증용 데이터 분리
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    # 학습 및 예측
    dt_clf.fit(X_train, y_train)    
    pred = dt_clf.predict(X_test)
    n_iter += 1
    # 반복 시마다 정확도 측정
    accuracy = np.round(accuracy_score(y_test, pred), 4)
    print('\n#{0} 교차 검증 정확도: {1}, 학습 데이터 크기: {2}, 검증 데이터 크기: {3}'
          .format(n_iter, accuracy, X_train.shape[0], X_test.shape[0]))
    print('#{0} 검증 세트 인덱스: {1}'.format(n_iter, test_index))
    cv_accuracy.append(accuracy)
    
# 평균 정확도 계산
print('\n## 평균 검증 정확도:', np.mean(cv_accuracy))
```

    
    #1 교차 검증 정확도: 1.0, 학습 데이터 크기: 120, 검증 데이터 크기: 30
    #1 검증 세트 인덱스: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
     24 25 26 27 28 29]
    
    #2 교차 검증 정확도: 0.9667, 학습 데이터 크기: 120, 검증 데이터 크기: 30
    #2 검증 세트 인덱스: [30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53
     54 55 56 57 58 59]
    
    #3 교차 검증 정확도: 0.8667, 학습 데이터 크기: 120, 검증 데이터 크기: 30
    #3 검증 세트 인덱스: [60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83
     84 85 86 87 88 89]
    
    #4 교차 검증 정확도: 0.9333, 학습 데이터 크기: 120, 검증 데이터 크기: 30
    #4 검증 세트 인덱스: [ 90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
     108 109 110 111 112 113 114 115 116 117 118 119]
    
    #5 교차 검증 정확도: 0.7333, 학습 데이터 크기: 120, 검증 데이터 크기: 30
    #5 검증 세트 인덱스: [120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137
     138 139 140 141 142 143 144 145 146 147 148 149]
    
    ## 평균 검증 정확도: 0.9


## ML 과정
- 데이터 수집
- 데이터셋 분리 (여기 집중!!!)
  + 통계에서 말하는 샘플링 에러와 관련이 있음
- 모델 불러오기
- 모델 학습
- 모델 평가

### Stratified K 폴드
- 종속변수가 불균형한(imbalanced) 분포도를 가진 데이터 집합
  + 코로나 데이터 (양성 / 음성)
    - 검사 10만명, 양성 판정 받는 사람은 매우 적고 / 대부분은 다 음성 판정


```python
import pandas as pd
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['label']=iris.target
iris_df['label'].value_counts()
kfold = KFold(n_splits=3)
# kfold.split(X)는 폴드 세트를 3번 반복할 때마다 달라지는 학습/테스트 용 데이터 로우 인덱스 번호 반환. 
n_iter =0
for train_index, test_index  in kfold.split(iris_df):
    n_iter += 1
    label_train= iris_df['label'].iloc[train_index]
    label_test= iris_df['label'].iloc[test_index]
    print('## 교차 검증: {0}'.format(n_iter))
    print('학습 레이블 데이터 분포:\n', label_train.value_counts())
    print('검증 레이블 데이터 분포:\n', label_test.value_counts())
```

    ## 교차 검증: 1
    학습 레이블 데이터 분포:
     1    50
    2    50
    Name: label, dtype: int64
    검증 레이블 데이터 분포:
     0    50
    Name: label, dtype: int64
    ## 교차 검증: 2
    학습 레이블 데이터 분포:
     0    50
    2    50
    Name: label, dtype: int64
    검증 레이블 데이터 분포:
     1    50
    Name: label, dtype: int64
    ## 교차 검증: 3
    학습 레이블 데이터 분포:
     0    50
    1    50
    Name: label, dtype: int64
    검증 레이블 데이터 분포:
     2    50
    Name: label, dtype: int64



```python
# 층화추출 방식으로 데이터셋 분리
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=3)
n_iter=0

for train_index, test_index in skf.split(iris_df, iris_df['label']):
    n_iter += 1
    label_train= iris_df['label'].iloc[train_index]
    label_test= iris_df['label'].iloc[test_index]
    print('## 교차 검증: {0}'.format(n_iter))
    print('학습 레이블 데이터 분포:\n', label_train.value_counts())
    print('검증 레이블 데이터 분포:\n', label_test.value_counts())
```

    ## 교차 검증: 1
    학습 레이블 데이터 분포:
     2    34
    0    33
    1    33
    Name: label, dtype: int64
    검증 레이블 데이터 분포:
     0    17
    1    17
    2    16
    Name: label, dtype: int64
    ## 교차 검증: 2
    학습 레이블 데이터 분포:
     1    34
    0    33
    2    33
    Name: label, dtype: int64
    검증 레이블 데이터 분포:
     0    17
    2    17
    1    16
    Name: label, dtype: int64
    ## 교차 검증: 3
    학습 레이블 데이터 분포:
     0    34
    1    33
    2    33
    Name: label, dtype: int64
    검증 레이블 데이터 분포:
     1    17
    2    17
    0    16
    Name: label, dtype: int64



```python

```
