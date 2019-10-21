import pandas as pd

cell_attributes = pd.read_csv("./meta_data.csv", index_col=0)
type(cell_attributes)

# We notice rows and columns are truncated with the dimensions given the bottom
print(cell_attributes)

# Change the output view options
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
print(cell_attributes)

# Does this function seem familiar?
cell_attributes.head(10)

# Pandas has different methods for subsetting dataframes.
# We'll dicuss the most common methods, loc, and iloc

# loc allows us to subset data by row or column label. For example, if I would
# like to subset the column 'n_counts', I would use the following command:

cell_attributes.loc[:,'n_counts']

# The comma separates rows and columns. The colon returns all rows.


# iloc allows up to subset rows and colums by index number. This is useful
# if we have a list of values that we would like parse our data frame by.[2,4,6]

# Print column names
cell_attributes.columns.values
cell_attributes.columns.values[[0,1,3,5,7]]

# Print columns 0, 1, 3, 5, and 7
cell_attributes.iloc[:,[0,1,3,5,7]].head(10)

# Print rows 1 through 5 and columns 0, 1, 3, 5, and 7
cell_attributes.iloc[:5,[0,1,3,5,7]].head(10)

# Print rows 1 through 5, columns 1 through 3, and column 7
cell_attributes.iloc[:5, 0:3 + 7].head(10)



# Conditional subset

# Let's make a smaller dataset to work with
cell_df_sub = cell_attributes.iloc[:25,[0,1,3,5]]

# Set ascending=True to reverse the order
cell_df_sub.sort_values('n_counts', ascending=False)

# Sort by multiple columns in different directions
cell_df_sub.sort_values(by=['tree_ident', 'n_counts'], ascending=[True, False])




