def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twoj znajomy {user['name']} opublikowal: {user['posts']}")


def add_new_user(users: list) -> None:
    new_name: str = input("Enter your name: ")
    new_name: str = input("Enter your surname")
    new_posts: int = int(input("Enter your posts: "))
    new_users: dict = {"name": new_name, "surname": new_surname, "posts": new_posts}
    print(new_user)
    users.append(new_user)


def search_user(users: list) -> None:
    kogo_szukasz = input("Kogo szukasz: ")
    for user in user:
        if user['name'] == kogo_szukasz:
            print(user)
