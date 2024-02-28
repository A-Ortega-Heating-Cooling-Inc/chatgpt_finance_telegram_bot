import asyncio
from prisma import Prisma

async def main() -> None:
    db = Prisma()
    await db.connect()

    clients = await db.customer.find_many()

    for client in clients:
        print(client)

    # write your queries here

    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())