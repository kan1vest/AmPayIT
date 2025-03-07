
from os import name
from sqlalchemy import delete, select
from database import Base, async_engine, async_session_factory
from models import EmployeesOrm
from schemas import EmployUpdateShaema



class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


    @staticmethod
    async def insert_employs():
        async with async_session_factory() as session:
            employ_1 = EmployeesOrm(name='employ_1', position='position_1', salary=30000)
            employ_2 = EmployeesOrm(name='Иван', position='position_2', salary=49000)
            employ_3 = EmployeesOrm(name='employ_3', position='position_3', salary=53000)
            employ_4 = EmployeesOrm(name='employ_4', position='position_4', salary=750000)
            employ_5 = EmployeesOrm(name='Анна', position='position_5', salary=120000)
            session.add_all([employ_1, employ_2, employ_3, employ_4, employ_5])
            # flush взаимодействует с БД, поэтому пишем await
            await session.flush() 
            await session.commit()

    @staticmethod
    async def select_emploes_salary(filter_salary = 50000):
        async with async_session_factory() as session:
            query = (
                select(EmployeesOrm.name, EmployeesOrm.position, EmployeesOrm.salary).where(EmployeesOrm.salary > filter_salary)
            )
            res = await session.execute(query)
            result = res.all()
            return result
        """ upd_name = 'Иван', upd_salary = 60000 """
    @staticmethod
    async def update_emploes_salary(upd_name = 'Иван', upd_salary = 60000):
        async with async_session_factory() as session:
            query = (
                select(EmployeesOrm.id).where(EmployeesOrm.name == upd_name)
            )
            res = await session.execute(query)
            upd_id = res.first()
            upd = await session.get(EmployeesOrm, upd_id[0])
            employ = {
                'name': upd.name, 
                'position': upd.position, 
                'salary': upd.salary, 
            } 
            upd.salary = upd_salary
            employ_update = {
                'name': upd.name, 
                'position': upd.position, 
                'salary': upd.salary, 
            }     
            await session.flush()
            await session.commit()
            return {
                'Данные': employ,
                "Изменены на данные": employ_update
            }

    @staticmethod
    async def delete_employ(delete_name = 'Анна'):
        async with async_session_factory() as session:
            query = (
                delete(EmployeesOrm).filter(EmployeesOrm.name == delete_name)
            )
            await session.execute(query)
            await session.commit()
            return {
                "msg": f"Удален сотрудник {delete_name}"
            }