from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='a0bfbd693b28439e85cb4d78dd2ff42a')

print("Selamat datang, mau tahu berita apa hari ini?\n" + 
"[1] Berita seputar teknologi\n" + 
"[2] Berita seputar bisnis\n" +
"[3] Berita seputar olahraga\n" +
"[4] Berita seputar kesehatan\n" +
"[5] Berita seputar science")
inp = int(input("Ketik pilihan Anda [1/2/3/4/5] : "))

def news(nilai) :
    if inp == 1:
        return newsapi.get_top_headlines(category='technology', country='id')
    if inp == 2:
        return newsapi.get_top_headlines(category='business', country='id')
    if inp == 3:
        return newsapi.get_top_headlines(category='sports', country='id')
    if inp == 4:
        return newsapi.get_top_headlines(category='health', country='id')
    if inp == 5:
        return newsapi.get_top_headlines(category='science', country='id')


print(news(inp))