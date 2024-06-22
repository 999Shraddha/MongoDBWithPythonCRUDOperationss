from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mydb
students = db.students
print(db)
# To insert
students_1 = {
    'Name': 'Jenny',
    'Address': 'Paris',
    'Course': 'Bsc.CSIT'
    
}
students_2 = {
      'Name': 'Merry',
    'Address': 'London',
    'Course': 'Psychology'
  } 
students.insert_one(students_1)
students.insert_one(students_2)

# To read a data
students_1 = students.find_one()
print(students_1)

# To update
students.update_one({"Name": "Jenny"}, {"$set": {"Course": "Psychology"}})
students_1 = students.find()
print(list(students_1))

# To delete
students.delete_one({"Name": "Merry"})
students_1 = students.find()
print(list(students_1))




