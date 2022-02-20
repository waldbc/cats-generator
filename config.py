""" Initialises layers for use in the program.
    Make sure to type the exact directory name into the folder value.

    Rarity weights are based on the order of the images in each folder, typically
    alphabetical.
"""
layers = [
    {
        'id': 1,
        'folder': 'Background',
        'rarities': [3, 14, 14, 14, 14, 14, 3, 8, 8, 8],
        'required': True,

    },

    {
        'id': 2,
        'folder': 'Body',
        'rarities': [1, 10, 65, 20, 4],
        'required': True,
    },

    {
        'id': 3,
        'folder': 'Bottom_Accessory',
        'rarities': [20, 10, 20, 50],
        'required': False,
    },

    {
        'id': 4,
        'folder': 'Eyes',
        'rarities': [2, 8, 14, 2, 1, 7, 3, 4, 7, 3, 5, 12, 12, 5, 9, 6],
        'required': True,
    },

    {
        'id': 5,
        'folder': 'Mouth',
        'rarities': [14, 12, 5, 12, 2, 14, 16, 10, 14, 1],
        'required': True,
    },

    {
        'id': 6,
        'folder': 'Top_Accessory',
        'rarities': [14, 9, 6, 4, 7, 1, 5, 5, 6, 3, 8, 8, 12, 12],
        'required': False,
    }
]
