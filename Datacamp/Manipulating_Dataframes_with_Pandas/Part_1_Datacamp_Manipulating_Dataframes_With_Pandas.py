"""
Datacamp - Manipulating DataFrames with pandas
https://www.datacamp.com/courses/manipulating-dataframes-with-pandas
Part 1 : Extracting and transforming data
Python 3.X
"""



"""
In this chapter, you will learn all about how to index, slice, filter, and transform DataFrames, using a variety of datasets, ranging from 2012 US election data for the state of Pennsylvania to Pittsburgh weather data.
"""



""" answer question : 4
Index ordering
50xp

In this exercise, the DataFrame election is provided for you. It contains the 2012 US election results for the state of Pennsylvania with county names as row indices. Your job is to select 'Bedford' county and the'winner' column. Which method is the preferred way?

Feel free to explore the DataFrame in the IPython Shell.
Possible Answers

    election['Bedford', 'winner']
    1
    election['Bedford']['winner']
    2
    election['eggs']['Bedford']
    3
    election.loc['Bedford', 'winner']
    4
    election.iloc['Bedford', 'winner']
    5
"""

""" results or consol output
In [2]: election.loc['Bedford', 'winner']
Out[2]: 'Romney'

In [3]: election.head()
Out[3]:
          state   total      Obama     Romney  winner  voters
county
Adams        PA   41973  35.482334  63.112001  Romney   61156
Allegheny    PA  614671  56.640219  42.185820   Obama  924351
Armstrong    PA   28322  30.696985  67.901278  Romney   42147
Beaver       PA   80015  46.032619  52.637630  Romney  115157
Bedford      PA   21444  22.057452  76.986570  Romney   32189
"""



"""
Positional and labeled indexing
100xp

Given a pair of label-based indices, sometimes it's necessary to find the corresponding positions. In this exercise, you will use the Pennsylvania election results again. The DataFrame is provided for you as election.

Find x and y such that election.iloc[x, y] == election.loc['Bedford', 'winner']. That is, what is the row position of 'Bedford', and the column position of 'winner'? Remember that the first position in Python is 0, not 1!

To answer this question, first explore the DataFrame using election.head() in the IPython Shell and inspect it with your eyes.
Instructions

    Explore the DataFrame in the IPython Shell using election.head().
    Assign the row position of election.loc['Bedford'] to x.
    Assign the column position of election['winner'] to y.
    Hit 'Submit Answer' to print the boolean equivalence of the .loc and .iloc selections.

"""
# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])
""" results or consol output
In [1]: election.head()
Out[1]:
          state   total      Obama     Romney  winner  voters
county
Adams        PA   41973  35.482334  63.112001  Romney   61156
Allegheny    PA  614671  56.640219  42.185820   Obama  924351
Armstrong    PA   28322  30.696985  67.901278  Romney   42147
Beaver       PA   80015  46.032619  52.637630  Romney  115157
Bedford      PA   21444  22.057452  76.986570  Romney   32189

<script.py> output:
    True
"""





"""
Indexing and column rearrangement
100xp

There are circumstances in which it's useful to modify the order of your DataFrame columns. We do that now by extracting just two columns from the Pennsylvania election results DataFrame.

Your job is to read the CSV file and set the index to 'county'. You'll then assign a new DataFrame by selecting the list of columns ['winner', 'total', 'voters']. The CSV file is provided to you in the variable filename.
Instructions

    Import pandas as pd.
    Read in filename using pd.read_csv() and set the index to 'county' by specifying the index_col parameter.
    Create a separate DataFrame results with the columns ['winner', 'total', 'voters'].
    Print the output using results.head(). This has been done for you, so hit 'Submit Answer' to see the new DataFrame!

"""
# Import pandas
import pandas as pd

# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')

# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())
""" results or consol output
In [1]: import pandas as pd

In [2]: election = pd.read_csv(filename, index_col='county')

In [3]: election.head()
Out[3]:
          state   total      Obama     Romney  winner  voters
county
Adams        PA   41973  35.482334  63.112001  Romney   61156
Allegheny    PA  614671  56.640219  42.185820   Obama  924351
Armstrong    PA   28322  30.696985  67.901278  Romney   42147
Beaver       PA   80015  46.032619  52.637630  Romney  115157
Bedford      PA   21444  22.057452  76.986570  Romney   32189

<script.py> output:
               winner   total  voters
    county
    Adams      Romney   41973   61156
    Allegheny   Obama  614671  924351
    Armstrong  Romney   28322   42147
    Beaver     Romney   80015  115157
    Bedford    Romney   21444   32189
"""





"""
Slicing rows
100xp

The Pennsylvania US election results data set that you have been using so far is ordered by county name. This means that county names can be sliced alphabetically. In this exercise, you're going to perform slicing on the county names of the election DataFrame from the previous exercises, which has been pre-loaded for you.
Instructions

    Slice the row labels 'Perry' to 'Potter' and assign the output to p_counties.
    Print the p_counties DataFrame. This has been done for you.
    Slice the row labels 'Potter' to 'Perry' in reverse order with the stepsize -1 and assign to p_counties_rev.
    Print the p_counties_rev DataFrame. This has also been done for you, so hit 'Submit Answer' to see the result of your slicing!

"""
# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc['Perry':'Potter',:]

# Print the p_counties DataFrame
print(p_counties)
print('-----------------')

# Slice the row labels 'Potter' to 'Perry' in reverse order with the stepsize -1: p_counties_rev
p_counties_rev = p_counties.loc['Potter':'Perry':-1,:]

# Print the p_counties_rev DataFrame
print(p_counties_rev)
""" results or consol output
<script.py> output:
                 state   total      Obama     Romney  winner   voters
    county
    Perry           PA   18240  29.769737  68.591009  Romney    27245
    Philadelphia    PA  653598  85.224251  14.051451   Obama  1099197
    Pike            PA   23164  43.904334  54.882576  Romney    41840
    Potter          PA    7205  26.259542  72.158223  Romney    10913
    -----------------
                 state   total      Obama     Romney  winner   voters
    county
    Potter          PA    7205  26.259542  72.158223  Romney    10913
    Pike            PA   23164  43.904334  54.882576  Romney    41840
    Philadelphia    PA  653598  85.224251  14.051451   Obama  1099197
    Perry           PA   18240  29.769737  68.591009  Romney    27245
"""




"""
Slicing columns
100xp

Similar to row slicing, columns can be sliced by value. In this exercise, your job is to slice column names from the Pennsylvania election results DataFrame using .loc[].

It has been pre-loaded for you as election, with the index set to 'county'.
Instructions

    Slice the columns from the starting column to 'Obama' and assign the result to left_columns
    Slice the columns from 'Obama' to 'winner' and assign the result to middle_columns
    Slice the columns from 'Romney' to the end and assign the result to right_columns
    The code to print the first 5 rows of left_columns, middle_columns, and right_columns has been written, so hit 'Submit Answer' to see the results!

"""
# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:,:'Obama']

# Print the output of left_columns.head()
print(left_columns.head())
print('-----------------')
# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:,'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())
print('-----------------')
# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:,'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())
print('-----------------')
""" results or consol output
<script.py> output:
              state   total      Obama
    county
    Adams        PA   41973  35.482334
    Allegheny    PA  614671  56.640219
    Armstrong    PA   28322  30.696985
    Beaver       PA   80015  46.032619
    Bedford      PA   21444  22.057452
    -----------------
                   Obama     Romney  winner
    county
    Adams      35.482334  63.112001  Romney
    Allegheny  56.640219  42.185820   Obama
    Armstrong  30.696985  67.901278  Romney
    Beaver     46.032619  52.637630  Romney
    Bedford    22.057452  76.986570  Romney
    -----------------
                  Romney  winner  voters
    county
    Adams      63.112001  Romney   61156
    Allegheny  42.185820   Obama  924351
    Armstrong  67.901278  Romney   42147
    Beaver     52.637630  Romney  115157
    Bedford    76.986570  Romney   32189
    -----------------
"""




"""
Subselecting DataFrames with lists
100xp

You can use lists to select specific row and column labels with the .loc[] accessor. In this exercise, your job is to select the counties ['Philadelphia', 'Centre', 'Fulton'] and the columns ['winner','Obama','Romney'] from the election DataFrame, which has been pre-loaded for you with the index set to 'county'.
Instructions

    Create the list of row labels ['Philadelphia', 'Centre', 'Fulton'] and assign it to rows.
    Create the list of column labels ['winner', 'Obama', 'Romney'] and assign it to cols.
    Create a new DataFrame by selecting with rows and cols in .loc[] and assign it to three_counties.
    Print the three_counties DataFrame. This has been done for you, so hit 'Submit Answer` to see your new DataFrame.

"""
# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows,cols]

# Print the three_counties DataFrame
print(three_counties)

""" results or consol output
<script.py> output:
                  winner      Obama     Romney
    county
    Philadelphia   Obama  85.224251  14.051451
    Centre        Romney  48.948416  48.977486
    Fulton        Romney  21.096291  77.748861
"""




"""
Thresholding data
100xp

In this exercise, we have provided the Pennsylvania election results and included a column called 'turnout' that contains the percentage of voter turnout per county. Your job is to prepare a boolean array to select all of the rows and columns where voter turnout exceeded 70%.

As before, the DataFrame is available to you as election with the index set to 'county'.
Instructions

    Create a boolean array of the condition where the 'turnout' column is greater than 70 and assign it to high_turnout.
    Filter the election DataFrame with the high_turnout array and assign it to high_turnout_df.
    Print the filtered DataFrame. This has been done for you, so hit 'Submit Answer' to see it!

"""
# Create the boolean array: high_turnout
high_turnout = election.turnout > 70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)
""" results or consol output
<script.py> output:
                 state   total      Obama     Romney  winner  voters    turnout  \
    county
    Bucks           PA  319407  49.966970  48.801686   Obama  435606  73.324748
    Butler          PA   88924  31.920516  66.816607  Romney  122762  72.436096
    Chester         PA  248295  49.228539  49.650617  Romney  337822  73.498766
    Forest          PA    2308  38.734835  59.835355  Romney    3232  71.410891
    Franklin        PA   62802  30.110506  68.583803  Romney   87406  71.850903
    Montgomery      PA  401787  56.637223  42.286834   Obama  551105  72.905708
    Westmoreland    PA  168709  37.567646  61.306154  Romney  238006  70.884347

                     margin
    county
    Bucks          1.165284
    Butler        34.896091
    Chester        0.422079
    Forest        21.100520
    Franklin      38.473297
    Montgomery    14.350390
    Westmoreland  23.738508
"""





"""
Filtering columns using other columns
100xp

The election results DataFrame has a column labeled 'margin' which expresses the number of extra votes the winner received over the losing candidate. This number is given as a percentage of the total votes cast. It is reasonable to assume that in counties where this margin was less than 1%, the results would too-close-to-call.

Your job is to use boolean selection to filter the rows where the margin was less than 1. You'll then convert these rows of the 'winner' column to np.nan to indicate that these results are too close to declare a winner.

The DataFrame has been pre-loaded for you as election.
Instructions

    Import numpy as np.
    Create a boolean array for the condition where the 'margin' column is less than 1 and assign it to too_close.
    Convert the entries in the 'winner' column where the result was too close to call to np.nan.
    Print the output of election.info(). This has been done for you, so hit 'Submit Answer' to see the results.

"""
# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election.margin < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.winner[too_close] = np.nan

# Print the output of election.info()
print(election.info())
""" results or consol output
<script.py> output:
    <class 'pandas.core.frame.DataFrame'>
    Index: 67 entries, Adams to York
    Data columns (total 8 columns):
    state      67 non-null object
    total      67 non-null int64
    Obama      67 non-null float64
    Romney     67 non-null float64
    winner     64 non-null object
    voters     67 non-null int64
    turnout    67 non-null float64
    margin     67 non-null float64
    dtypes: float64(4), int64(2), object(2)
    memory usage: 4.7+ KB
    None
"""





"""
Filtering using NaNs
100xp

In certain scenarios, it may be necessary to remove rows and columns with missing data from a DataFrame. The .dropna() method is used to perform this action. You'll now practice using this method on a dataset obtained from Vanderbilt University, which consists of data from passengers on the Titanic.

The DataFrame has been pre-loaded for you as titanic. Explore it in the IPython Shell and you will note that there are many NaNs. You will focus specifically on the 'age' and 'cabin' columns in this exercise. Your job is to use .dropna() to remove rows where any of these two columns contains missing data and rows where all of these two columns contain missing data.

You'll also use the .shape attribute, which returns the number of rows and columns in a tuple from a DataFrame, or the number of rows from a Series, to see the effect of dropping missing values from a DataFrame.

Finally, you'll use the thresh= keyword argument to drop columns from full dataset that have more than 1000 missing values.
Instructions

    Select the 'age' and 'cabin' columns of titanic and create a new DataFrame df.
    Print the shape of df. This has been done for you.
    Drop rows in df with how='any' and print the shape.
    Drop rows in df with how='all' and print the shape.
    Drop columns from the titanic DataFrame that have more than 1000 missing values by specifying the thresh and axis keyword arguments. Print the output of .info() from this.

"""
# Select the 'age' and 'cabin' columns: df
df = titanic[['age','cabin']]

# Print the shape of df
print(df.shape)
print('------------------------')

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)
print('------------------------')
# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)
print('------------------------')
# Call .dropna() with thresh=1000 and axis='columns' and print the output of .info() from titanic
print(titanic.dropna(thresh=1000, axis='columns').info())
print('------------------------')
""" results or consol output
<script.py> output:
    (1309, 2)
    ------------------------
    (272, 2)
    ------------------------
    (1069, 2)
    ------------------------
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1309 entries, 0 to 1308
    Data columns (total 10 columns):
    pclass      1309 non-null int64
    survived    1309 non-null int64
    name        1309 non-null object
    sex         1309 non-null object
    age         1046 non-null float64
    sibsp       1309 non-null int64
    parch       1309 non-null int64
    ticket      1309 non-null object
    fare        1308 non-null float64
    embarked    1307 non-null object
    dtypes: float64(2), int64(4), object(4)
    memory usage: 102.3+ KB
    None
    ------------------------
"""




"""
Using apply() to transform a column
100xp

The .apply() method can be used on a pandas DataFrame to apply an arbitrary Python function to every element. In this exercise you'll take daily weather data in Pittsburgh in 2013 obtained from Weather Underground.

A function to convert degrees Fahrenheit to degrees Celsius has been written for you. Your job is to use the .apply() method to perform this conversion on the 'Mean TemperatureF' and 'Mean Dew PointF' columns of the weather DataFrame.
Instructions

    Apply the to_celsius function over the ['Mean TemperatureF','Mean Dew PointF'] columns.
    Reassign the columns of df_celsius to ['Mean TemperatureC','Mean Dew PointC'].
    Hit 'Submit Answer' to see the new DataFrame with the converted units.

"""
# Write a function to convert degrees Fahrenheit to degrees Celsius: to_celsius
def to_celsius(F):
    return 5/9*(F - 32)

# Apply the function over 'Mean TemperatureF' and 'Mean Dew PointF': df_celsius
df_celsius = weather[['Mean TemperatureF','Mean Dew PointF']].apply(to_celsius)

# Reassign the columns df_celsius
df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

# Print the output of df_celsius.head()
print(df_celsius.head())
""" results or consol output
<script.py> output:
       Mean TemperatureC  Mean Dew PointC
    0          -2.222222        -2.777778
    1          -6.111111       -11.111111
    2          -4.444444        -9.444444
    3          -2.222222        -7.222222
    4          -1.111111        -6.666667
"""




"""
Using .map() with a dictionary
100xp

The .map() method is used to transform values according to a Python dictionary look-up. In this exercise you'll practice this method while returning to working with the election DataFrame, which has been pre-loaded for you.

Your job is to use a dictionary to map the values 'Obama' and 'Romney' in the 'winner' column to the values 'blue' and 'red', and assign the output to the new column 'color'.
Instructions

    Create a dictionary with the key:value pairs 'Obama':'blue' and 'Romney':'red'.
    Use the .map() method on the 'winner' column using the red_vs_blue dictionary you created.
    Print the output of election.head(). This has been done for you, so hit 'Submit Answer' to see the new column!

"""
# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue','Romney':'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election.winner.map(red_vs_blue)

# Print the output of election.head()
print(election.head())
""" results or consol output
<script.py> output:
              state   total      Obama     Romney  winner  voters color
    county
    Adams        PA   41973  35.482334  63.112001  Romney   61156   red
    Allegheny    PA  614671  56.640219  42.185820   Obama  924351  blue
    Armstrong    PA   28322  30.696985  67.901278  Romney   42147   red
    Beaver       PA   80015  46.032619  52.637630  Romney  115157   red
    Bedford      PA   21444  22.057452  76.986570  Romney   32189   red

"""





"""
Using vectorized functions
100xp

When performance is paramount, you should avoid using .apply() and .map() because those constructs perform Python for-loops over the data stored in a pandas Series or DataFrame. By using vectorized functions instead, you can loop over the data at the same speed as compiled code (C, Fortran, etc.)! NumPy, SciPy and pandas come with a variety of vectorized functions (called Universal Functions or UFuncs in NumPy).

You can even write your own vectorized functions, but for now we will focus on the ones distributed by NumPy and pandas.

In this exercise you're going to import the zscore method from scipy.stats and use it compute the deviation in voter turnout in Pennsylvania from the mean in fractions of the standard deviation. In statistics, the z-score is the number of standard deviations by which an observation is above the mean - so if it is negative, it means the observation is below the mean.

Instead of using .apply() as you did in the earlier exercises, the zscore UFunc will take a pandas Series as input and return a NumPy array. You will then assign the values of the NumPy array to a new column in the DataFrame. You will be working with the election DataFrame - it has been pre-loaded for you.
Instructions

    Import zscore from scipy.stats.
    Call zscore with election['turnout'] as input .
    Print the output of type(turnout_zscore). This has been done for you.
    Assign turnout_zscore to a new column in election as 'turnout_zscore.
    Print the output of election.head(). This has been done for you, so hit 'Submit Answer' to view the result.

"""
# Import zscore from scipy.stats
from scipy.stats import zscore

# Call zscore with election['turnout'] as input: turnout_zscore
turnout_zscore = zscore(election['turnout'])

# Print the type of turnout_zscore
print(type(turnout_zscore))
print('------------------')

# Assign turnout_zscore to a new column: election['turnout_zscore']
election['turnout_zscore'] = turnout_zscore

# Print the output of election.head()
print(election.head())
""" results or consol output
<script.py> output:
    <class 'numpy.ndarray'>
    ------------------
              state   total      Obama     Romney  winner  voters    turnout  \
    county
    Adams        PA   41973  35.482334  63.112001  Romney   61156  68.632677
    Allegheny    PA  614671  56.640219  42.185820   Obama  924351  66.497575
    Armstrong    PA   28322  30.696985  67.901278  Romney   42147  67.198140
    Beaver       PA   80015  46.032619  52.637630  Romney  115157  69.483401
    Bedford      PA   21444  22.057452  76.986570  Romney   32189  66.619031

                  margin  turnout_zscore
    county
    Adams      27.629667        0.853734
    Allegheny  14.454399        0.439846
    Armstrong  37.204293        0.575650
    Beaver      6.605012        1.018647
    Bedford    54.929118        0.463391
"""
