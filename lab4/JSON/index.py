import json

with open("example.json", "r") as json_file:
    a = json.load(json_file)
    
print("Has pet:", a["has_pet"])
print("Hobbies:", a["hobbies"])

del a["favorite_foods"]["perekus"]

a["Mass"] = [1, "h", {"a": 1}, [1, 2, 3]]
print(a) # В данном случае мы работаем с питоновским словарем, а не с JSON кодом 
print()

print(json.dumps(a)) # Представляем словарь в виде Джейсона
print()

print(json.dumps(a, indent = 2)) # Добавляем отступы

# Записываем данные в файл Джейсон
with open("example.json", "w") as json_file:
    json.dump(a, json_file, indent=4)