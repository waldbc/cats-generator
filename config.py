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

    },

    {
        'id': 2,
        'folder': 'Body',
        'rarities': [1, 10, 65, 20, 4],
    },

    {
        'id': 3,
        'folder': 'Bottom_Accessory',
        'rarities': [2, 10, 85, 3],
    },

    {
        'id': 4,
        'folder': 'Eyes',
        'rarities': [2, 8, 14, 2, 1, 7, 3, 4, 7, 3, 5, 12, 12, 5, 9, 6],
    },

    {
        'id': 5,
        'folder': 'Mouth',
        'rarities': [14, 12, 5, 12, 2, 14, 16, 10, 14, 1],
    },

    {
        'id': 6,
        'folder': 'Top_Accessory',
        'rarities': [14, 9, 6, 4, 7, 1, 5, 5, 6, 3, 8, 8, 12, 12],
    }
]
