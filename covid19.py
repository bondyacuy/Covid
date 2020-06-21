from bs4 import BeautifulSoup as Bs # Mengimport Module BeautifulSoup Dari Module bs4
import requests, os # Mengimport Module requests dan Module os

os.system('clear') # Melakukan clear ( pembersihan )
print 'Tools : Update Covid 19'
print '>>>>>>>>> ( ? ) <<<<<<<<<'
print
covid = requests.get('http://covid19.go.id') # Memproses Permintaan HTTP
soup = Bs(covid.text, 'html.parser') # Parser
find_1 = soup.find_all('strong') # Mencari Tag "<strong>"
find_2 = soup.find_all('div', {'class' : 'pt-4 text-color-grey text-1'}) # Mencari Tag "div" dengan class tertentu
find_3 = soup.find_all('div', {'class' : 'pt-4 text-color-black text-1'}) # Mencari Tag "div" dengan class tertentu
negara = find_1[0].text # Memuat Index dan Mengambil data ( text )
terkonfirmasi = find_1[1].text # Memuat Index dan Mengambil data ( text )
meninggal_global = find_1[2].text # Memuat Index dan Mengambil data ( text )
keterangan_global = find_2[0].text # Memuat Index dan Mengambil data ( text )
positif_indo = find_1[3].text # Memuat Index dan Mengambil data ( text )
sembuh_indo = find_1[4].text # Memuat Index dan Mengambil data ( text )
meninggal_indo = find_1[5].text # Memuat Index dan Mengambil data ( text )
keterangan_indo = find_3[0].text # Memuat Index dan Mengambil data ( text )
print '\tGLOBAL ( Dunia )'
print '============ LIVE ============='
print 'Jumlah Negara :', negara
print 'Terkonfirmasi :', terkonfirmasi
print 'Meninggal :', meninggal_global
print keterangan_global
print '\tINDONESIA'
print '============ LIVE ============='
print 'Positif :', positif_indo
print 'Sembuh :', sembuh_indo
print 'Meninggal :', meninggal_indo
print keterangan_indo