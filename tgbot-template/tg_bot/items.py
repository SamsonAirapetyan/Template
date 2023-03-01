from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str
    description: str
    price: int
    photo_link: str


description = "Адаптивная прозрачность использует возможности H2 для минимизации интенсивности громких звуков, таких как сирены или электрические инструменты, чтобы вы могли с комфортом слышать окружающий мир."
description_2 = "Разработанный компанией Apple динамический драйвер, оснащенный специальным усилителем, воспроизводит музыку в исключительно детальном качестве звука-так что вы наслаждаетесь каждым тоном, от глубоких, насыщенных басов до четких, чистых максимумов."
Airpods_pro2 = Item(
    id=1, title="Airpods Pro 2", description=description, price=180,
    photo_link="https://avatars.mds.yandex.net/get-mpic/7179065/img_id4030892675689895998.png/orig"
)
Airpods_3 = Item(id=2, title="Airpods 3", description=description_2, price=1,
                 photo_link="https://avatars.mds.yandex.net/get-mpic/5220722/img_id6843138161345205453.jpeg/orig")

items = [Airpods_pro2, Airpods_3]
