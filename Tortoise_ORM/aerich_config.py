TORTOISE_ORM = {
  "connections": {"default": "sqlite://product.db"},
  "apps": {
    "models": {
      "models": ["tortoise_test",
                 "task.models",
                 "user.models",
                 "aerich.models"],
      "default_connection": "default",
    },
  },
}