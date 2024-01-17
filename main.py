import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
import pickle
import subprocess

## Временные переменные
VARTMP_newgame = False
VARTMP_game_works = True

with open('users.sfh', 'rb') as file:
    LIST_users = pickle.load(file)
with open('saves.sfh', 'rb') as file:
    LIST_all_saves = pickle.load(file)


def check_player_add(id):
    global LIST_users
    if id in LIST_users:
        return True
    else:
        LIST_users.append(id)
        with open('users.sfh', 'wb') as file:
            pickle.dump(LIST_users, file)
        with open('users.sfh', 'rb') as file:
            LIST_users = pickle.load(file)
        print('ABCD')
        return False


def get_resources(id):
    global LIST_all_saves
    z = 10000000000000000000000000000
    for i in range(len(LIST_all_saves)):
        k = LIST_all_saves[i]
        if k[0] == id:
            z = i
            LIST_resources = z
        else:
            pass
    if LIST_resources != 10000000000000000000000000000:
        return LIST_resources
    else:
        pass

def print_resources_daily(id):
    global LIST_all_saves
    TMP_LIST_resources = LIST_all_saves[get_resources(id)]
    output = ''
    output += 'Цикл: '
    output += str(TMP_LIST_resources[13])
    output += '\n'
    output += 'РЕСУРСНАЯ СВОДКА:\n'
    output += '-----------------------\n'
    output += 'Сталь, тонн: '
    output += str(TMP_LIST_resources[4])
    output += ' ('
    output += str(TMP_LIST_resources[16])
    output += ')'
    output += '\n'
    output += 'Дерево, тонн: '
    output += str(TMP_LIST_resources[5])
    output += ' ('
    output += str(TMP_LIST_resources[17])
    output += ')'
    output += '\n'
    output += 'Бетон, тонн: '
    output += str(TMP_LIST_resources[6])
    output += ' ('
    output += str(TMP_LIST_resources[18])
    output += ')'
    output += '\n'
    output += 'Цветные металлы, тонн: '
    output += str(TMP_LIST_resources[7])
    output += ' ('
    output += str(TMP_LIST_resources[19])
    output += ')'
    output += '\n'
    output += 'ТНП, на человеко-цикл: '
    output += str(TMP_LIST_resources[8])
    output += ' ('
    output += str(TMP_LIST_resources[20])
    output += ')'
    output += '\n'
    output += 'Продовольствие, человеко-цикл: '
    output += str(TMP_LIST_resources[9])
    output += ' ('
    output += str(TMP_LIST_resources[21])
    output += ')'
    output += '\n'
    output += 'Спирт, литров: '
    output += str(TMP_LIST_resources[10])
    output += ' ('
    output += str(TMP_LIST_resources[22])
    output += ')'
    output += '\n'
    output += 'Лёгкое оружие, единиц: '
    output += str(TMP_LIST_resources[11])
    output += '\n'
    output += 'Тяжёлое оружие, единиц: '
    output += str(TMP_LIST_resources[12])
    output += '\n'
    output += '-----------------------\n'
    output += 'СВОДКА ПО НАСЕЛЕНИЮ:\n'
    output += '-----------------------\n'
    output += 'Рабочие, чел.: '
    output += str(TMP_LIST_resources[1])
    output += '\n'
    output += 'Иждивенцы, чел.: '
    output += str(TMP_LIST_resources[2])
    output += '\n'
    output += 'Ликвидаторы, чел.: '
    output += str(TMP_LIST_resources[3])
    output += '\n'
    output += '-----------------------\n'
    output += "Политическая сводка (строго секретно):\n"
    output += '-----------------------\n'
    output += 'Счастье: '
    output += str(TMP_LIST_resources[14])
    output += '%\n'
    output += 'Благонадёжность: '
    output += str(TMP_LIST_resources[15])
    output += '%\n'
    return output

def wrap_cycle_up(id):
    global LIST_all_saves
    TMP_LIST_resources = LIST_all_saves[get_resources(id)]
    for i in range(4, 11):
        TMP_LIST_resources[i] += TMP_LIST_resources[i + 12]
    TMP_LIST_resources[13] += 1
    LIST_all_saves[get_resources(id)] = TMP_LIST_resources
    with open('saves.sfh', 'wb') as file:
            pickle.dump(LIST_all_saves, file)
    with open('saves.sfh', 'rb') as file:
            LIST_all_saves = pickle.load(file)

    




bot = Bot(token="6351936579:AAF0oXDukVCs0qIf6ZxMakFcjkmrjY2CsiA")
dp = Dispatcher()

@dp.message(F.text)
async def mainFunction(message: Message):
    global LIST_users
    playerid = message.from_user.id
    if message.text == "/start":
        await message.answer('Hi')
        if check_player_add(playerid) is True:
            pass
        else:
            await message.answer("Вы - новый игрок. Если хотите начать играть, напишите сообщение \"НОВАЯ ИГРА\" (без кавычек, заглавными).")
            VARTMP_newgame = True
    elif message.text == "НОВАЯ ИГРА" and VARTMP_newgame is True:
        pass
    elif message.text == "1234567":
        out = 'Добрый день, товарищ начсектора.\n'
        out += print_resources_daily(1111111)
        await message.answer(out)
    elif VARTMP_game_works is True:
        if message.text == "ЦИКЛ":
            wrap_cycle_up(1111111)
    else:
        pass




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())