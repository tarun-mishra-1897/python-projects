import numpy as np
print(np.__version__)
# theory question
#1. What is NumPy, and why is it widely used in Python?

#ans.>> numpy is very powerful library in python for numerical calculations
#     1. it gives efficent array of an object 
#     2. it is useful in mathematical  and statistical functions
#     3. from numpy we will able to access other library funcios(it is backbone of other library like pandas,matplotlib etc)

#2. How does broadcasting work in NumPy?

#ans.>> numpy allows to perform operations between different data of array in shapes without copying such data and numpy do faster calculaions and memory efficent

#3. What is a Pandas DataFrame?

#ans.>> in pandas , dataframe is 2d data frame , it is uses for data manipulation and analysis of data easly. it consist of rows and columns

#4. Explain the use of the groupby() method in Pandas.

#ans.>> groupby method is used when we need to group the data based on one or more rows and columns and then apply functions like sum,mean,min etc

#5. Why is Seaborn preferred for statistical visualizations?

#ans.>> we use seaborn for statistical visualizations because :-
#      1. Supports statistical plots like boxplots, violin plots, etc.
#      2. Makes complex visualizations simpler

#6. What are the differences between NumPy arrays and Python lists?

#ans.>> 1. numpy array :- >> it is used when the data types of such data is same,
#                         >> it is faster then python lists , thats is why it uses less memory

#       2. python list :- >> it can be used in mixed data type 
#                         >> it is slower then numpy's array , and it uses more memory usage

#7. What is a heatmap, and when should it be used?

#ans.>> heatmap is 2D visualization of data , it is used to repersente values of data and such value is alloted by different colour 
# it is used for spotting patterns of data and best repersentation for correlation metrices

#8. What does the term “vectorized operation” mean in NumPy?

#ans.>> Vectorized operations allow array-wide computations without using loops, 
#       making them much faster and more readable (e.g., a + b for two arrays).

#9. How does Matplotlib differ from Plotly?

#ans.>> a. matplotlib :- 1. in this results and graphs are static means we are not able to edit like plotly
#                        2. in this we need more code to perform a functions
#                        3. in this results are image , live editing , zoomin ,zoomout not possible

#      b. plotly :-     1. in this results and graphs are not static means Interactive (zoom, hover) is possible
#                       2. we use this for Simpler for modern visuals
#                       3. in this results are Web-based charts

#10. What is the significance of hierarchical indexing in Pandas?

#ans.>> hierarchical indexing means multiple level indexing , in pandas it is allow to do multiple level indexing in rows and columns
#       it's best practice for working with grouped or multi-dimensional data.

# 11. What is the role of Seaborn’s pairplot() function?

#ans.>> pairplot is used for represente a relationship between numeric variable in dataset . it helps us to understanding correaltion , it is also helps in EDA

# 12. What is the purpose of the describe() function in Pandas?

#ans.>> describe() gives us statical summary of numerical columns of such dataset
#       statical summary means  >> count, mean, std, min, max, etc

#13. Why is handling missing data important in Pandas?

#ans.>> missing data handling is very important in pandas because :-
#       error is output when there is no values in columns so removing null values from data we use dropna() method to avoid errors

#14. What are the benefits of using Plotly for data visualization?

#ans.>> these are the benefits of using plotly for data visualization :-
#      1.it is interactive and user-friendly 
#      2.it is best for making dashboards and web pages
#      3.it supports 3D and map visualization 

#15. How does NumPy handle multidimensional arrays?

#ans.>>NumPy uses ndarrays that can be of any dimension (1D, 2D, 3D…). Operations are applied efficiently using broadcasting and slicing.

#16. What is the role of Bokeh in data visualization?

#ans.>>bokeh is simillar to plotly , it is used for building interactive, web-ready visualizations. It’s good for:
#      1. Real-time data
#      2. Interactive dashboards

17.# Explain the difference between apply() and map() in Pandas.

#ans.>> 1. map(): Used with Series for element-wise operations.
#       2. apply(): Used with DataFrame or Series for applying custom functions row-wise or column-wise.

#18. What are some advanced features of NumPy?

#ans.>> these are the advance function in numpy :-
#      1.Linear algebra (np.linalg)
#      2.Random number generation (np.random

#19. How does Pandas simplify time series analysis?

#ans.>>Pandas has:
#    1. Date/time indexing
#    2. Resampling (resample())
#    3. Rolling windows (rolling())
#    4. Shifting/lagging data (shift())

# 20. What is the role of a pivot table in Pandas?

#ans.>> Pivot tables are used to:
#     1.Summarize large datasets
#     2.Group and aggregate data
#     3.Reshape data for analysis

#21. Why is NumPy’s array slicing faster than Python’s list slicing?

#ans.>>because numpy array uses contigous memory blocks and optimized with code, allowing slicing to return views (not copies), which making it faster.

#22. What are some common use cases for Seaborn?

#ans.>> these are the some common use cases of seaborn :-
#      1. to present correlation heatmap
#      2. to distribution plotting( histogram )
#      3. to Categorical plots (bar, box, violin)
#      4.to Regression plots

# practical question......

import numpy as np
print(np.__version__)
#1. How do you create a 2D NumPy array and calculate the sum of each row?


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_sums = np.sum(arr, axis=1)
print("Sum o f each row:", row_sums)

#2. Write a Pandas script to find the mean of a specific column in a DataFrame

import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [24, 27, 22, 25],
    'Score': [85, 90, 78, 88]
}

df = pd.DataFrame(data)

# Find the mean of the 'Score' column
mean_score = df['Score'].mean()

print("Mean of the 'Score' column:", mean_score)

#3. Create a scatter plot using Matplotlib

import matplotlib.pyplot as plt

# Data points for the scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Create scatter plot
plt.scatter(x, y, color='blue', label='Data Points')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Scatter Plot')
plt.legend()

# Display the plot
plt.show()

#4.How do you calculate the correlation matrix using Seaborn and visualize it with a heatmap?
import seaborn as sns
df = sns.load_dataset("iris")
corr = df.corr(numeric_only = True)
sns.heatmap(corr , annot = True , cmap = "coolwarm")
plt.title("correlation heatmap visualization")
plt.show()

#5.Generate a bar plot using Plotly
import plotly.graph_objects as go
import plotly.express as px
fig = go.Figure()
fig.add_trace(go.Bar(x=[1,3,6,8],y=[4,5,3,9]))

#6.Create a DataFrame and add a new column based on an existing column.

import pandas as pd
data = pd.DataFrame({"student" :["a","b","c"],"marks" : [67,54,86]})
data["status"] = data["marks"].apply(lambda x : "pass" if x >60 else "fail")
data

#7.Write a program to perform element-wise multiplication of two NumPy arrays.
# element wise multplication means index-wise multiplication
a = np.array([[1, 2, 3],
              [0,3,5]])
b = np.array([[4, 5, 6],
            [1,4,8]])
a*b

#8.Create a line plot with multiple lines using Matplotlib
x = [1, 2, 3, 4, 5]
y1 = [5, 1, 7, 8, 2]
y2 = [7, 8, 3, 5, 1]
plt.plot(x,y1,color="green",marker="o",linestyle="--",linewidth = 1,markersize=5,label= "y1 is for tata motors")
plt.plot(x,y2,color="blue",marker="o",linestyle="--",linewidth = 1,markersize=5,label="y2 is for tata power")

plt.title("multiple line in one plot")
plt.xlabel(" days")
plt.ylabel("stok price")
plt.legend()
plt.grid()
plt.show()

#9. Generate a Pandas DataFrame and filter rows where a column value is greater than a threshold

data = pd.DataFrame({"student" :["a","b","c"],"marks" : [67,54,86]})
filtered_data = data[data["marks"] > 60]
filtered_data 

#10. Create a histogram using Seaborn to visualize a distribution
x = [3,2,5,7,4,7,8]
sns.histplot(x , bins = 8 , kde = True)

#11. Perform matrix multiplication using NumPy
a = np.array([[1, 2, 3],
              [0,3,5],
             [1,3,4]])
b = np.array([[4, 5, 6],
              [3,5,7],
            [1,4,8]])
a@b

#12. Use Pandas to load a CSV file and display its first 5 rows


#13. Create a 3D scatter plot using Plotly

fig = go.Figure()
fig.add_trace(go.Scatter3d(x = [1,2,3,4] , y = [3,5,6,2] , z = [4,7,1,5] ))
fig.show()














