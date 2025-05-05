# %%
import json

def load_data(file_path):
    """
    Load data from a JSON file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

animals_data = load_data('animals_data.json')
# print(json.dumps(animals_data, indent=4))

# %%
def print_animal_data(animals):
    """
    Print the animal data in a formatted way.
    """
    for animal in animals:
        name = animal.get('name')
        if name:
            print(f"Name: {name}")
        
        diet = animal.get('characteristics', {}).get('diet')
        if diet:
            print(f"Diet: {diet}")

        location = animal.get('locations', [])
        if location:
            print(f"Location: {location[0]}")

        animal_type = animal.get('characteristics', {}).get('type')
        if animal_type:     
            print(f"Type: {animal_type}")
        print()

print_animal_data(animals_data)
    

# %%
