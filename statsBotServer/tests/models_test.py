"""
Модуль тестов по методам модуля models.py.
"""
import unittest
from src.models import StatsModel
from tests.correct_responses import CorrectResponses


class ModelsTest(unittest.TestCase):
    """
    Класс тестов для модуля models.py.
    """
    def test_get_number_of_messages_one_user(self):
        """
        Тест метода get_number_of_messages_one_user() класса StatsModel.
        """
        models_object = StatsModel()
        print("\n")
        self.assertEqual(models_object.get_number_of_messages_one_user("mjc01"), 2)
        if models_object.get_number_of_messages_one_user("mjc01") == 2:
            print("Test StatsModel.get_number_of_messages_one_user(\"mjc01\") is OK.")
        else:
            print("Test StatsModel.get_number_of_messages_one_user(\"mjc01\") is Fail.")

    def test_get_number_of_character_one_user(self):
        """
        Тест метода get_number_of_character_one_user() класса StatsModel.
        """
        models_object = StatsModel()
        print("\n")
        self.assertEqual(models_object.get_number_of_character_one_user("mjc01"), 237)
        if models_object.get_number_of_character_one_user("mjc01") == 237:
            print("Test StatsModel.get_number_of_character_one_user(\"mjc01\") is OK.")
        else:
            print("Test StatsModel.get_number_of_character_one_user(\"mjc01\") is Fail.")

    def test_get_number_of_users(self):
        """
        Тест метода get_number_of_users() класса StatsModel.
        """
        models_object = StatsModel()
        print("\n")
        self.assertEqual(models_object.get_number_of_users(), 266)
        if models_object.get_number_of_users() == 266:
            print("Test StatsModel.get_number_of_users() is OK.")
        else:
            print("Test StatsModel.get_number_of_users() is Fail.")

    def test_get_number_of_messages_all_users(self):
        """
        Тест метода get_number_of_messages_all_users() класса StatsModel.
        """
        models_object = StatsModel()
        print("\n")
        self.assertEqual(models_object.get_number_of_messages_all_users(), 4927)
        if models_object.get_number_of_messages_all_users() == 4927:
            print("Test StatsModel.get_number_of_messages_all_users() is OK.")
        else:
            print("Test StatsModel.get_number_of_messages_all_users() is Fail.")

    def test_get_number_messages_of_each_user(self):
        """
        Тест метода get_number_messages_of_each_user() класса StatsModel.
        :return:
        """
        models_object = StatsModel()
        print("\n")
        self.assertEqual(dict(models_object.get_number_messages_of_each_user()),
                         CorrectResponses.stats_data_for_info_type_3)
        if dict(models_object.get_number_messages_of_each_user()) == \
                CorrectResponses.stats_data_for_info_type_3:
            print("Test StatsModel.get_number_messages_of_each_user() is OK.")
        else:
            print("Test StatsModel.get_number_messages_of_each_user() is Fail.")

    def test_get_character_count_of_each_user(self):
        """
        Тест метода get_character_count_of_each_user() класса StatsModel.
        """
        models_object = StatsModel()
        print("\n")
        self.assertEqual(dict(models_object.get_character_count_of_each_user()),
                         CorrectResponses.stats_data_for_info_type_4)
        if dict(models_object.get_character_count_of_each_user()) == \
                CorrectResponses.stats_data_for_info_type_4:
            print("Test StatsModel.get_character_count_of_each_user() is OK.")
        else:
            print("Test StatsModel.get_character_count_of_each_user() is Fail.")

    def test_get_users_list(self):
        """
        Тест метода get_user_list() класса StatsModel.
        :return:
        """
        models_object = StatsModel()
        print("\n")
        self.assertEqual(models_object.get_users_list(), CorrectResponses.users_list)
        if models_object.get_users_list() == CorrectResponses.users_list:
            print("Test StatsModel.get_users_list() is OK.")
        else:
            print("Test StatsModel.get_users_list() is Fail.")

if __name__ == '__main__':
    unittest.main()
