#date and time
# import datetime #importing the datetime module

#working with dates
# from datetime import date
# today=date.today()
# print(today)

#creating the specific Date
# specific_date=date(2026,3,23)
# print(specific_date)

#extracting year,month,day
# from datetime import date
# print(today.year)


#file handling in python(chatgpt:revature_snowflake file)
"""File handling is the process of creating,opening,
 reading,writing,appending and closing files in python"""
#1.opening the file
#syntax
# file=open("filename.txt","mode")

"""Mode	    Description
"r"	        Read (default). File must exist.
"w"	        Write. Creates a new file or overwrites an existing file.
"a"	        Append. Adds data to the end of the file.
"x"	        Create a new file. Raises an error if the file already exists.
"r+"	    Read and write.
"w+"	    Read and write. Overwrites the file.
"a+"	    Read and append.
"rb"	    Read a binary file.
"wb"	    Write a binary file
"""

#Reading the file
#read the entire file
# file=open("C:/Users/baika/OneDrive/Desktop/student.txt","r")
# print(file.read())
# file.close()

#read the first 10 characters
# file=open("C:/Users/baika/OneDrive/Desktop/student.txt","r")
# print(file.read(10))
# file.close()


#read one line
# file=open("C:/Users/baika/OneDrive/Desktop/student.txt","r")
# print(file.readline())
# file.close()

#read all lines
# file=open("C:/Users/baika/OneDrive/Desktop/student.txt","r")
# print(file.readlines())
# file.close()
# #output:['hello Chennai\n', 'welcome to filehandling']


#writing to a file:overwrites an existing file
# file=open("C:/Users/baika/OneDrive/Desktop/student.txt","w")
# file.write("python is the programming language")
# file.close()

# file=open("C:/Users/baika/OneDrive/Desktop/student.txt","r")
# print(file.read())
# file.close()

# #Appending to a file
# file=open("C:/Users/baika/OneDrive/Desktop/student.txt","a")
# file.write("\niam from warangal")#here \n means newline
# file.close()

# file=open("C:/Users/baika/OneDrive/Desktop/student.txt","r")
# print(file.read())
# file.close()

#creating a new file
# file=open("rajkumar.txt","x")
# file.close()

# file=open("E:/python/rajkumar.txt","w")
# file.write("python is programming language")
# file.close()

# file=open("E:/python/rajkumar.txt","r")
# print(file.read())
# file.close()

# file=open("E:/python/rajkumar.txt","r")
# print(file.read(10))
# file.close()

# #7.closing a file
# file.close() #Always close the file after use to free system resorces

#8.Using with statement
# with open("E:/python/rajkumar.txt","r") as file:
#     print(file.read())
"""no need to call the close().python closes the file automatically"""



"""append to the end of the file"""
# with open("E:/python/rajkumar.txt","a") as file:
#     file.write("kiran")
#     file.write("rajkumar")
#     file.write("ramu")


# #9.loop through  a file
# with open("E:/python/rajkumar.txt","r") as file:
#     for line in file:
#         print(line.strip())

#10.File pointer methods
"""tell():
Returns the current cursor position"""
# file=open("E:/python/rajkumar.txt","r")
# print(file.tell())


# seek()
"""Moves the cursor to a specific position"""
# file=open("E:/python/rajkumar.txt","r")
# print(file.seek(5))
# print(file.read())

#11.check if file exists
# import os
# if os.path.exists("E:/python/rajkumar.txt"):
#     print("file exists")
# else:
#     print("file not found")


#13.rename a file
import os
os.rename("E:/python/rajkumar.txt","E:/python/raj.txt")

#14.Delete a file
import os
os.remove("E:/python/rajkumar.txt")

# import os 
# print(os.getcwd())



