import requests


class BaseClient:
    # URL vk api
    BASE_URL = "https://api.vk.com/method/"
    # метод vk api
    method = None
    # GET, POST, ...
    http_method = None

    def __init__(self):
        # Инициализация
        self.success = True

    def get_params(self):
        return None

    def get_json(self):
        # Получение данных POST запроса
        return None

    def _get_data(self, method, http_method):
        # Отправка запроса к VK API
        try:
            response = requests.get(self.BASE_URL + self.method + "." + self.http_method, params=self.get_params())
            print(self.BASE_URL + self.method + "." + self.http_method)

        except Exception:
            raise SystemExit("Нет ответа от VK")

        return self.response_handler(response)

    def response_handler(self, response):
        # Обработка ответа от VK API
        return response

    def is_success(self):
        # Проверка найден ли ID
        return self.success

    def execute(self):
        # Запуск клиента
        try:
            self.success = True
            return self._get_data(
                self.method,
                http_method=self.http_method
            )
        except Exception:
            #print('Ошибка')
            self.success = False
