"""what is json?
JSON(Javascript Object Notation is a lightweight format used tom store and exchange data)"""


"""which is module is used to work with jsonn in python?
The built in json module"""

""" Why is JSON important?
Easy to read and write.
Language-independent.
Widely used in REST APIs and web applications for data exchange."""

"""dump(): Saves a Python object into a JSON file.
   load(): Reads a JSON file and converts it into a Python object.
   dumps(): Converts a Python object into a JSON string.
   loads(): Converts a JSON string into a Python object."""


# #convert python object to JSON
# import json
# student={
#     "name":"rajkumar",
#     "rollno":14,
#     "branch":"cse"
# }
# obj=json.dumps(student)
# print(obj)
# print(type(obj))


#convert json string into python object
# import json
# student='''{
#     "name":"rajkumar",
#     "rollno":14,
#     "branch":"cse"
# }'''
# obj=json.loads(student)
# print(obj)
# print(type(obj))


# #dump
# import json
# student={
#     "name":"rajkumar",
#     "rollno":14,
#     "branch":"cse"
# }
# with open("student.json","w") as file:
#     json.dump(student,file)


#load()
import json
with open("student.json","r") as file:
    data=json.load(file)
print(data)