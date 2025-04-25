from datetime import datetime

def mesma_data(data1, data2):
	return data1.day == data2.day and data1.month == data2.month and data1.year == data2.year

def new_date(str_data):
	try:
		data = datetime.strptime(str_data,'%d-%m-%Y')
	except:
		data = datetime.now()
	return data

def debug(valor):
	print(valor)
