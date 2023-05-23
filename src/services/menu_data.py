import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.data = pd.read_csv(source_path)
        self.sets_dishes()

    def mapping(self):
        dishes = {}
        for name, price, ingredient, amount in self.data.itertuples(
            index=False
        ):
            if name not in dishes:
                dishes[name] = {
                    "price": price,
                    "ingredients": [],
                    "amount": [],
                }
            dishes[name]["price"] = price
            dishes[name]["ingredients"].append(ingredient)
            dishes[name]["amount"].append(amount)
        return dishes

    def sets_dishes(self):
        mapped_dict = self.mapping()
        for item, value in mapped_dict.items():
            dish = Dish(item, value["price"])
            for i in range(len(value["ingredients"])):
                dish.add_ingredient_dependency(
                    Ingredient(value["ingredients"][i]), value["amount"][i]
                )
            self.dishes.add(dish)
