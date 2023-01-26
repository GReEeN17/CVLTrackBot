import unittest
from unittest import IsolatedAsyncioTestCase

from database import cache, database
from mainTelegram import bot

lg_test = [['SkyStepS', 'ВК_БЮРО', 'перенесена_на_неопределенную_дату'],
           ['SkyStepS', 'ANTIFIRE', '15.10.2022_18:20_(Сб)', 'улица_Маршала_Новикова,_1к3', '3:0'],
           ['SkyStepS', 'Юниоры Приморы', '20.10.2022 18:45 (Чт)', 'Королева 23', '3:0'],
           ['Баррель', 'SkyStepS', '24.10.2022 20:45 (Пн)', 'ул. Вязовая, д. 10 (Академия Платонова)', '1:3'],
           ['SkyStepS', 'RED BARONS', '19.11.2022 18:20 (Сб)', 'улица Маршала Новикова, 1к3', '3:2'],
           ['THWW', 'SkyStepS', '27.11.2022 11:50 (Вс)', 'Ул. Шевченко, д.3, школа#6', '0:3'],
           ['Маяк', 'SkyStepS', '04.12.2022 18:45 (Вс)', 'Пр. Динамо,44Б', '0:3'],
           ['Фаер', 'SkyStepS', '07.12.2022 20:45 (Ср)', 'проспект Сизова, 17', '0:3'],
           ['SkyStepS', 'ВК Остров', 'перенесена на неопределенную дату'],
           ['SkyStepS', 'Prima', 'перенесена на неопределенную дату'],
           ['АБСОЛЮТ-1', 'SkyStepS', 'перенесена на неопределенную дату']]
cg_test = [['3 (до 29.01.2023)', 'SkyStepS'], ['1 (до 20.11.2022)', 'SkyStepS', 'Нет Идей', '22.10.2022 11:30 (Сб)', 'Комендантский 29/2', '3:0'],
           ['2 (до 31.12.2022)', 'SkyStepS', 'Океанприбор', '27.12.2022 18:35 (Вт)', 'Комендантский просп., 29, корп. 2', '3:2']]






class TestDB(IsolatedAsyncioTestCase):
    async def test_crud(self):
        await database.insertLG(lg_test)
        self.assertEqual(await database.selectLG(0), ('SkyStepS', 'ВК_БЮРО', 'перенесена_на_неопределенную_дату', '', '', ''))

if __name__ == '__main__':
    unittest.main()