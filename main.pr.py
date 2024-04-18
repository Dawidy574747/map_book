users: list[dict] = [
    {"name": "Dawid", "sourname": "Baluka", "posts": 6000},
    {"name": "Kevin", "sourname": "Czajkowski", "posts": 6002},
    {"name": "Kamil", "sourname": "Gil", "posts": 1000000},
    {"name": "Daniel", "sourname": "Blaszczyk", "posts": 6}

]


def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twoj znajomy {user['name']} opublikowal: {user['posts']}")

show_users(users)