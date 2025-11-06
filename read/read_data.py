import csv

def main_menu():
    while True:
        show_choices()
        choice = input("Choisir votre action : ")
        match choice:
            case "1": __show_movies_menu(__read_rows())
            case "2": __getby_title_menu()
            case "3": __get_under_age()
            case "4": __get_by_genre()
            case "5": __get_between_years()
            case "6": exit()

def show_choices():
    print("1. Afficher les films")
    print("2. Récupérer depuis le titre ")
    print("3. Récupérer les films sous une limite d'âge :")
    print("4. Récupérer les films selon un genre")
    print("5. Récupérer les films entre deux années (incluses)")
    print("6. Exit")

def __show_movies_menu(rows: list):
    for row in rows:
        print(row)

def __getby_title_menu():
    title = input("Entrez le nom du film cherché : ")
    __get_by_title(title)

def __get_by_title(title: str):
    __show_movies_menu([row for row in __read_rows() if title in row[1]])

def __get_under_age():
    pass

def __get_by_genre():
    pass

def __get_between_years():
    pass

def __read_rows():
    with open("read/data/movies.csv", "r", newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)

main_menu()