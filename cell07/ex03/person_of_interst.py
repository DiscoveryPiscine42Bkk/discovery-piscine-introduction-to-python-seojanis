def famous_births(figures):

    sorted_figures = sorted(figures.values(), key=lambda person: int(person["date_of_birth"]))

    for person in sorted_figures:
        print(f'{person["name"]} is a great scientist born in {person["date_of_birth"]}.')

        scientists = {
            "a": { " name": "j", "date_of_birth": "3333" },
            "b": { " name": "e", "date_of_birth": "6666" },
            "c": { " name": "n", "date_of_birth": "1000" },
            "d": { " name": "n", "date_of_birth": "2007" },
            "e": { " name": "i", "date_of_birth": "1978" },
            "f": { " name": "e", "date_of_birth": "2550" }
        }

        famous_births(scientists)