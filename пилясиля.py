import json
from idlelib.iomenu import encoding

#cтудия маникюра "ногтеточки у кошечки"
bd_odin = [
    {"id": 1, "name": "Евкакия", "age": 11},
    {"id": 2, "name": "Зелеколия", "age": 67},
    {"id": 3, "name": "Любаня", "age": 22},
    {"id": 4, "name": "Светлана", "age": 32},
    {"id": 5, "name": "Юлианна", "age": 21}
]

bd_dva = [
    {"id": 1, "design": "сложный"},
    {"id": 2, "design": "лёгкий"},
    {"id": 3, "design": "сложный"},
    {"id": 4, "design": "средний"},
    {"id": 5, "design": "сложный"}
]

bd_tri = [
    {"id": 1, "bolezn": "здоровые ногти"},
    {"id": 2, "bolezn": "онихилис"},
    {"id": 3, "bolezn": "здоровые ногти"},
    {"id": 4, "bolezn": "лейкохиния"},
    {"id": 5, "bolezn": "сифилис"}
]

with open ("пилясиля.json", "w", encoding="utf-8") as f:
    json.dump(bd_odin, f, ensure_ascii=False, indent=2)

with open("табл2.json", "w", encoding="utf-8") as f:
    json.dump(bd_dva, f, ensure_ascii=False, indent=2)

with open ("нупж.json", "w", encoding="utf-8") as f:
    json.dump(bd_tri, f, ensure_ascii=False, indent=2)