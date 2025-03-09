
from itertools import product
from more_itertools import quantify
from sqlalchemy import delete, select
from database import Base, async_engine, async_session_factory
from models import ProductsOrm



class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


    @staticmethod
    async def insert_products():
        async with async_session_factory() as session:
            product_1 = ProductsOrm(name='prod_1', price=10000, quantity=1)
            product_2 = ProductsOrm(name='prod_2', price=20000, quantity=2)
            product_3 = ProductsOrm(name='prod_3', price=30000, quantity=3)
            product_4 = ProductsOrm(name='prod_4', price=40000, quantity=4)
            product_5 = ProductsOrm(name='prod_5', price=50000, quantity=15)
            product_6 = ProductsOrm(name='prod_6', price=60000, quantity=6)
            product_7 = ProductsOrm(name='prod_7', price=70000, quantity=7)
            product_8 = ProductsOrm(name='prod_8', price=80000, quantity=8)
            product_9 = ProductsOrm(name='prod_9', price=90000, quantity=19)
            product_10 = ProductsOrm(name='prod_10', price=100000, quantity=10)
            session.add_all([product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8, product_9, product_10])
            await session.flush() 
            await session.commit()

    @staticmethod
    async def select_products_quantity(filter_quantity = 10):
        async with async_session_factory() as session:
            query = (
                select(ProductsOrm.name, ProductsOrm.price, ProductsOrm.quantity).where(ProductsOrm.quantity < filter_quantity)
            )
            res = await session.execute(query)
            result = res.all()
            print(result)
            return result
  
    @staticmethod
    async def update_product_price(upd_name = 'prod_1', upd_price = 111111):
        async with async_session_factory() as session:
            query = (
                select(ProductsOrm.id).where(ProductsOrm.name == upd_name)
            )
            res = await session.execute(query)
            upd_id = res.first()
            upd = await session.get(ProductsOrm, upd_id[0])
            employ = {
                'name': upd.name, 
                'price': upd.price, 
                'quantity': upd.quantity, 
            } 
            upd.price = upd_price
            employ_update = {
                'name': upd.name, 
                'price': upd.price, 
                'quantity': upd.quantity, 
            }     
            await session.flush()
            await session.commit()
            return {
                'Данные': employ,
                "Изменены на данные": employ_update
            }
