import requests
#zaleznie od strony, czasem odpala od razu a czasem po którymś odpalaniu programu (nie wyrzuca błędu ale też nie zapisuje zawsze do pliku)
e = open("end.txt","w")
e.write("")
e.close()


class AppCrawler:

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.apps = []

    def crawl(self):
        self.get_app_from_link(self.starting_url)
        return

    def  get_app_from_link(self, link):
        start_page = requests.get(link)
        f = open("plik.txt", "w", encoding="UTF-8")
        f.write(start_page.text)
        f.close()

        return


crawler = AppCrawler("https://www.nba.com/amp/league/standings", 0)
crawler.crawl()

f = open("plik.txt", "r", encoding="UTF-8")
tab = []
stats = []
titles = []
for x in f:
    line = x.strip()
    tab.append(line)
f.close()

for x in range(len(tab)):
    if tab[x].startswith("<td"):
        if tab[x+1].startswith("<a"):
            stats.append(tab[x + 1].replace("<span>", "").replace("</span>", "").replace('<a href="//nba.com/teams/',"").replace('">',"") + "\n")
        else:
            stats.append(tab[x+1].replace("<span>","").replace("</span>","") + "\n")
    elif tab[x].startswith("<th") and tab[x+1] != "<tr>":
        titles.append(tab[x+1].replace('<span class="show-for-sr">',"").replace('</span>',""))

titles = titles * 11
e = open("end.txt","w",encoding="UTF-8")
for x in range(len(titles)):
    if x < len(stats) and (x+1)%11 == 0:
        e.write(titles[x] + ": " + stats[x]+"\n")
    elif x < len(stats):
        e.write(titles[x] + ": " + stats[x])

e.close()

