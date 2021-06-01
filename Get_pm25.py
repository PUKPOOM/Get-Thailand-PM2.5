from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import csv
import os.path

def Get_PM25(city, region):
	'Start Get_PM25'
	print('\n##### P M 2 . 5 | S T A R T #####')
	print('City : {} | Region : {}' .format(city, region))

	# from http://berkeleyearth.lbl.gov/air-quality/maps/cities/Thailand/
	url = 'http://berkeleyearth.lbl.gov/air-quality/maps/cities/Thailand/' + city + '/' + region + '.txt'
	web_open = req(url)
	html = web_open.read()			
	web_open.close()
	##print("Closed or not : ", web_open.closed)
	##print(html)
	##print(len(html))

	raw_data = str(html, 'utf-8')				# convert byte to str
	##print(raw_data)
	##print(type(raw_data))
	##print(len(raw_data))

	data = raw_data.split('\t')					# split by '\t'
	##print(data)
	print('Data Count = {}' .format(len(data)))

	header = raw_data.split('% ')
	del(header[0])
	del(header[9:])
	header = [idx.replace("\r\n","") for idx in header]	# remove '\r\n'
	header = [idx.split(': ') for idx in header]		# # split by ': '
	print(header)

	pm25_data = []
	for idx in range(0, len(data), 6):
		##print('INDEX : {} = {}' .format(idx, data[idx]))]
		try:
			pm25_data.append((data[idx][-4:], data[idx+1], data[idx+2], data[idx+3], data[idx+4]))	# Year, Month, Day, Hour, PM2.5
		except:
			continue
	##print(pm25_data)

	filename = 'PM25.csv'
	file_exists = os.path.isfile(filename)
	with open(filename,'a', newline="") as f:
		fw = csv.writer(f)
		row_list = []
		if not file_exists:
			row_list = ['Country', 'City', 'Region', 'Population', 'Latitude', 'Longitude', 'Time Zone',
						'Year', 'Month', 'Day', 'Hour', 'PM2.5']
			fw.writerow(row_list)
		for idx in range(len(pm25_data)):
			row_list = []
			row_list.append(header[0][1])
			row_list.append(header[1][1])
			row_list.append(header[3][1])
			row_list.append(header[5][1])
			row_list.append(header[6][1])
			row_list.append(header[7][1])
			row_list.append(header[8][1])
			row_list.append(pm25_data[idx][0])
			row_list.append(pm25_data[idx][1])
			row_list.append(pm25_data[idx][2])
			row_list.append(pm25_data[idx][3])
			row_list.append(pm25_data[idx][4])
			fw.writerow(row_list)

##city = 'Bangkok'
##region = 'Bangkok'
##Get_PM25(city, region)

city_set = [('Bangkok','Bangkok'), ('Chaiyaphum','Chaiyaphum'), ('Changwat_Ubon_Ratchathani','Ubon_Ratchathani'), ('Changwat_Udon_Thani','Udon_Thani'), ('Chanthaburi','Chanthaburi'), ('Chiang_Mai','Chiang_Mai'),
			('Chiang_Rai','Chiang_Rai'), ('Chon_Buri','Chon_Buri'), ('Chon_Buri','Sattahip'), ('Chon_Buri','Si_Racha'), ('Chumphon','Chumphon'),
			('Kalasin','Kalasin'), ('Kamphaeng_Phet','Kamphaeng_Phet'), ('Kanchanaburi','Kanchanaburi'), ('Kanchanaburi','Tha_Maka'), ('Khon_Kaen','Khon_Kaen'), ('Khon_Kaen','Khon_Kaen'),
			('Lampang','Lampang'), ('Lop_Buri','Lop_Buri'), ('Maha_Sarakham','Maha_Sarakham'), ('Nakhon_Pathom','Nakhon_Pathom'), ('Nakhon_Ratchasima','Nakhon_Ratchasima'), ('Nakhon_Sawan','Nakhon_Sawan'),
			('Nakhon_Si_Thammarat','Nakhon_Si_Thammarat'), ('Nong_Khai','Nong_Khai'), ('Nonthaburi','Bang_Kruai'), ('Nonthaburi','Mueang_Nonthaburi'), ('Nonthaburi','Pak_Kret'),
			('Pathum_Thani','Ban_Lam_Luk_Ka'), ('Pathum_Thani','Khlong_Luang'), ('Pattaya','Phatthaya'), ('Phetchabun','Phetchabun'), ('Phitsanulok','Phitsanulok'), ('Phra_Nakhon_Si_Ayutthaya','Phra_Nakhon_Si_Ayutthaya'),
			('Phuket','Ban_Talat_Yai'), ('Phuket','Phuket'), ('Prachuap_Khiri_Khan','Hua_Hin'), ('Ratchaburi','Ban_Pong'), ('Ratchaburi','Ratchaburi'), ('Rayong','Klaeng'), ('Rayong','Rayong'),
			('Sakon_Nakhon','Sakon_Nakhon'), ('Samut_Prakan','Phra_Pradaeng'), ('Samut_Prakan','Samut_Prakan'), ('Samut_Sakhon','Krathum_Baen'), ('Samut_Sakhon','Samut_Sakhon'),
			('Sara_Buri','Phra_Phutthabat'), ('Sara_Buri','Saraburi'), ('Surat_Thani','Ko_Samui'), ('Surat_Thani','Surat_Thani'), ('Trang','Trang'), ('Uttaradit','Uttaradit'), ('Yala','Yala')]
for city, region in city_set:
	Get_PM25(city, region)