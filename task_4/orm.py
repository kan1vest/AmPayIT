
from sqlalchemy import delete, select
from database import Base, async_engine, async_session_factory
from models import WorkersORM
import csv


class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


    @staticmethod
    async def insert_employs():
        async with async_session_factory() as session:
            with open('task_4/file.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',', fieldnames=['name', 'position', 'salary'])
                for row in reader:
                    employ = WorkersORM(name=row['name'], position=row['position'], salary=int(row['salary']))
                    session.add(employ)
            await session.flush() 
            await session.commit()

    @staticmethod
    async def select_emploes_position(filter = 'разработчик'):
        async with async_session_factory() as session:
            query = (
                select(WorkersORM.name, WorkersORM.position, WorkersORM.salary).where(WorkersORM.position == filter)
            )
            res = await session.execute(query)
            result = res.all()
            return result


    @staticmethod
    async def update_emploes_salary(upd_name = 'Андрей', upd_salary = 60000):
        async with async_session_factory() as session:
            query = (
                select(WorkersORM.id).where(WorkersORM.name == upd_name)
            )
            res = await session.execute(query)
            upd_id = res.first()
            upd = await session.get(WorkersORM, upd_id[0])
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

    """ @staticmethod
    async def delete_employ(delete_name = 'Анна'):
        async with async_session_factory() as session:
            query = (
                delete(EmployeesOrm).filter(EmployeesOrm.name == delete_name)
            )
            await session.execute(query)
            await session.commit()
            return {
                "msg": f"Удален сотрудник {delete_name}"
            } """