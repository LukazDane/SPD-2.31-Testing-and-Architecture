# by Kami Bigdely
# Consolidate conditional expressions
def dice(ingredients):
    print("diced all ingredients.")


def mix_all(diced_ingredients):
    print("mixed all.")


def add_salt():
    print('added salt.')


def pour(liquid):
    print('poured', liquid + '.',)


def make_shirazi_salad(ingredients):
    recipie = ['cucumber', 'tomato', 'onion', 'lemon juice']
    requirements_met = all(ingredient in ingredients for ingredient in recipie)
    if requirements_met:
        dice(ingredients)
        mix_all(ingredients)
        add_salt()
        pour('lemon juice')
        print('Your yummy shirazi salad is ready!')
    else:
        for i, j in zip(recipie, ingredients):
            if i not in ingredients:
                print("needs " + i)


if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
