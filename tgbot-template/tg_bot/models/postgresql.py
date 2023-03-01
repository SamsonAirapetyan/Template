from typing import Union

import asyncpg
from asyncpg.pool import Pool


# from ..config import load_config

# config = load_config('.e
#
# nv')
class Database:
    # def __init__(self, loop: asyncio.AbstractEventLoop):
    #     self.pool: asyncio.pool.Pool = loop.run_until_complete(
    #         asyncpg.create_pool(
    #             user="samson",
    #             password="76Samson263838",
    #             host="127.0.0.1",
    #             database='aiogram'
    #         )
    #     )

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        pool = await asyncpg.create_pool(
            user="samson",
            password="76Samson263838",
            host="127.0.0.1",
            database='aiogram'
        )
        self.pool = pool

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users(
        id int NOT NULL,
        Name varchar(255) NOT NULL,
        email varchar(255),
        PRIMARY KEY (id)
        );
        """

        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND".join([
            f" {item} = ${num}" for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())

    async def select_users(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def add_user(self, id: int, name: str, email: str = None):
        sql = "INSERT INTO Users (id, Name, email) VALUES ($1, $2, $3)"
        await self.pool.execute(sql, id, name, email)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.pool.fetch(sql)

    async def count_users(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM Users")

    async def update_email(self, email, id):
        sql = "UPDATE Users SET email = $1 WHERE =$2"
        await self.pool.execute(sql, email, id)

    async def delete_users(self):
        await self.pool.execute("DELETE FROM Users WHERE True")

# db = Database(loop=asyncio.get_event_loop())
