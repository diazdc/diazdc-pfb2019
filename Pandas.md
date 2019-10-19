# Pandas

## What is pandas?

**Python Data Analysis Library**

A powerful library for manipulating data arranged in formats like matricies and data frames. It's arguably the most popular Python library used for data analysis. Pandas aims to provide Python users the same type of functionality as the popular statiscal language, **R**.

<br/>

![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2019/04/Python-Pandas-Applications.jpg)

<br/>

### Why familiarize yourself with Pandas?

So far we've discussed bulding multidimensional objects like lists of lists and dictionaries of dictionaries from raw data. However, bioinformatics modules (and many others) will often **return** results in the form of **data frame** or **a matrix**.

For example, you might need parse your RNA-seq results by a range of log fold changes or p-values.

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

## A breif word on vectorization

**Pandas, like R, works most efficiently with vectorized operations**

<br/>

This topic can get quite complicated, so here's what you need to know:
The most efficent way to perform operations is across entire rows or columns (vectors), rather than each individual units.

Rather that looping through individual values (scalars), we _apply_ operations to a list 

If you frequently work dataframes or matricies, please consider reading this 
[article](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6).

[here](https://stackoverflow.com/questions/35091979/why-is-vectorization-faster-in-general-than-loops)

![](https://miro.medium.com/max/2060/1*p4zjrqG97C4bFmOXU5UQog.png)

## Pandas has the ability to read in various data formats

- Open a local file using Pandas, usually a CSV file, but could also be a delimited text file (like TSV), Excel, etc

- Open a remote file or database like a CSV or a JSONon a website through a URL or read from a SQL table/database

### Reading in csv files

```
pandas.read_csv()

```



```

```





