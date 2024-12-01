from backend.db import SessionLocal

async def get_db():
    """
        Генератор, который предоставляет сессию базы данных SQLAlchemy.
        Создает сессию базы данных, используя `SessionLocal`, и автоматически закрывает её
        в блоке `finally`, даже если возникают исключения.  Это гарантирует, что ресурсы базы данных
        будут освобождены после использования.
        Yields:
            Session: Сессия SQLAlchemy для работы с базой данных.
        """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()