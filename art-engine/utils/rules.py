
class IgnoreLayer(Exception):
    pass


def rule0(layer_name: str, final_layers: dict, layer_images: list, rarities: list) -> (list, list):
    """A dummy rule."""
    return layer_images, rarities


def rule1(layer_name: str, final_layers: dict, layer_images: list, rarities: list) -> (list, list):
    """1. Якщо Uniform не none – використовувати у слоях Casual top, Casual pants та Hat тільки none."""
    condition_layer = "Trait7_Uniform"
    target_layers = ["Trait8_Casual_pants", "Trait9_Casual_top", "Trait11_Hat"]

    if layer_name not in target_layers:
        return layer_images, rarities

    if final_layers[condition_layer] != "None":
        layer_images = ["None"]
        rarities = [100] if rarities is not None else None

    return layer_images, rarities


def rule2(layer_name: str, final_layers: dict, layer_images: list, rarities: list) -> (list, list):
    """2. Якщо у Eyes не Ukrainian – не використовувати Bounty hunter та Ranger у Uniform."""
    condition_layer = "Trait4_Eyes"
    target_layers = ["Trait7_Uniform"]

    if layer_name not in target_layers:
        return layer_images, rarities

    if final_layers[condition_layer] != "None" and \
            final_layers[condition_layer].name == "Ukrainian.png":
        return layer_images, rarities

    filtered_layer_images = []
    filtered_rarities = [] if rarities is not None else None

    for index, image in enumerate(layer_images):
        if image != "None" and image.name in ["Bounty-hunter.png", "Ranger.png"]:
            continue

        # keep values
        filtered_layer_images.append(image)
        if rarities is not None:
            filtered_rarities.append(rarities[index])

    return filtered_layer_images, filtered_rarities


def rule3(layer_name: str, final_layers: dict, layer_images: list, rarities: list) -> (list, list):
    """3. Якщо Uniform = none, Bounty hunter або Ranger – не використовувати слой Vest."""
    condition_layer = "Trait7_Uniform"  # OK
    target_layers = ["Trait10_Vest"]

    if layer_name not in target_layers:
        return layer_images, rarities

    if final_layers[condition_layer] != "None" and \
            final_layers[condition_layer].name not in ["Bounty-hunter.png", "Ranger.png"]:
        return layer_images, rarities

    layer_images = ["None"]
    rarities = [100] if rarities is not None else None

    return layer_images, rarities


# class Rule(ABC):
#     condition_layer: str
#     target_layers: list[str]
#
#     @classmethod
#     @abstractmethod
#     def ignore_rule_condition(cls) -> bool:
#         pass
#
#     @classmethod
#     @abstractmethod
#     def filter_images(cls) -> (list, list):
#         pass
#
#     @classmethod
#     def apply(cls, layer_name: str, final_layers: dict, layer_images: list, rarities: list) -> (list, list):
#
#         # ignore other layers
#         if layer_name not in cls.target_layers:
#             return layer_images, rarities
#
#         # check for the rule condition
#         if cls.ignore_rule_condition():
#             return layer_images, rarities
#
#         filtered_layer_images, filtered_rarities = cls.filter_images()
#
#         return filtered_layer_images, filtered_rarities


# def rule4(layer_name: str, final_layers: dict, layer_images: list, rarities: list) -> (list, list):
#     """4. Якщо Uniform = Bounty hunter або Ranger – не використовувати слої Accessory Mouth та Accessory face."""
#     condition_layer = "Trait7_Uniform" !!!!!
#     target_layers = ["Trait5_Accessory_mouth", "Trait6_Accessory_face"]
#
#     if layer_name not in target_layers:
#         return layer_images, rarities
#
#     if (final_layers["Trait7_Uniform"] == "None") \
#             or (final_layers["Trait7_Uniform"].name not in ["Bounty-hunter.png", "Ranger.png"]):
#         return layer_images, rarities
#
#     layer_images = ["None"]
#     rarities = [100] if rarities is not None else None
#
#     return layer_images, rarities
