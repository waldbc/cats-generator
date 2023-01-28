from abc import abstractmethod, ABC


class RuleBase(ABC):
    condition_layer: str
    target_layers: list[str]

    @classmethod
    @abstractmethod
    def ignore_rule_condition(cls, final_layers: dict) -> bool:
        pass

    @classmethod
    @abstractmethod
    def filter_images(cls, layer_images: list, rarities: list) -> (list, list):
        pass

    @classmethod
    def apply(cls, layer_name: str, final_layers: dict, layer_images: list, rarities: list) -> (list, list):

        # ignore other layers
        if layer_name not in cls.target_layers:
            return layer_images, rarities

        # check for the rule condition
        if cls.ignore_rule_condition(final_layers):
            return layer_images, rarities

        filtered_layer_images, filtered_rarities = cls.filter_images(
            layer_images, rarities
        )

        return filtered_layer_images, filtered_rarities


class Rule0(RuleBase):
    condition_layer: str = "Trait1_Background"
    target_layers: list[str] = ["Trait11_Hat"]

    @classmethod
    def ignore_rule_condition(cls, final_layers: dict) -> bool:
        # never ignore
        return False

    @classmethod
    def filter_images(cls, layer_images: list, rarities: list) -> (list, list):
        # noop
        return layer_images, rarities


class Rule1(RuleBase):
    """1. Якщо Uniform не none – використовувати у слоях Casual top, Casual pants та Hat тільки none."""

    condition_layer: str = "Trait7_Uniform"
    target_layers: list[str] = ["Trait8_Casual_pants", "Trait9_Casual_top", "Trait11_Hat"]

    @classmethod
    def ignore_rule_condition(cls, final_layers: dict) -> bool:

        return final_layers[cls.condition_layer].name == "None"

    @classmethod
    def filter_images(cls, layer_images: list, rarities: list) -> (list, list):
        filtered_layer_images = ["None"]
        filtered_rarities = [100] if rarities is not None else None
        return filtered_layer_images, filtered_rarities


class Rule2(RuleBase):
    """2. Якщо у Eyes не Ukrainian – не використовувати Bounty hunter та Ranger у Uniform."""

    condition_layer: str = "Trait4_Eyes"
    target_layers: list[str] = ["Trait7_Uniform"]

    @classmethod
    def ignore_rule_condition(cls, final_layers: dict) -> bool:
        return final_layers[cls.condition_layer].name != "None" and \
            final_layers[cls.condition_layer].name == "Ukrainian.png"

    @classmethod
    def filter_images(cls, layer_images: list, rarities: list) -> (list, list):
        filtered_layer_images = []
        filtered_rarities = [] if rarities is not None else None

        for index, image in enumerate(layer_images):
            if image != "None" and image.name in [
                "Bounty-hunter.png",
                "Ranger.png"
            ]:
                continue

            # keep values
            filtered_layer_images.append(image)
            if rarities is not None:
                filtered_rarities.append(rarities[index])

        return filtered_layer_images, filtered_rarities


class Rule3(RuleBase):
    """3. Якщо Uniform = none, Bounty hunter або Ranger – не використовувати слой Vest."""

    condition_layer: str = "Trait7_Uniform"
    target_layers: list[str] = ["Trait10_Vest"]

    @classmethod
    def ignore_rule_condition(cls, final_layers: dict) -> bool:
        return final_layers[cls.condition_layer].name != "None" and \
            final_layers[cls.condition_layer].name not in [
                "Bounty-hunter.png",
                "Ranger.png"
            ]

    @classmethod
    def filter_images(cls, layer_images: list, rarities: list) -> (list, list):
        filtered_layer_images = ["None"]
        filtered_rarities = [100] if rarities is not None else None
        return filtered_layer_images, filtered_rarities


class Rule4(RuleBase):
    """4. Якщо Accessory Mouth та Accessory face не none - не використовувати Bounty hunter та Ranger у Uniform."""

    condition_layer: str = "Trait5_Accessory_mouth"
    condition_layer2: str = "Trait6_Accessory_face"
    target_layers: list[str] = ["Trait7_Uniform"]

    @classmethod
    def ignore_rule_condition(cls, final_layers: dict) -> bool:
        return final_layers[cls.condition_layer].name == "None" \
            or final_layers[cls.condition_layer2].name == "None"

    @classmethod
    def filter_images(cls, layer_images: list, rarities: list) -> (list, list):
        filtered_layer_images = []
        filtered_rarities = [] if rarities is not None else None

        for index, image in enumerate(layer_images):
            if image != "None" and image.name in [
                "Bounty-hunter.png",
                "Ranger.png"
            ]:
                continue

            # keep values
            filtered_layer_images.append(image)
            if rarities is not None:
                filtered_rarities.append(rarities[index])

        return filtered_layer_images, filtered_rarities


class Rule5(RuleBase):
    """5. Якщо Uniform = none - використовувати Casual top, Casual pants та Hat всі слої крім none."""

    condition_layer: str = "Trait7_Uniform"
    target_layers: list[str] = ["Trait8_Casual_pants", "Trait9_Casual_top", "Trait11_Hat"]

    @classmethod
    def ignore_rule_condition(cls, final_layers: dict) -> bool:
        return final_layers[cls.condition_layer].name != "None"

    @classmethod
    def filter_images(cls, layer_images: list, rarities: list) -> (list, list):
        filtered_layer_images = []
        filtered_rarities = [] if rarities is not None else None

        for index, image in enumerate(layer_images):
            # ignore values
            if image == "None":
                continue

            # keep values
            filtered_layer_images.append(image)
            if rarities is not None:
                filtered_rarities.append(rarities[index])

        return filtered_layer_images, filtered_rarities
