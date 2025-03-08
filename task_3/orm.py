
import datetime
from os import name
from sqlalchemy import and_, delete, func, select, true
from database import Base, async_engine, async_session_factory
from models import OrdersOrm



class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


    @staticmethod
    async def insert_orders():
        async with async_session_factory() as session:
            order_1 = OrdersOrm(customer_id= 1, amount=30000)
            order_2 = OrdersOrm(customer_id= 1, amount=49000)
            order_3 = OrdersOrm(customer_id= 1, amount=53000)
            order_4 = OrdersOrm(customer_id= 2, amount=750000)
            order_5 = OrdersOrm(customer_id= 2, amount=10000)
            order_6 = OrdersOrm(customer_id= 3, amount=120000)
            order_7 = OrdersOrm(customer_id= 3, amount=120000)
            session.add_all([order_1, order_2, order_3, order_4, order_5, order_6, order_7])
            await session.flush() 
            await session.commit()

    @staticmethod
    async def select_order_amount_for_client():
        async with async_session_factory() as session:
            query = select(OrdersOrm.customer_id, func.sum(OrdersOrm.amount)).group_by(OrdersOrm.customer_id)
            res = await session.execute(query)
            result = res.fetchall()
            for record in reversed(result): 
                print("Клиент:", record[0],",Сумма заказа:", record[1])
            print("Максимальная сумма заказа:", max(result, key=lambda x: x[1])[1])


    @staticmethod
    async def select_order_date(year = 2023):
        async with async_session_factory() as session:
            query = select(OrdersOrm.id).where(
                and_(
                    (OrdersOrm.order_date >= datetime.datetime(year, 1, 1)),
                    (OrdersOrm.order_date <= datetime.datetime(year, 12, 31))
                )
            )
            res = await session.execute(query)
            result = res.fetchall()
            if result:
                print(len(result), f"заказов за {year} год")
            else:
                print(f"Заказов за {year} год нет")

    @staticmethod
    async def select_order_amount_average_for_client():
        async with async_session_factory() as session:
            query = select(OrdersOrm.customer_id, func.avg(OrdersOrm.amount)).group_by(OrdersOrm.customer_id)
            res = await session.execute(query)
            result = res.fetchall()
            for record in reversed(result): 
                print("Клиент:", record[0],",Средняя сумма заказа:", record[1])
        

        