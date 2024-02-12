lst = ['Malayalam', 'Drawing', 'madamIamadam', '1234321']

nlst=list(filter(lambda x:x.lower()==x.lower()[::-1],lst))

print(nlst)










employees = {
   1: {"first_name": "John", "last_name": "Doe", "age": 30, "grade": "Highly-skilled"},
    2:{"first_name": "Jane", "last_name": "Smith", "age": 25, "grade": "Skilled"},
    3:{"first_name": "Bob", "last_name": "Johnson", "age": 35, "grade": "Semi-skilled"},
    4:{"first_name": "Alice", "last_name": "Williams", "age": 28, "grade": "Highly-skilled"},
    5:{"first_name": "Charlie", "last_name": "Brown", "age": 40, "grade": "Semi-skilled"}
}


highs=list(map(lambda x:x["first_name"]+ " " +x["last_name"],
               filter(lambda x:x["grade"]=="Highly-skilled",employees.values())))

for name in highs:
    print(name)
