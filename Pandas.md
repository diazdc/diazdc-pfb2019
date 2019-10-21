# Pandas

## What is Pandas?

**Python Data Analysis Library**

A powerful library for manipulating data arranged in formats like matricies and data frames. It's arguably the most popular Python library used for data analysis. Pandas aims to provide Python users the same type of functionality as the popular statistical language, **R**.

<br/>

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2019/04/Python-Pandas-Applications.jpg)

<br/>

### Why familiarize yourself with Pandas?

So far we've discussed building multidimensional objects like lists of lists and dictionaries of dictionaries from raw data. However, bioinformatics modules (and many others) will often **return** results in the form of Pandas **data frame** or **a matrix**. Further manipulation of these results will require some degree of Pandas operations.

For example, lets say you want to parse your RNA-seq results to a list of genes within a specific range of p-values and log fold changes, like "all p-values less than `1e-15` and log fold changes greater than `1.2`". You can apply your knowledge of Python operators such as `and, >, <` to subset a data frame based on the afformentioned parameters.

#### Pandas has the ability to read in various data formats

- Open a local file using Pandas, usually a CSV file, but could also be a delimited text file (like TSV), Excel, etc

- Open a remote file or database like a CSV or a JSONon a website through a URL or read from a SQL table/database

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

You can think of a vector (also reffered to as an [array](https://docs.python.org/3/library/array.html)) as a type of list that contains a single data type and optimized for parallel computing. For matricies and data frames in Pandas (also NumPy), vectors are rows and columns.

Rather that looping through individual values (scalars), we apply operations to vectors (rows/columns). That is, the vector is treated as a single object. This topic can get a bit complicated, but it is worth doing your homework if you frequently work with these data types. Here's a few articles to get you started:

- [A beginners guide to optimizing pandas code for speed.](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6)
- [Why is vectorization faster in general than loops?](https://stackoverflow.com/questions/35091979/why-is-vectorization-faster-in-general-than-loops)
- [Python Lists vs. Numpy Arrays, what's the difference?](https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference)


<br/>

<img src="https://miro.medium.com/max/2060/1*p4zjrqG97C4bFmOXU5UQog.png" width="80%" height="80%" />

Vectorization with Pandas series is **~390x** faster than crude looping

<br/>

## Basic methods for data manipulation

### Reading in csv files and row/column slicing

"Slicing" refers to subsetting, or removing rows and columns from a data frame. Here we'll read in a data frame, look at the contents, and subset it by slicing out arbitrary regions.

<br/>

```
import pandas as pd

# Setting index_col to 0 tells us that the first column contains the row names
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

#### Slicing

Pandas has different methods for subsetting dataframes.
We'll dicuss the most common methods, **loc**, and **iloc**

**loc** allows us to subset data by row or column label. For example, if I would
like to subset the column 'n_counts', I would use the following command:

<br/>

```
# The comma separates rows and columns, and the colon returns all rows.
cell_attributes.loc[:,'n_counts']
```

<br/>

**iloc** allows us to subset rows and colums by index number. This is useful if we want to subset multiple rows or columns without typing index names. Lets say we want to remove the columns with names 'orig_ident', 'res_2', and 'louvain'.

Lets take a look at the column names first and see if we can slice out the ones we'd like to keep.

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

<br/>

### Ordering dataframes by column values

Here we'll take look at ordering our data by a particular column value, or multiple column values.

<br/>

```
# Let's make a smaller dataset to work with
cell_df_sub = cell_attributes.iloc[:25,[0,1,3,5]]

# Set ascending=True to reverse the order
cell_df_sub.sort_values('n_counts', ascending=False)

# Sort by multiple columns in different directions
cell_df_sub.sort_values(by=['tree_ident', 'n_counts'], ascending=[True, False])
```

<br/>

### Subsetting data by condition

Understanding how to subset your data using conditional operations is very, _very_ useful. You'll often encounter situations where you want to filter your data on a certain set of parameters to reduce it to a more "meaningful" state (to make your PI happy).

<br/>

```
# Subsetting on a single condition
cell_df_sub.loc[(cell_df_sub['tree_ident'] == 1),]
```

<br/>

In the second example we're chaining together boolean operators to achieve results that satisfy multiple conditions. You can make these statments complex as you'd like.

Note: Pandas uses a pipe symbol to represent `or`, and an ampersand symbol to represent `and`. The backslashes in code simply allow us to break up our statement at arbitrary points for readbility.

<br/>

```
# Subsetting on multiple conditions.
cell_df_sub.loc[
    (cell_df_sub['tree_ident'] == 1) | \
    (cell_df_sub['tree_ident'] == 2) & \
    (cell_df_sub['n_genes'] > 1000),]
```

<br/>

What's actually going on here? The rows in the data frame are actually subsetted on a vector of True/False statements. That is, for every condition that is True for all statements, a row will be returned. If we remove the boonlean statements placed within `cell_df_sub.loc[]`, you can see why this is occuring.

<br/>

```
cell_df_sub['tree_ident'] == 1 | \
    (cell_df_sub['tree_ident'] == 2) & \
    (cell_df_sub['n_genes'] > 1000)
```

The End












