"""
Модуль для реализации клиентской части бота по сбору статистики из БД.
"""
import json
from telethon.sync import events
import requests
from constants import BotConstants


if __name__ == '__main__':
    users_event_flag = {}

    @BotConstants.BOT.on(events.NewMessage(pattern="/start"))
    async def start_handler(event):
        """
        Обработчик события "/start". В чат выводится инструкция по общению с ботом.
        :param event: событие
        """
        await adding_flag_for_user(event, 0)
        start_message = "Данный бот предоставляет доступ к статистике по собранной базе с форума" \
                        " dccomics.ru.\nДоступные функции: \n/numberofusers - количество пользов" \
                        "ателей,\n/numberofmessagesusers - общее количество сообщений,\n/numberm" \
                        "essagesofeachuser - количество сообщений каждого пользователя,\n/charac" \
                        "tercountofeachuser - количество символов по всем сообщениями пользовате" \
                        "ля,\n/userslist - список пользователей."
        await BotConstants.BOT.send_message(event.chat_id, start_message)

    @BotConstants.BOT.on(events.NewMessage(pattern="/numberofusers"))
    async def number_of_users_handler(event):
        """
        Обработчик события "/numberofusers". В чат выводится количество пользователей.
        :param event: событие
        """
        chat = await event.get_chat()
        response = requests.get(f'{BotConstants.URL}{BotConstants.INFO_POINT}1/')
        response_in_json = json.loads(response.text)
        await BotConstants.BOT.send_message(chat.id, "Количество пользователей на форуме:\n" +
                                            str(response_in_json))

    @BotConstants.BOT.on(events.NewMessage(pattern="/numberofmessagesusers"))
    async def number_of_messages_users_handler(event):
        """
        Обработчик события "/numberofmessagesusers". В чат выводится общее количество сообщений.
        :param event: событие
        """
        chat = await event.get_chat()
        response = requests.get(f'{BotConstants.URL}{BotConstants.INFO_POINT}2/')
        response_in_json = json.loads(response.text)
        await BotConstants.BOT.send_message(chat.id, "Общее количество сообщений:\n" +
                                            str(response_in_json))

    @BotConstants.BOT.on(events.NewMessage(pattern="/numbermessagesofeachuser"))
    async def number_messages_of_each_user_handler(event):
        """
        Обработчик события "/numbermessagesofeachuser". В чат выводится количество сообщений
        каждого пользователя.
        :param event: событие
        """
        chat = await event.get_chat()
        response = requests.get(f'{BotConstants.URL}{BotConstants.INFO_POINT}3/')
        response_in_json = json.loads(response.text)

        await BotConstants.BOT.send_message(chat.id, "Количество сообщений каждого пользователя:\n")
        message_to_user = ""
        for field, text_field in response_in_json.items():
            message_to_user += f"{field}: {text_field}\n"

        await BotConstants.BOT.send_message(chat.id, message_to_user)

    @BotConstants.BOT.on(events.NewMessage(pattern="/charactercountofeachuser"))
    async def character_count_of_each_user_handler(event):
        """
        Обработчик события "/charactercountofeachuser". В чат выводится количество символов
        каждого пользователя.
        :param event: событие
        """
        chat = await event.get_chat()
        response = requests.get(f'{BotConstants.URL}{BotConstants.INFO_POINT}4/')
        response_in_json = json.loads(response.text)

        await BotConstants.BOT.send_message(chat.id, "Количество символов по всем сообщениям"
                                                     " пользователя:\n")
        message_to_user = ""
        for field, text_field in response_in_json.items():
            message_to_user += f"{field}: {text_field}\n"

        await BotConstants.BOT.send_message(chat.id, message_to_user)

    @BotConstants.BOT.on(events.NewMessage)
    async def user_stats_handler(event):
        """
        Обработчик события ввода имени пользователя для получения его статистики.
        :param event: событие
        """
        sender = await event.get_sender()
        user_message_text = event.message.text

        if sender.id not in users_event_flag:
            await adding_flag_for_user(event, 0)

        if users_event_flag[sender.id] == 1 and user_message_text != "/userslist":
            chat = await event.get_chat()

            all_users = requests.get(f'{BotConstants.URL}/acquisition')
            if user_message_text in json.loads(all_users.text):
                response = requests.get(f'{BotConstants.URL}{BotConstants.INFO_POINT}'
                                        f'{user_message_text}/1/')
                await BotConstants.BOT.send_message(chat.id, "Количество сообщений:\n" +
                                                    str(json.loads(response.text)))
                response = requests.get(f'{BotConstants.URL}{BotConstants.INFO_POINT}'
                                        f'{user_message_text}/2/')
                await BotConstants.BOT.send_message(chat.id, "Количество символов по всем"
                                                             " сообщениям:\n" +
                                                    str(json.loads(response.text)))
            else:
                await BotConstants.BOT.send_message(chat.id, "Введённого пользователя нет в базе.")

            await BotConstants.BOT.send_message(chat.id, "Для повторного получения статистики поль"
                                                         "зователя по имени введите команду /users"
                                                         "list.")
            await adding_flag_for_user(event, 0)

    @BotConstants.BOT.on(events.NewMessage(pattern="/userslist"))
    async def users_list_handler(event):
        """
        Обработчик события "/userslist". В чат выводится список пользователей.
        :param event: событие
        """
        await adding_flag_for_user(event, 0)
        chat = await event.get_chat()
        response = requests.get(f'{BotConstants.URL}/acquisition')
        response_in_json = json.loads(response.text)

        await BotConstants.BOT.send_message(chat.id, "Список пользователей форума:\n")
        message_to_user = ""
        for row in response_in_json:
            message_to_user += f"{row}\n"

        await BotConstants.BOT.send_message(chat.id, message_to_user)
        await adding_flag_for_user(event, 1)
        await BotConstants.BOT.send_message(chat.id, "Введите имя пользователя для вывода"
                                                     " его статистики.")

    async def adding_flag_for_user(event, flag):
        """
        Метод для установки флага для пользователя по его id.
        :param event: событие
        :param flag: значение флага
        """
        sender = await event.get_sender()
        users_event_flag[sender.id] = flag


    BotConstants.BOT.run_until_disconnected()
