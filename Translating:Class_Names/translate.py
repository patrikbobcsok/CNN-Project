translate = {"cane": "dog",
             "cavallo": "horse", 
             "elefante": "elephant", 
             "farfalla": "butterfly", 
             "gallina": "chicken", 
             "gatto": "cat", 
             "mucca": "cow", 
             "pecora": "sheep",
             "ragno": "spider", 
             "scoiattolo": "squirrel"}
import json

# Translated class names
translated_class_names = ['dog', 'horse', 'elephant', 'butterfly', 'chicken', 
                          'cat', 'cow', 'sheep', 'spider', 'squirrel']

# Save to JSON file
with open("class_names.json", "w") as f:
    json.dump(translated_class_names, f)

print("✅ Translated class names saved.")