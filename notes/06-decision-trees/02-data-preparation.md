## 6.2 Data Cleaning and Preparation

In this session we did data cleaning and preparation on the credit-risk -scoring data. 

Below is the summary of the operations:

* downloaded the dataset using `wget`

* made the name of the columns uniform by making all of their letters lower case

* converted the categorical variables (that were `int64` initially) into strings (`okay`, `default` etc.) using `map()` method

* replaced missing values in numerical variables (which were a very large number 99999999) with `NaN` first

* splitted the dataset into 60/20/20 using `train_test_split` method

* binarized our target variable (since it is a binary classification problem)


**List of new commnads learnt:**

1. `!head CreditScoring.csv`

2. `df.status = df.status.map(status_values)`

3. `df.income.replace(to_replace = 99999999, value = np.nan)`

4. `df.status.value_counts()`

5. `df[df.status != 'unk'].reset_index(drop = True)`

**References**

1. Youtube video for Machine Learning Zoomcamp [Link](https://www.youtube.com/watch?v=tfuQdI3YO2c&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=58)

2. Jupyter notebook [Link](https://github.com/bhasarma/mlcoursezoom-camp/blob/main/WK06-decision-trees/WEEK-06-notebook.ipynb)

