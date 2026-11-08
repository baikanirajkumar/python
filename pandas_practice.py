import pandas
# print(pandas.__version__)


#load data from csv file
import pandas as pd
d=pd.read_csv("C:/Users/baika/OneDrive/Desktop/covid.csv")
df=pd.DataFrame(d)
print(df)  #if it is csv use it 

# #load data from excel file
# #if it is excel file use it
# import pandas as pd
# d=pd.read_excel("filepath/filename.xlsx")
# df=pd.DataFrame(d)
# print(df)

#create a dataframe using dictionary
import pandas as pd
# di={"name":["raj","kumar","ramesh"],"rollno":[1,2,3],"percentage":[90,30,40]}
# df=pd.DataFrame(di)
# print(df)


#create a dataframe using list of tuples
# l=[("rajkumar",67.0,56),("ramesh",89.7,89),("tharun",89.8,76)]
# df=pd.DataFrame(l)
# print(df)


#indexing slicing
# b=df.head() #first five reocrds
# print(b)

# b=df.head(3)
# print(b)


# c=df.tail() #last five records
# print(c)

# c=df.tail(3) #last 3 records
# print(c)


# b=df.describe() #return count,mean,std,min,25%,50%,75%,max
# print(b)


# b=df.shape #return no of rows and columns
# print(b)

# b=df[0:10:1] #indexing
# print(b)

# b=df["Population"] #dataframe["columnname"]
# print(b)

# b=df[["State/UTs","Population"]] #dataframe[["column1","column2"]]
# print(b)

# b=df[["State/UTs","Population"]][0:5:1]
# print(b)

# for row in df.iterrows(): #return every row separately
#     print(row)

# b=df.loc[1] # acessing using row number(starting row number is 0)
# print(b)

# b=df.loc[1,["State/UTs","Population"]] 
# print(b)

# b=df.loc[0:5] #start and end is included
# print(b)




# b=df.loc[0:2,["State/UTs","Population"]] #dataframe.loc[start:stop,["column1","column2",.....]]
# print(b)

#difference between loc and iloc
# b=df.loc[1:5] # stop index is included
# print(b)
# c=df.iloc[1:5] #stop index is excluded
# print(c)


# b=df.loc[0:5,["State/UTs","Population"]]
# print(b)


# b=df.head()
# print(b)


# b=df.loc[0:5,"Total Cases":"Population"]
# print(b)


#understanding iloc(stop index will be excluded)
"""in loc column can be accessed using the column name 
but in iloc column can be accessed  using index"""

#data_frame.iloc[row_number,column_number]
# b=df.iloc[2,1]  # 2nd row 1st column(row starts with 0 index and column starts with 0 index)
# print(b)


#data_frame.iloc[row_start:row_stop,column_start:column_stop]
# b=df.iloc[0:3,0:3] #upto to second row and return up to second column
# print(b)

#data_frame[start:stop,column_number]
# b=df.iloc[0:3,1]
# print(b)


#dataframe.iloc[[row1,row2]]
# b=df.iloc[[1,4]] #1st row and 2nd row
# print(b)

#dataframe[:,[col_1,col_2]]
# b=df.iloc[:,[0,3]]  #all rows and 0th column and 3rd column 
# print(b)

#dataframe.iloc[start:stop,[col_1,col_2]]
# b=df.iloc[0:5,[1,2]]
# print(b)


#sorting dataframe

#data_frame.sort_values("column_name")
# b=df.sort_values("Population") #ascending order
# print(b)

#data_frame.sort_values("column_name",ascending=False)
# b=df.sort_values("Population",ascending=False)
# print(b)

#data_frame.sort_values(["column1","column2"])
# b=df.sort_values(["State/UTs","Population"]) #based on the first column name it will be sorted
# print(b)

#manipulating dataframe
#adding column
#data_frame[column_name]=default_value
b=df["count"]=0
print(b)

b=df.head
print(b)

#data_frame[column_name]=expression/condition
#adding all columns into one column
#sample example to count from youtube 
# b=df["Total"]=df["Telugu"]+df["english"]+df["maths"]
# print(b)

# #removing column
# b=df["per"]="Pass/fail" #created column
# print(b)

# df.drop(columns="count")
# print(b)

b=df["marks"]=12
print(b)






