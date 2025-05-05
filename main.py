# %%
import json


def load_data(file_path):
    """
    Load data from a JSON file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def generate_animals_info(animals):
    """
    Return a string with animal info.
    """
    # Define empty string
    output = ''

    for animal in animals:
        output += '<li class="cards__item">'

        name = animal.get('name')
        if name:
            output += f"<strong>Name:</strong> {name}<br>"
        
        diet = animal.get('characteristics', {}).get('diet')
        if diet:
            output += f"<strong>Diet:</strong> {diet}<br>"

        location = animal.get('locations', [])
        if location:
            output += f"<strong>Location:</strong> {location[0]}<br>"

        animal_type = animal.get('characteristics', {}).get('type')
        if animal_type:     
            output += f"<strong>Type:</strong> {animal_type}<br>"
        
        # blank line after each animal
        output += '</li>'

    return output


def read_template(file_path):
    """
    Read content of HTML template file and return it as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def merge_template_with_data(template_str, animal_info_str):
    """
    Replace placeholder in HTML template with animal info string.

    Params:
        template_str (str): HTML template content as a string.
        animal_info_str (str): Formatted string containing animal info.

    Returns:
        str: The final HTML content with animal data inserted.
    """
    return template_str.replace("__REPLACE_ANIMALS_INFO__", animal_info_str)


def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    animals_data = load_data('animals_data.json')
    animal_info = generate_animals_info(animals_data)
    # print(animal_info)
    template = read_template('animals_template.html')
    animals_html = merge_template_with_data(template, animal_info)

    write_to_file('animals.html', animals_html)
    

if __name__ == "__main__":
    main()


# %%
