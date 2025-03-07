
import asyncio
import os
import sys


sys.path.insert(1, os.path.join(sys.path[0], '..'))

from orm import AsyncORM


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_employs()
    print(*(await AsyncORM.select_emploes_salary()))
    print(await AsyncORM.update_emploes_salary())
    print(await AsyncORM.delete_employ())
   



if __name__ == "__main__":
    asyncio.run(main())
