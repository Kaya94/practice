import asyncio
from time import time

async def do_smth(sec) -> None:
    await asyncio.sleep(sec)
    print("result", sec)


async def print2() -> None:
    await asyncio.sleep(10)
    print(2)


async def print1(sec) -> None:
    await asyncio.sleep(sec)
    print(sec)
    await do_smth(sec)


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 16):
            tg.create_task(print1(i))


start = time()
asyncio.run(main())
print(f"Время на работу: {time() - start}")

