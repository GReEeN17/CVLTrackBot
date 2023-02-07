from test_compare import TestCMP
from test_database import TestDB
from test_cmp_db_tt import TestCDT
import unittest
import xmlrunner


test_classes = [TestCMP, TestDB, TestCDT]
suites_list = []
for test_class in test_classes:
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    suites_list.append(suite)

if __name__ == '__main__':
    testRunner = xmlrunner.XMLTestRunner(output='test-reports').run(unittest.TestSuite(suites_list))
