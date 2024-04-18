users: list[dict] = [
    {"name": "Dawid", "sourname": "Baluka", "posts": 6000},
    {"name": "Kevin", "sourname": "Czajkowski", "posts": 6002},
    {"name": "Kamil", "sourname": "Gil", "posts": 1000000},
    {"name": "Daniel", "sourname": "Blaszczyk", "posts": 6}

]


def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twoj znajomy {user['name']} opublikowal: {user['posts']}")


if __name__ == "__main__":
    print("Witaj uzytkowniku")
    while True:

        print("Menu:")
        print("1. Wyswietl co u znajomych")
        menu_option: str = input("dokonaj wyboru:")
        if menu_option == "0":
            print("Program konczy prace")
            break
        if menu_option == "1":
            show_users(users)
