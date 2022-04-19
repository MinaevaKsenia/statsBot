"""
Модуль тестов по методам модуля stats_acquisition.py.
"""
import unittest
from flask import jsonify
from src.views.stats_acquisition import (
    StatsAcquisitionView,
    StatAcquisitionView,
    UsersListAcquisitionView
)
from src.main import create_app
from .correct_responses import CorrectResponses


class AcquisitionTest(unittest.TestCase):
    """
    Класс тестов для модуля stats_acquisition.py.
    """
    def test_get_of_stats_acquisition(self):
        """
        Тест метода get() класса StatsAcquisitionView с передачей значений параметра info_type
        в промежутке от 1 до 4.
        """
        with create_app().app_context():
            stats_acquisition_object = StatsAcquisitionView()
            response = jsonify(266), 200
            result = stats_acquisition_object.get(1)
            print("\n")
            self.assertEqual(response[0].get_json(), result[0].get_json())
            self.assertEqual(response[1], result[1])
            if result[0].get_json() == response[0].get_json() and result[1] == response[1]:
                print("Test StatsAcquisitionView.get(1) is OK.")
            else:
                print("Test StatsAcquisitionView.get(1) is Fail.")

            response = jsonify(4927), 200
            result = stats_acquisition_object.get(2)
            self.assertEqual(response[0].get_json(), result[0].get_json())
            self.assertEqual(response[1], result[1])
            if result[0].get_json() == response[0].get_json() and result[1] == response[1]:
                print("Test StatsAcquisitionView.get(2) is OK.")
            else:
                print("Test StatsAcquisitionView.get(2) is Fail.")

            response = jsonify(CorrectResponses.stats_data_for_info_type_3), 200
            result = stats_acquisition_object.get(3)
            self.assertEqual(response[0].get_json(), result[0].get_json())
            self.assertEqual(response[1], result[1])
            if result[0].get_json() == response[0].get_json() and result[1] == response[1]:
                print("Test StatsAcquisitionView.get(3) is OK.")
            else:
                print("Test StatsAcquisitionView.get(3) is Fail.")

            response = jsonify(CorrectResponses.stats_data_for_info_type_4), 200
            result = stats_acquisition_object.get(4)
            self.assertEqual(response[0].get_json(), result[0].get_json())
            self.assertEqual(response[1], result[1])
            if result[0].get_json() == response[0].get_json() and result[1] == response[1]:
                print("Test StatsAcquisitionView.get(4) is OK.")
            else:
                print("Test StatsAcquisitionView.get(4) is Fail.")

    def test_get_of_stat_acquisition(self):
        """
        Тест метода get() класса StatAcquisitionView с передачей значений параметра info_type
        в промежутке от 1 до 2.
        """
        with create_app().app_context():
            stat_acquisition_object = StatAcquisitionView()
            response = jsonify(2), 200
            result = stat_acquisition_object.get("mjc01", 1)
            print("\n")
            self.assertEqual(response[0].get_json(), result[0].get_json())
            self.assertEqual(response[1], result[1])
            if result[0].get_json() == response[0].get_json() and result[1] == response[1]:
                print("Test StatAcquisitionView.get(\"mjc01\", 1) is OK.")
            else:
                print("Test StatAcquisitionView.get(\"mjc01\", 1) is Fail.")

            response = jsonify(237), 200
            result = stat_acquisition_object.get("mjc01", 2)
            self.assertEqual(response[0].get_json(), result[0].get_json())
            self.assertEqual(response[1], result[1])
            if result[0].get_json() == response[0].get_json() and result[1] == response[1]:
                print("Test StatAcquisitionView.get(\"mjc01\", 2) is OK.")
            else:
                print("Test StatAcquisitionView.get(\"mjc01\", 2) is Fail.")

    def test_get_of_users_list_acquisition(self):
        """
        Тест метода get() класса UsersListAcquisitionView.
        """
        with create_app().app_context():
            user_list_acquisition_object = UsersListAcquisitionView()
            response = jsonify(CorrectResponses.users_list), 200
            result = user_list_acquisition_object.get()
            print("\n")
            self.assertEqual(response[0].get_json(), result[0].get_json())
            self.assertEqual(response[1], result[1])
            if result[0].get_json() == response[0].get_json() and result[1] == response[1]:
                print("Test UsersListAcquisitionView.get() is OK.")
            else:
                print("Test UsersListAcquisitionView.get() is Fail.")


if __name__ == '__main__':
    unittest.main()
