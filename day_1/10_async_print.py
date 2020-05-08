"""
Пример программы для работы с асинхронностью
"""
import asyncio

async def print_counter(x):
    for number in range(x):
        print(number)
        await asyncio.sleep(.5)

async def start(x):
    coroutines = []
    for number in range(x):
        coroutines.append(
            asyncio.create_task(print_counter(x))
        )
    await asyncio.wait(coroutines)

user_count = int(input("Количество фуункций >> "))
asyncio.run(start(user_count))