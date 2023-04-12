"""Напишите приложение на Python, которое будет принимать на вход текстовый документ и создавать из него таблицу. Для этого задания необходимо выполнить следующие шаги:

1. Реализуйте функцию, которая будет принимать на вход путь к текстовому документу и возвращать его содержимое в виде строки.
2. Напишите функцию, которая будет разбивать текст на строки и создавать список списков, где каждый подсписок будет соответствовать строке в таблице.
3. Реализуйте функцию, которая будет определять количество столбцов в таблице. Для этого можно использовать первую строку текста и подсчитывать количество разделителей (например, запятых или табуляций).
4. Напишите функцию, которая будет формировать таблицу из списка списков строк. Для этого можно использовать библиотеку pandas, которая предоставляет удобный интерфейс для работы с таблицами.
5. Реализуйте функцию, которая будет записывать таблицу в файл. Формат файла может быть любым, например, CSV или Excel.
6. Предусмотрите обработку ошибок и ввод корректных данных. 


Например, в качестве такого файла может быть список студентов группы, список товаров и т.д."""


import pandas as pd
import openpyxl


def text_file_txt(path: str):
	with open(path, 'r') as f:
		text = f.read()
	return text


def split_rows(text: str):
	rows = []
	for i in text.split('\n'):
		row = i.split('\t')
		rows.append(row)
	return rows


def count(rows):
	return len(rows[0])


def table(rows):
	headers = rows[0]
	data = rows[1:]
	table = pd.DataFrame(data, columns=headers)
	return table


def table_on_file(table, path):
	if path.endswith('.csv'):
		table.to_csv(path, index=False)
	elif path.endswith('.xlsx'):
		table.to_excel(path, index=False)
	else:
		raise ValueError("Неподерживаемый тип файла.")
	

try:
	# Вывод текста из файла
	path = input('Введите путь до файла: ')
	text = text_file_txt(path)
	print(f"Содержимое файла:\n{text}")

	# Вывод списка списков  
	row = split_rows(text)
	print(f"\nСписок списков строк:\n{row}")

	# Вывод количества столбцов в тексте
	col = count(row)
	print(f'\nКоличество столбцов: {col}')

	# Вывод таблицы
	table = table(row)
	print(table)

	# Таблица в csv/xlsx файле
	path_to_csv = input('\nВведите путь к файлу csv/excel: ')
	table_on_file(table, path_to_csv)

except FileNotFoundError:
	print('Файл не найден или не существует.')
except ValueError as e:
	print(e)
