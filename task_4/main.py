
import asyncio
import os
import sys


sys.path.insert(1, os.path.join(sys.path[0], '..'))

from orm import AsyncORM


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_employs()
    print(await AsyncORM.select_emploes_position())
    print(await AsyncORM.update_emploes_salary())
   



if __name__ == "__main__":
    asyncio.run(main())
