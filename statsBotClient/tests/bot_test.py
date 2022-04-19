"""
Модуль тестов по всем гет-запросам к серверу.
"""
import unittest
import requests
from tests.correct_responses import CorrectResponses


class BotTest(unittest.TestCase):
    """
    Класс тестов гет-запросов к серверу.
    """
    def test_get_stats_with_info_point_1(self):
        """
        Тест гет-запроса с параметром 1.
        """
        response = requests.get('http://localhost:5000/acquisition/1/')
        print("\n")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 266)
        if response.json() == 266:
            print("Get request to http://localhost:5000/acquisition/1/ is OK.")
        else:
            print("Get request to http://localhost:5000/acquisition/1/ is Fail.")

    def test_get_stats_with_info_point_2(self):
        """
        Тест гет-запроса с параметром 2.
        """
        response = requests.get('http://localhost:5000/acquisition/2/')
        print("\n")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 4927)
        if response.json() == 4927:
            print("Get request to http://localhost:5000/acquisition/2/ is OK.")
        else:
            print("Get request to http://localhost:5000/acquisition/2/ is Fail.")

    def test_get_stats_with_info_point_3(self):
        """
        Тест гет-запроса с параметром 3.
        """
        response = requests.get('http://localhost:5000/acquisition/3/')
        print("\n")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), CorrectResponses.stats_data_for_info_type_3)
        if response.json() == CorrectResponses.stats_data_for_info_type_3:
            print("Get request to http://localhost:5000/acquisition/3/ is OK.")
        else:
            print("Get request to http://localhost:5000/acquisition/3/ is Fail.")

    def test_get_stats_with_info_point_4(self):
        """
        Тест гет-запроса с параметром 4.
        """
        response = requests.get('http://localhost:5000/acquisition/4/')
        print("\n")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), CorrectResponses.stats_data_for_info_type_4)
        if response.json() == CorrectResponses.stats_data_for_info_type_4:
            print("Get request to http://localhost:5000/acquisition/4/ is OK.")
        else:
            print("Get request to http://localhost:5000/acquisition/4/ is Fail.")

    def test_get_stat_with_info_point_1(self):
        """
        Тест гет-запроса статистики пользователя по имени и параметру 1.
        """
        response = requests.get('http://localhost:5000/acquisition/mjc01/1/')
        print("\n")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 2)
        if response.json() == 2:
            print("Get request to http://localhost:5000/acquisition/mjc01/1/ is OK.")
        else:
            print("Get request to http://localhost:5000/acquisition/mjc01/1/ is Fail.")

    def test_get_stat_with_info_point_2(self):
        """
        Тест гет-запроса статистики пользователя по имени и параметру 2.
        """
        response = requests.get('http://localhost:5000/acquisition/mjc01/2/')
        print("\n")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 237)
        if response.json() == 237:
            print("Get request to http://localhost:5000/acquisition/mjc01/2/ is OK.")
        else:
            print("Get request to http://localhost:5000/acquisition/mjc01/2/ is Fail.")

    def test_get_users_list(self):
        """
        Тест гет-запроса списка пользователей.
        :return:
        """
        response = requests.get('http://localhost:5000/acquisition')
        print("\n")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), CorrectResponses.users_list)
        if response.json() == CorrectResponses.users_list:
            print("Get request to http://localhost:5000/acquisition is OK.")
        else:
            print("Get request to http://localhost:5000/acquisition is Fail.")

if __name__ == '__main__':
    unittest.main()
