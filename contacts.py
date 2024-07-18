contacts = {
    'number': 4,
    'students':
        [{'name':'Tom', 'email':'tom@email.com'}, 
         {'name':'Gerry', 'email':'gerry@email.com'},
         {'name':'Amy', 'email':'amy@email.com'},
         {'name':'Gio', 'email':'gio@email.com'}]
}
print("Student emails:")
for student in contacts['students']:
    print(f"{student['name']:10} : {student['email']}")



         
