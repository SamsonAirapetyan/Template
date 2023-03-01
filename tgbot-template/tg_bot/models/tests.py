from SQLLite import Database

db = Database()


def test():
    db.create_table_users()
    users = db.select_all_users()
    print(f"fДо добавления _______________{users}")
    db.add_user(5, "Samson", "email")
    db.add_user(6, "Grant", "samsonchikl.email")
    db.add_user(7, " Diana", "Dianchil.com")
    db.add_user(8, 2, 3)
    users = db.select_all_users()

    print(f"После добавления______________{users}")


test()
