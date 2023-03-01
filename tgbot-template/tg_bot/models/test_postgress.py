import asyncio

from postgresql import Database


async def test():
    await db.delete_users()
    # print("Create the table")
    # await db.create_table_users()
    # print("Created")
    #
    # print("\nAdd users\n")
    #
    # await db.add_user(1, "Samson", " email")
    # await db.add_user(2, "Grant", "asmc@")
    # await db.add_user(3, "David", "sdf#")
    # print("Ready")
    #
    # users = await db.select_all_users()
    # print(f"Получил всех пользователей {users}")
    #
    # user = await db.select_users(name="Samson", id=1)
    # print(f"Пользователь {user}")

loop = asyncio.get_event_loop()
db = Database()
db.create()
loop.run_until_complete(test())
