from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    ingredient = Ingredient("ovo")
    ingredient_2 = Ingredient("bacon")
    dish_Jhuly = Dish("jhuly", 39.99)
    dish_2 = Dish("macarronada", 10.99)
    dish_Jhuly_3 = Dish("jhuly", 39.99)

    assert dish_Jhuly.name == "jhuly"
    assert repr(dish_Jhuly) == "Dish('jhuly', R$39.99)"

    assert dish_Jhuly.__eq__(dish_Jhuly_3) is True
    assert dish_Jhuly.__eq__(dish_2) is False

    assert hash(dish_Jhuly) == hash(dish_Jhuly_3)
    assert hash(dish_Jhuly) != hash(dish_2)

    with pytest.raises(TypeError):
        Dish("Jhuly", "imensuravel")

    with pytest.raises(ValueError):
        Dish("Jhuly", 0)

    dish_Jhuly.add_ingredient_dependency(ingredient, 2)
    dish_Jhuly_3.add_ingredient_dependency(ingredient_2, 1)

    assert dish_Jhuly.get_ingredients() == {
        Ingredient("ovo")
    }

    assert dish_Jhuly_3.get_ingredients() == {
        Ingredient("bacon")
    }

    assert dish_Jhuly.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
    }

    assert dish_Jhuly_3.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
