from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user_task";
        ALTER TABLE "task" DROP COLUMN "deadlines";
        ALTER TABLE "user" DROP COLUMN "created_at";
        ALTER TABLE "user" DROP COLUMN "edited_at";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "task" ADD "deadlines" DATE NOT NULL;
        ALTER TABLE "user" ADD "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "user" ADD "edited_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        CREATE TABLE "user_task" (
    "task_id" INT NOT NULL REFERENCES "task" ("task_id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("user_id") ON DELETE CASCADE
);"""
