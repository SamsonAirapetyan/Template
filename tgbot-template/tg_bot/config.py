from dataclasses import dataclass
from typing import List
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    database_user: str
    database_pas: str


@dataclass
class Miscellaneous:
    wallet: str
    qiwi_token: str
    qiwi_p_pub: str
    qiwi_p_sec: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME'),
            database_user=env.str('PG_USER'),
            database_pas=env.str('PG_PASSWORD')
        ),
        misc=Miscellaneous(
            wallet=env.str('WALLET'),
            qiwi_token=env.str('QIWI'),
            qiwi_p_pub=env.str('QIWI_P_PUB'),
            qiwi_p_sec=env.str('QIWI_P_SEC')
        )
    )
