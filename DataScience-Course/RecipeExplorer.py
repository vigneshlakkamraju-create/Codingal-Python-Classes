pasta = ("Pasta Arrabiata", "Italian", 20,"Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")
print("Recipe 1:", pasta[0])
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[3])


all_recipies = (pasta, biryani)
print("\nFirst Recipe Name:", all_recipies[0][0])
print("Second Recipe Name:", all_recipies[1][2])
print("Pasta details (sliced):", pasta[1:3])

print("\nPasta Recipe Details:")
for detail in pasta:
    print(" -", detail)

pasta_ingredients = {"Pasta", "Tomato Sauce", "Chili Flakes", "Garlic", "Olive Oil"}
biryani_ingredients = {"Chicken", "Basmati Rice", "Garlic", "Tomato Sauce", "Spices"}

print("\nPasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)
print("Total pasta ingredients:", len(pasta_ingredients))

pasta_ingredients.add("Parmesan")
pasta_ingredients.discard("Chili Flakes")
print("\nUpdated Pasta Ingredients:", pasta_ingredients)

all_ingredients =pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll Ingredients:", all_ingredients)
print("Common Ingredients:", common)
print("Ingredients only in Pasta:", only_pasta)
print("Unique Ingredients to Each Recipe:", unique_to_each)

