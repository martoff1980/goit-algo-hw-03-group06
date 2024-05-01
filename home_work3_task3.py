n = 3
disks = {
    "A": list(val for val in range(n, 0, -1)),
    "B": [],
    "C": []
}


print("Початковий стан:", disks)  # {'A': [3, 2, 1], 'B': [], 'C': []}")
print("Перемістити диск з A на C: 1")
disks["C"].append(disks["A"].pop())
print("Проміжний стан:", disks)  # {'A': [3, 2], 'B': [], 'C': [1]}"
print("Перемістити диск з A на B: 2")
disks["B"].append(disks["A"].pop())
print("Проміжний стан:", disks)  # {'A': [3], 'B': [2], 'C': [1]}"
print("Перемістити диск з C на B: 1")
disks["B"].append(disks["C"].pop())
print("Проміжний стан:", disks)  # "{'A': [3], 'B': [2, 1], 'C': []}"
print("Перемістити диск з A на C: 3")
disks["C"].append(disks["A"].pop())
print("Проміжний стан:", disks)  # {'A': [], 'B': [2, 1], 'C': [3]}"
print("Перемістити диск з B на A: 1")
disks["A"].append(disks["B"].pop())
print("Проміжний стан:", disks)  # {'A': [1], 'B': [2], 'C': [3]}"
print("Перемістити диск з B на C: 2")
disks["C"].append(disks["B"].pop())
print("Проміжний стан:", disks)  # "{'A': [1], 'B': [], 'C': [3, 2]}"
print("Перемістити диск з A на C: 1")
disks["C"].append(disks["A"].pop())
print("Проміжний стан:", disks)  # "{'A': [], 'B': [], 'C': [3, 2, 1]}"
print("Кінцевий стан:", disks)  # {'A': [], 'B': [], 'C': [3, 2, 1]}"
