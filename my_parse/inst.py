from instabot import Bot
import time
import shutil

"""
Источник Интсаграмм

На вход программе подяется 2 имени пользователя
Задача программы найти самую короткую цепоччку рукопожатий между этими пользователями

рукопожатием считаем только взаимоподписанных пользовтаелей
"""

shutil.rmtree(r"C:\Users\aermo\data_mining\my_parse\config", ignore_errors=True)  # не запускается с созданным config
bot = Bot()
username = input("Введите логин")
paswrd = input("Введите пароль")
bot.login(username=username, password=paswrd)
print("Привет! Я попробую найти связь между двумя пользователями инстаграма через цепочку рукопожатий")
name_1 = input("Введите первого пользователя")
name_2 = input("Введите второго пользователя")
user_1 = bot.get_user_id_from_username(name_1)
user_2 = bot.get_user_id_from_username(name_2)

print(" Процесс займёт длительное время, ожидайте")
user_following_1 = bot.get_user_following(user_1)  # подписки первого пользователя
connections = []

# первое рукопожатие
for a in user_following_1:
    time.sleep(10)
    if user_2 in bot.get_user_following(a) and a in bot.get_user_following(user_2):
        connections.append(f"{user_1} - {a} - {user_2}")
    elif user_1 in bot.get_user_following(a):
        time.sleep(15)
        # второе рукопожатие
        for b in bot.get_user_following(a):
            time.sleep(25)
            if user_2 in bot.get_user_following(b) and b in bot.get_user_following(user_2):
                connections.append(f"{user_1} - {a} - {b} - {user_2}")
            elif a in bot.get_user_following(b):
                time.sleep(15)
                # третье рукопожатие
                for c in bot.get_user_following(b):
                    time.sleep(15)
                    if user_2 in bot.get_user_following(c) and c in bot.get_user_following(user_2):
                        connections.append(f"{user_1} - {a} - {b} - {c} - {user_2}")
                    elif b in bot.get_user_following(c):
                        time.sleep(15)
                        # четвёртое рукопожатие
                        for d in bot.get_user_following(c):
                            time.sleep(15)
                            if user_2 in bot.get_user_following(d) and d in bot.get_user_following(user_2):
                                connections.append(f"{user_1} - {a} - {b} - {c} - {d} - {user_2}")
                            elif c in bot.get_user_following(d):
                                time.sleep(15)
                                # пятое рукопожатие
                                for i in bot.get_user_following(d):
                                    time.sleep(5)
                                    if user_2 in bot.get_user_following(i) and i in bot.get_user_following(user_2):
                                        connections.append(f"{user_1} - {a} - {b} - {c} - {d} - {i} - {user_2}")
                                    elif d in bot.get_user_following(i):
                                        time.sleep(15)
                                        # шестое рукопожатие
                                        for f in bot.get_user_following(i):
                                            time.sleep(15)
                                            if user_2 in bot.get_user_following(f) and f in bot.get_user_following(
                                                    user_2):
                                                connections.append(f"{user_1} - {a} - {b} - {c} - {d} - {i} - {f} - {user_2}")
                                            else:
                                                pass
                                    else:
                                        pass
                            else:
                                pass
                    else:
                        pass
            else:
                pass
    else:
        pass

print(f"Связи которые мы нашли: {connections}")


