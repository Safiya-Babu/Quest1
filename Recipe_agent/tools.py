def categorize_ingredients(ingredients: str) -> str:

    ingredients = ingredients.lower()

    proteins = []
    vegetables = []
    carbs = []

    if "egg" in ingredients:
        proteins.append("egg")

    if "chicken" in ingredients:
        proteins.append("chicken")

    if "onion" in ingredients:
        vegetables.append("onion")

    if "tomato" in ingredients:
        vegetables.append("tomato")

    if "rice" in ingredients:
        carbs.append("rice")

    if "bread" in ingredients:
        carbs.append("bread")

    result = "Ingredient Categories:\n"
    result += f"Proteins: {', '.join(proteins) if proteins else 'None'}\n"
    result += f"Vegetables: {', '.join(vegetables) if vegetables else 'None'}\n"
    result += f"Carbohydrates: {', '.join(carbs) if carbs else 'None'}"

    return result


def estimate_budget(ingredients: str) -> str:

    ingredients = ingredients.lower()

    cost = 0

    if "egg" in ingredients:
        cost += 8

    if "onion" in ingredients:
        cost += 5

    if "tomato" in ingredients:
        cost += 5

    if "rice" in ingredients:
        cost += 20

    if "bread" in ingredients:
        cost += 25

    return f"Estimated ingredient cost: ₹{cost}"