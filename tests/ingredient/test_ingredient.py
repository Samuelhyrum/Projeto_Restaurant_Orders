from src.models.ingredient import (
    Ingredient, Restriction
) # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("ovo")
    ingredient_2 = Ingredient("linguiça")
    ingredient_3 = Ingredient("ovo")

    assert ingredient.name == "ovo"

    assert hash(ingredient) == hash(ingredient_3)
    assert hash(ingredient) != hash(ingredient_2)

    assert ingredient.__eq__(ingredient_3) is True
    assert ingredient.__eq__(ingredient_2) is False

    assert repr(ingredient) == "Ingredient('ovo')"

    assert ingredient.restrictions == {
        Restriction.ANIMAL_DERIVED,
    }
