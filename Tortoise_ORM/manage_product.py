from tortoise import Tortoise, run_async
from tortoise_test import Product
from user.models import User
from task.models import Task

async def connect_db():
    await Tortoise.init(
        db_url="sqlite://product.db",
        modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

async def create_product():
    await connect_db()
    await Product.create(
        product_name="Марафон похудения",
        product_type="online",
        product_description="text",
    )

async def query_product():
    await connect_db()
    await Product.get(id=1)
    print("All products")
    print(await Product.all().values('id', 'product_name'))


async def update_product():
    await connect_db()
    update1 = await Product.get(id=1)
    await update1.save()

async def delete_product():
    await connect_db()
    await Product.get(id=5).delete()

async def create_user():
    await connect_db()
    await User.create(
        id=1,
        username="Paspekov123",
        firstname="Paspekov",
        lastname="Nikolay",
        age="34"
    )

async def create_task():
    await connect_db()
    await Task.create(
        task_id=1,
        name="Сопровождение",
        description= "text"
    )

if __name__ == "__main__":
    #run_async(create_product())
    #run_async(query_product())
    #run_async(update_product())
    run_async(delete_product())
    #run_async(create_user())
    #run_async(create_task())