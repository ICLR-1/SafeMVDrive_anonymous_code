import json
json_path=""
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
total_distance=0.0
for item in data:
    distance = item["min_distance"]
    total_distance+=distance
avg_distance= total_distance/float(len(data))
print("escape_scene_number:",len(data))
print("avg_distance:",avg_distance)
