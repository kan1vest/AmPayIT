
import asyncio
import os
import sys


sys.path.insert(1, os.path.join(sys.path[0], '..'))

from orm import AsyncORM


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_products()
    await AsyncORM.select_products_quantity()
    print(await AsyncORM.update_product_price())
   



if __name__ == "__main__":
    asyncio.run(main())
