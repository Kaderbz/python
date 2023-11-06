employees = [
    {
    "id": 11,
    "name":"Abhinav",
    "salary":75000
    },
    {
    "id": 2131,
    "name":["Raj","ed","sth"],
    "salary":62000
    },
    {
    "id": 3012,
    "name":"Raj",
    "salary":32000
    }]
print(employees[0]["id"])
for i in range(len(employees)):
    for key in employees[i]:
        print(f"{key}")
print(employees[1]["name"][2])