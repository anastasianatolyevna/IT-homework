# Соединяем Питона с БД
import mysql.connector
import decimal

# Коннектимся к нашей БД
conn = mysql.connector.connect(
    user="root",
    password="891109",
    host="localhost"
   )
curs = conn.cursor()

# Использование БД, созданной в MySQL
curs.execute("""USE tradein;""")

# Открываем файл OrderLog для импорта данных в БД
data = open('TradeLog20160114.txt').read()

# Формируем список из первых 100 записей (для экономии времени и места :) )
lines = data.split('\n')[1:100]

# Заполняем таблицу OrdLog данными из файла OrderLog20160114.txt и делаем проверку
# повторного запуска скрипта без занесения старых записей в БД
for i, elem in enumerate(lines):
    try:
        t = ''
        for field in elem.split(',')[1:]:
            try:
                float(field)
            except Exception:
                # Если поле пустое, то ставим 0
                if field == '':
                    t += '0, '
                else:
                    t += f"'{field}', "
            else:
                t += f'{field}, '
        request = f"""INSERT INTO ordlog(seccode, buysell, time, orderno, action, price, volume, tradeno, tradeprice) VALUES ({t[:-2]});"""
        curs.execute(request)       
    except Exception as e:
        pass
    
conn.commit()

# Делаем запрос на получение всех данных из таблицы OrdLog
curs.execute("""SELECT * from ordlog;""")

# Получаем результат сделанного запроса
rows = curs.fetchall()

# -----Разбиваем таблицу OrdLog на 3 новых--------

# Открываем файл с тикерами
tickers_text = open('ListingSecurityList_new.csv', encoding = "cp1251").read()

tickers = {}
for elem in tickers_text.split('\n')[:-1]:
    t = elem.split(',')
    tickers[t[7].replace("\"", "")] = t[5].replace("\"", "")

# Проверка возможности повторного запуска скрипта без занесения старых записей в БД
for record in rows:
    try:
        if tickers[record[1]] == 'Акция привилегированная':
            t = f"""INSERT INTO PreferredStock(seccode, buysell, time, orderno, action, price, volume, tradeno, tradeprice) VALUES {tuple(elem if type(elem) != decimal.Decimal else float(elem) for elem in record[1:])};"""
            curs.execute(t)
        elif tickers[record[1]] == 'Акция обыкновенная':
            t = f"""INSERT INTO CommonStock(seccode, buysell, time, orderno, action, price, volume, tradeno, tradeprice) VALUES {tuple(elem if type(elem) != decimal.Decimal else float(elem) for elem in record[1:])};"""
            curs.execute(t)
        elif 'облигац' in tickers[record[1]].lower():
            t = f"""INSERT INTO Bonds(seccode, buysell, time, orderno, action, price, volume, tradeno, tradeprice) VALUES {tuple(elem if type(elem) != decimal.Decimal else float(elem) for elem in record[1:])};"""
            curs.execute(t)
    except Exception as e:
        pass
conn.commit()

# Получаем список обыкновенных акций и считаем общее их количество
curs.execute("""SELECT * from CommonStock;""")
rows = curs.fetchall()
all_tickers = {}
for r in rows:
    if r[1] in all_tickers:
        all_tickers[r[1]] += 1
    else:
        all_tickers[r[1]] = 0
# Находим максимальный тикер(тот, который больше всего встретился) 
t = max(all_tickers, key=lambda x: all_tickers[x])
# Выводим на экран
print('Тикер, по которому было сделано больше всего сделок: ', t, ', в количестве: ', all_tickers[t])

