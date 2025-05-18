# %%
import json


def load_data(file_path):
    """
    Load data from a JSON file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def select_skin_type(animals):
    """
    Prompt user to select a skin type and return it.
    """
    skin_types = set()

    for animal in animals:
        skin_type = animal.get('characteristics', {}).get('skin_type')
        # Skip if skin_type is missing or None
        if skin_type:
            skin_types.add(skin_type)
    
    skin_types = sorted(list(skin_types))
    print('\nList of Skin Types:')
    for i, skin_type in enumerate(skin_types, start=1):
        print(f'{i}. {skin_type}')
    
    # Create a lookup to handle case-insensitive user input 
    skin_type_lookup = {s.lower(): s for s in skin_types}

    while True:
        user_input = input('\nEnter skin type to filter animals: ').strip().lower()

        if user_input in skin_type_lookup:
            return skin_type_lookup[user_input]
        else:
            print('Invalid input. Please choose from the displayed list.')


def generate_animals_info(animals, skin):
    """
    Generate HTML list items for animals matching the selected skin type.
    """
    # Define empty string
    output = ''

    # Tracks if at least one matching animal was found
    found = False

    for animal in animals:
        if animal.get('characteristics').get('skin_type') == skin:
            output += serialize_animal(animal)
            found = True
    
    if not found:
        output = '<p>No animal found for that skin type!</p>\n'

    return output


def serialize_animal(animal):
    """
    Convert a single animal's data into an HTML list item string.
    """
    output = ''
    output += ' <li class="cards__item">\n'

    if animal.get('name'):
        output += '     <div class="card__title">{}</div>\n'.format(animal['name'])
    output += '     <div class="card__text">\n'
    output += '         <ul>\n'

    taxonomy = animal.get('taxonomy', {})
    characteristics = animal.get('characteristics', {})
    locations = animal.get('locations', [])

    if taxonomy.get('scientific_name'):
        output += '             <li><strong>Scientific Name:</strong> {}</li>\n'.format(taxonomy['scientific_name'])
    
    if characteristics.get('type'):
        output += '             <li><strong>Type:</strong> {}</li>\n'.format(characteristics['type'])
    
    if characteristics.get('skin_type'):
        output += '             <li><strong>Skin Type:</strong> {}</li>\n'.format(characteristics['skin_type'])
    
    if characteristics.get('diet'):
        output += '             <li><strong>Diet:</strong> {}</li>\n'.format(characteristics['diet'])
    
    if locations and locations[0]:
        output += '             <li><strong>Location:</strong> {}</li>\n'.format(locations[0])
    
    if characteristics.get('slogan'):
        output += '             <li><strong>Slogan:</strong> {}</li>\n'.format(characteristics['slogan'])

    output += '         </ul>\n'
    output += '     </div>\n'
    output += ' </li>\n'

    return output


def read_template(file_path):
    """
    Read and return HTML template content from a file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def merge_template_with_data(template_str, animal_info_str):
    """
    Insert animal info into the HTML template placeholder.
    """
    return template_str.replace("__REPLACE_ANIMALS_INFO__", animal_info_str)


def write_to_file(file_path, content):
    """
    Write the final HTML content as a file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print("HTML file successfully generated :)")


def main():
    """
    Main program flow: 
    load data, filter by skin type, 
    generate and save HTML.
    """
    animals_data = load_data('animals_data.json')
    skin_type = select_skin_type(animals_data)
    animal_info = generate_animals_info(animals_data, skin_type)
    template = read_template('animals_template.html')
    animals_html = merge_template_with_data(template, animal_info)
    write_to_file('animals.html', animals_html)
    

if __name__ == "__main__":
    main()
