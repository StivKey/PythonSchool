import time
import locale
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# result = finish - start
# print(result)


locale.setlocale(locale.LC_ALL, "RU") # Русифицируем дату время и т.п locale (Подключая данный модуль)
print(time.strftime("Сегодня:  %B %d, %Y", time.localtime()))