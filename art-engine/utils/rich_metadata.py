""" Adds a trait count and frequency % to the metadata of each token. """

import json

from parse_yaml import read_yaml


def create_counts() -> dict:

    attributes_count = dict()
    config_file = read_yaml()

    amount = config_file['amount']

    if config_file['id_from_one']:
        edition = 1
    else:
        edition = 0

    for _ in range(amount):

        json_path = f'build/json/{edition}.json'

        with open(json_path, 'r', encoding='utf-8') as infile:

            data = json.load(infile)
            token_attributes = data['attributes']

            for attr in token_attributes:
                attr_key = (attr['trait_type'], attr['value'])
                if attr_key not in attributes_count:
                    attributes_count[attr_key] = 1
                else:
                    attributes_count[attr_key] += 1

        edition += 1

    return attributes_count


def calculate_percentages() -> dict:

    config_file = read_yaml()
    amount = config_file['amount']
    attributes_count = create_counts()
    attribute_percentages = dict()

    def percent(count): return (count / amount) * 100

    for attribute in attributes_count:
        freq_percent = percent(attributes_count[attribute])
        freq_percent = round(freq_percent, 3)

        attribute_percentages[attribute] = f'{freq_percent}%'

    return attribute_percentages


def update_metadata(attribute_count: dict, attribute_freq: dict) -> None:

    config_file = read_yaml()
    amount = config_file['amount']

    if config_file['id_from_one']:
        edition = 1
    else:
        edition = 0

    for _ in range(amount):

        json_path = f'build/json/{edition}.json'

        with open(json_path, 'r', encoding='utf-8') as infile:

            data = json.load(infile)
            token_attributes = data['attributes']

            for attr in token_attributes:
                attr_key = (attr['trait_type'], attr['value'])

                count = attribute_count[attr_key]
                freq = attribute_freq[attr_key]

                attr['count'] = count
                attr['frequency'] = freq

        data['attributes'] = token_attributes

        # Opens the original json file and writes the new data
        with open(json_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=2)

        edition += 1


update_metadata(create_counts(), calculate_percentages())
