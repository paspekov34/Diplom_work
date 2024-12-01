TORTOISE_ORM = {
  "connections": {"default": "sqlite://product.db"},
  "apps": {
    "models": {
      "models": [
                 "task.models",
                 "user.models",
                 "aerich.models"],
      "default_connection": "default",
    },
  },
}

"""
    Конфигурация Tortoise ORM.
    `connections`:  Определяет подключения к базам данных.  Здесь используется единственное подключение 
                    `default` к базе данных SQLite с именем `product.db`.  Можно добавить другие подключения
                    для работы с разными базами данных (PostgreSQL, MySQL и т.д.).
    `apps`: Определяет приложения Tortoise ORM.  В данном случае у нас одно приложение `models`,
            которое содержит модели из файлов `task.models`, `user.models` и `aerich.models`.
            `default_connection` указывает на подключение, которое будет использоваться по умолчанию 
            для этого приложения.  `aerich.models` необходим для использования Aerich (инструмента миграций).
    """