# Pandas

## What is Pandas?

**Python Data Analysis Library**

A powerful library for manipulating data arranged in formats like matricies and data frames. It's arguably the most popular Python library used for data analysis. Pandas aims to provide Python users the same type of functionality as the popular statiscal language, **R**.

<br/>

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2019/04/Python-Pandas-Applications.jpg)

<br/>

### Why familiarize yourself with Pandas?

So far we've discussed building multidimensional objects like lists of lists and dictionaries of dictionaries from raw data. However, bioinformatics modules (and many others) will often **return** results in the form of Pandas **data frame** or **a matrix**. Further manipulation of these results will require some degree of Pandas operations.

For example, lets say you want to parse your RNA-seq results to a list of genes within a specific range of p-values and log fold changes, like "all p-values less than 1e-15 and log fold changes greater than 1.2". You can apply your knowledge of Python operators such as `and, >, <` to subset a data frame based on the afformentioned parameters.

<br/>

## Types of data manipulated in Pandas

### Matrices

A matrix is an data structure where numbers are arranged into rows and columns. They will typically conatin floats __or__ integers, but not both. Matrices are used when you need to perform mathmatical operations between datasets that contain multiple dimensions.

<br/>

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Gene_co-expression_network_construction_steps.png/720px-Gene_co-expression_network_construction_steps.png)

<br/>

### Data frames

A data frame is a table-like data structure and can cotain mixed data types (strings, floats, integers, etc.). This is the type of data structure you're used seeing in Excel.

<br/>

![](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0161567.t005&type=large)

<br/>

## A brief word on vectorization

**Operations in Pandas, like R, work most efficiently when vectorized**<br/>

<br/>

You can think of a vector (also reffered to as an [array](https://docs.python.org/3/library/array.html)) as a list that contains a single data type used. For matricies, this can be any row or column.

Rather that looping through individual values (scalars), we _apply_ operations to vectors. That is, the vector is treated as a single object. 

If you frequently work dataframes or matricies, please consider reading this 
[article](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6) and this
[stackoverflow thread](https://stackoverflow.com/questions/35091979/why-is-vectorization-faster-in-general-than-loops).

![](https://miro.medium.com/max/2060/1*p4zjrqG97C4bFmOXU5UQog.png)

<img src="https://miro.medium.com/max/2060/1*p4zjrqG97C4bFmOXU5UQog.png" width="75%" height="75%" />

## Pandas has the ability to read in various data formats

- Open a local file using Pandas, usually a CSV file, but could also be a delimited text file (like TSV), Excel, etc

- Open a remote file or database like a CSV or a JSONon a website through a URL or read from a SQL table/database

<br/>

## Basic methods for data manipulation

### Reading in csv files

<br/>

```
import pandas as pd

cell_attributes = pd.read_csv("./meta_data.csv", index_col = 0)
type(cell_attributes)
```

<br/>

```
# We notice rows and columns are truncated with the dimensions given the bottom
print(cell_attributes)

# Change the output view options
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

# Does this function seem familiar?
cell_attributes.head(10)
```

<br/>

Pandas has different methods for subsetting dataframes.
We'll dicuss the most common methods, **loc**, and **iloc**

loc allows us to subset data by row or column label. For example, if I would
like to subset the column 'n_counts', I would use the following command:

<br/>

```
# The comma separates rows and columns, and the colon returns all rows.
cell_attributes.loc[:,'n_counts']
```

<br/>

iloc allows up to subset rows and colums by index number. This is useful if we want to subset multiple rows or columns without typing index names. Lets say we want to remove the columns with names 'orig_ident', 'res_2', and 'louvain'.

<br/>

```
# Return column names
cell_attributes.columns.values
cell_attributes.columns.values[[0,1,3,5,7]]
```

<br/>

Now we can apply the same indexing pattern to our **iloc** method to return only the columns we're interested in. I've also included a few more slicing variations so you can get a feel for more complex slicing patterns.

<br/>

```
# Return columns 0, 1, 3, 5, and 7
cell_attributes.iloc[:,[0,1,3,5,7]].head(10)

# Return rows 1 through 5 and columns 0, 1, 3, 5, and 7
cell_attributes.iloc[:5,[0,1,3,5,7]].head(10)

# Return rows 1 through 5, columns 1 through 3, and column 7
cell_attributes.iloc[:5, 0:3 + 7].head(10)
```



