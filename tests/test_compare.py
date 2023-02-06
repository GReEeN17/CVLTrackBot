from datetime import datetime
import unittest
from data import lg_test_1, lg_test_2, lg_test_3, lg_test_4, lg_test_5
from data import cg_test_1, cg_test_2, cg_test_3, cg_test_4, cg_test_5
from functions.functions_match_handler import set_next_game


class TestCMP(unittest.TestCase):
    def test_1_1(self):
        time = datetime(2022, 12, 28, 18, 50)
        set_game = set_next_game(lg_test_1, cg_test_1, time)
        set_right = [True, False, [['SkyStepS', 'ВК_БЮРО', 'перенесена на неопределенную дату'],
                      ['SkyStepS', 'ВК Остров', 'перенесена на неопределенную дату'],
                      ['SkyStepS', 'Prima', 'перенесена на неопределенную дату'],
                      ['АБСОЛЮТ-1', 'SkyStepS', 'перенесена на неопределенную дату']], [], None, None, None, None]
        self.assertEqual(set_game, set_right)

    def test_1_2(self):
        time = datetime(2024, 4, 1, 4, 10)
        set_game = set_next_game(lg_test_1, cg_test_1, time)
        set_right = [True, False, [['SkyStepS', 'ВК_БЮРО', 'перенесена на неопределенную дату'],
                                   ['SkyStepS', 'ВК Остров', 'перенесена на неопределенную дату'],
                                   ['SkyStepS', 'Prima', 'перенесена на неопределенную дату'],
                                   ['АБСОЛЮТ-1', 'SkyStepS', 'перенесена на неопределенную дату']], [], None, None,
                     None, None]
        self.assertEqual(set_game, set_right)

    def test_2_1(self):
        time = datetime(2023, 3, 9, 18, 40)
        set_game = set_next_game(lg_test_2, cg_test_2, time)
        right_next_l_m = datetime(2023, 3, 10, 19, 0)
        set_right = [False, False, [], [], right_next_l_m, None, 4, None]
        self.assertEqual(set_game, set_right)

    def test_2_2(self):
        time = datetime(2023, 4, 1, 11, 31)
        set_game = set_next_game(lg_test_2, cg_test_2, time)
        right_next_l_m = datetime(2023, 4, 8, 18, 50)
        set_right = [False, False, [], [], right_next_l_m, None, 8, None]
        self.assertEqual(set_game, set_right)

    def test_3_1(self):
        time = datetime(2023, 1, 10, 18, 10)
        set_game = set_next_game(lg_test_3, cg_test_3, time)
        right_next_l_m = datetime(2023, 1, 12, 17, 40)
        set_right = [True, False, [['SkyStepS', 'ВК Остров', 'перенесена на неопределенную дату'],
                                   ['АБСОЛЮТ-1', 'SkyStepS', 'перенесена на неопределенную дату']],
                     [], right_next_l_m, None, 7, None]
        self.assertEqual(set_game, set_right)

    def test_3_2(self):
        time = datetime(2023, 1, 12, 17, 41)
        set_game = set_next_game(lg_test_3, cg_test_3, time)
        right_next_l_m = datetime(2023, 1, 15, 18, 30)
        set_right = [True, False, [['SkyStepS', 'ВК Остров', 'перенесена на неопределенную дату'],
                                   ['АБСОЛЮТ-1', 'SkyStepS', 'перенесена на неопределенную дату']],
                     [], right_next_l_m, None, 9, None]
        self.assertEqual(set_game, set_right)

    def test_3_3(self):
        time = datetime(2023, 1, 17, 18, 20)
        set_game = set_next_game(lg_test_3, cg_test_3, time)
        set_right = [True, False, [['SkyStepS', 'ВК Остров', 'перенесена на неопределенную дату'],
                                   ['АБСОЛЮТ-1', 'SkyStepS', 'перенесена на неопределенную дату']],
                     [], None, None, None, None]
        self.assertEqual(set_game, set_right)

    def test_4_1(self):
        time = datetime(2023, 1, 6, 16, 17)
        set_game = set_next_game(lg_test_4, cg_test_4, time)
        right_next_l_m = datetime(2023, 1, 12, 17, 40)
        right_next_c_m = datetime(2023, 1, 9, 15, 0)
        set_right = [True, False, [['SkyStepS', 'ВК Остров', 'перенесена на неопределенную дату'],
                                   ['АБСОЛЮТ-1', 'SkyStepS', 'перенесена на неопределенную дату']],
                     [], right_next_l_m, right_next_c_m, 7, 2]
        self.assertEqual(set_game, set_right)

    def test_4_2(self):
        time = datetime(2023, 1, 9, 15, 1)
        set_game = set_next_game(lg_test_4, cg_test_4, time)
        right_next_l_m = datetime(2023, 1, 12, 17, 40)
        set_right = [True, False, [['SkyStepS', 'ВК Остров', 'перенесена на неопределенную дату'],
                                    ['АБСОЛЮТ-1', 'SkyStepS', 'перенесена на неопределенную дату']],
                      [], right_next_l_m, None, 7, None]
        self.assertEqual(set_game, set_right)

    def test_5_1(self):
        time = datetime(2023, 7, 9, 12, 29)
        set_game = set_next_game(lg_test_5, cg_test_5, time)
        set_right = [False, False, [], [], None, None, None, None]
        self.assertEqual(set_game, set_right)
