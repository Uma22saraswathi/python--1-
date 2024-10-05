student={
    "name":"uma",
    "age":21,
    "rollno":54,
    "school":"tilak"
}
keys_to_delete=["rollno","school"]
for i in keys_to_delete:
    if i in student:
        del student[i]
print(student)        