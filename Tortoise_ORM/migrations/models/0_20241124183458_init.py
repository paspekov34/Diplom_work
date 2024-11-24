from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "product" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "product_name" VARCHAR(275) NOT NULL,
    "product_type" VARCHAR(275) NOT NULL,
    "product_description" TEXT NOT NULL,
    "product_description_2" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "task" (
    "task_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(250) NOT NULL,
    "description" TEXT,
    "deadlines" DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "user_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "username" VARCHAR(250) NOT NULL,
    "firstname" VARCHAR(250) NOT NULL,
    "lastname" VARCHAR(250) NOT NULL,
    "age" INT NOT NULL,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "edited_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "user_task" (
    "user_id" INT NOT NULL REFERENCES "user" ("user_id") ON DELETE NO ACTION,
    "task_id" INT NOT NULL REFERENCES "task" ("task_id") ON DELETE NO ACTION
);
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_user_task_user_id_dd81f4" ON "user_task" ("user_id", "task_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
