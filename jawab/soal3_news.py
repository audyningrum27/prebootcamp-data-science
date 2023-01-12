import requests

api_key = '89980703ef69479c9c3e7811c6c20333'
category = {
    1: 'technology',
    2: 'business',
    3: 'sports',
    4: 'health',
    5: 'science'
}

print("Selamat datang, mau tahu berita apa hari ini?\n" + 
"[1] Berita seputar teknologi\n" + 
"[2] Berita seputar bisnis\n" +
"[3] Berita seputar olahraga\n" +
"[4] Berita seputar kesehatan\n" +
"[5] Berita seputar science")
inp = int(input("Ketik pilihan Anda [1/2/3/4/5] : "))

news = category[inp]

url = 'https://newsapi.org/v2/top-headlines?country=id&category='+news+'&apiKey='+api_key

articles = requests.get(url)

print('\nBerikut adalah top 5 berita Indonesia bidang ' +  category[inp] + ':')

i = 0
while i < 5:
    print('{} - {}'.format(i+1, articles.json()['articles'][i]['title']))
    i += 1