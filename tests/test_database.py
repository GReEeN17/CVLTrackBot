import unittest

from database import database
from data import lg_test_2, cg_test_2


class TestDB(unittest.TestCase):
    def test_league_games(self):
        database.insert_lg(lg_test_2)
        self.assertEqual(database.select_lg(0),
                         (0, '9 легион', 'SkyStepS', '11.02.2023 21:00 (Сб)', 'Гражданский проспект 7', ''))
        self.assertEqual(database.select_lg(1),
                         (1, 'SkyStepS', 'ПРОСВЕТ', '18.02.2023 11:30 (Сб)', 'Комендантский просп. 29к2', ''))
        self.assertEqual(database.select_lg(2),
                         (2, 'SkyStepS', 'VOLBOL - M', '25.02.2023 11:30 (Сб)', 'Комендантский просп. 29к2', ''))
        self.assertEqual(database.select_lg(3),
                         (3, 'Вертикаль', 'SkyStepS', '04.03.2023 16:00 (Сб)',
                          'пос. Металлострой, ул. Полевая, д. 10 лит. А, с/з №2', ''))
        self.assertEqual(database.select_lg(4),
                         (4, 'Оккервиль', 'SkyStepS', '10.03.2023 19:00 (Пт)',
                          'Санкт-Петербург проспект Солидарности д.11 корп.2', ''))
        self.assertEqual(database.select_lg(5),
                         (5, 'Морские волки', 'SkyStepS', '15.03.2023 19:40 (Ср)', 'Двинская ул., 5/7', ''))
        self.assertEqual(database.select_lg(6),
                         (6, 'SkyStepS', 'Oris (Uglovo Team)', '25.03.2023 11:30 (Сб)', 'Комендантский просп. 29к2',''))
        self.assertEqual(database.select_lg(7),
                         (7, 'SkyStepS', 'LEGENDA', '01.04.2023 11:30 (Сб)', 'Комендантский просп. 29к2', ''))
        self.assertEqual(database.select_lg(8),
                         (8, 'Охта', 'SkyStepS', '08.04.2023 18:50 (Сб)', 'пр. Энергетиков 50', ''))
        database.clear_lg()

    def test_cup_games(self):
        database.insert_cg(cg_test_2)
        self.assertEqual(database.select_cg(0),
                         (0, '1 (до 20.11.2022)', 'SkyStepS', 'Нет Идей', '22.10.2022 11:30 (Сб)', 'Комендантский 29/2',
                          '3:0'))
        self.assertEqual(database.select_cg(1),
                         (1, '2 (до 31.12.2022)', 'SkyStepS', 'Океанприбор', '27.12.2022 18:35 (Вт)',
                          'Комендантский просп., 29, корп. 2', '3:2'))
        self.assertEqual(database.select_cg(2),
                         (2, '3 (до 29.01.2023)', 'ПМЦ Калининский', 'SkyStepS', '20.01.2023 19:50 (Пт)',
                          'Демьяна Бедного 9', '3:2'))
        database.clear_cg()
