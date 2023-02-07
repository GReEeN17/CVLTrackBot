import unittest
from functions.functions_league_check import compare_db_w_tt
from database import database
from data import lg_test_1, lg_test_2, lg_test_3, lg_test_5, lg_test_6


def make_res_n_responses(lg_1, lg_2):
    database.insert_lg(lg_1)
    res = compare_db_w_tt(lg_2)
    count = 0
    responses = []
    response = database.select_lg(count)
    while response:
        count += 1
        responses.append(response)
        response = database.select_lg(count)
    database.clear_lg()
    return [res, responses]


class TestCDT(unittest.TestCase):
    '''def test_cdt_1(self):
        res, responses = make_res_n_responses(lg_test_1, lg_test_1)
        self.assertEqual(res, [responses, []])

    def test_cdt_2(self):
        res, responses = make_res_n_responses(lg_test_1, lg_test_3)
        self.assertEqual(res, [responses, [[7, 0, 'diff_time', 'diff_place'],
                                           [9, 9, 'diff_time', 'diff_place']]])

    def test_cdt_3(self):
        res, responses = make_res_n_responses(lg_test_3, lg_test_1)
        self.assertEqual(res, [responses, [[0, 7, 'postponed'], [9, 9, 'postponed']]])

    def test_cdt_4(self):
        res, responses = make_res_n_responses(lg_test_1, lg_test_6)
        self.assertEqual(res, [responses, [[7, 0, 'diff_time', 'diff_place'],
                                           [9, 9, 'diff_time', 'diff_place'],
                                           [10, 10, 'played']]])

    def test_cdt_5(self):
        res, responses = make_res_n_responses(lg_test_6, lg_test_1)
        self.assertEqual(res, [responses, [[0, 7, 'postponed'], [9, 9, 'postponed'],
                                           [10, 10, 'postponed']]])

    def test_cdt_6(self):
        res, responses = make_res_n_responses(lg_test_3, lg_test_6)
        self.assertEqual(res, [responses, [[10, 10, 'played']]])

    def test_cdt_7(self):
        res, responses = make_res_n_responses(lg_test_6, lg_test_3)
        self.assertEqual(res, [responses, [[10, 10, 'postponed']]])

    def test_cdt_8(self):
        res, responses = make_res_n_responses(lg_test_2, lg_test_5)
        self.assertEqual(res, [responses, [[0, 0, 'played'],
                                           [1, 1, 'played'],
                                           [2, 2, 'played'],
                                           [3, 3, 'played'],
                                           [4, 4, 'played'],
                                           [5, 5, 'played'],
                                           [6, 6, 'played'],
                                           [7, 7, 'played'],
                                           [8, 8, 'played']]])

    def test_cdt_9(self):
        res, responses = make_res_n_responses(lg_test_5, lg_test_2)
        self.assertEqual(res, [responses, []])'''
