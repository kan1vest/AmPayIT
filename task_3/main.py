
import asyncio
import os
import sys


sys.path.insert(1, os.path.join(sys.path[0], '..'))

from orm import AsyncORM


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_orders()
    await AsyncORM.select_order_amount_for_client()
  
   



if __name__ == "__main__":
    asyncio.run(main())
