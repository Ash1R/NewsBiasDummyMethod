import csv

with open("allsides_data.csv") as allsides:
    read = csv.reader(allsides)
    alldata = list(read)

ratingdict = {i[0]:i[1] for i in alldata[1:]}


with open("<input topical MIT bias file>") as afile:
    reader = csv.reader(afile)
    data = list(reader)

biasvals = {"center":0, "left-center":-1, "right-center":1.14, "left":-2, "right":2.28}

conversiond = {'aljazeera':'Al Jazeera', 'alternet':'AlterNet', 'americanconservative': 'American Conservative Union', 'americanthinker':'American Thinker', 'ap':'Associated Press', 'atlantic':'The Atlantic', 'axios':'Axios', 'bbc': 'BBC News', 'breitbart':'Breitbart News',  'businessinsider':'Business Insider', 'buzzfeed':'BuzzFeed News', 'cbs': 'CBS News', 'cnbc':'CNBC', 'cnn': 'CNN (Web News)', 'dailycaller':'The Daily Caller', 'dailykos':'Daily Kos', 'dailymail':'Daily Mail', 'dailywire':'The Daily Wire', 'economist':'The Economist', 'federalist':'The Federalist', 'fox': 'Fox Online News', 'guardian': 'The Guardian', 'huffingtonpost': 'HuffPost', 'infowars':'InfoWars', 'jacobinmag':'Jacobin','motherjones':'Mother Jones', 'nationalreview': 'National Review', 'nbc':'NBCNews.com', 'npr':'NPR Online News', 'nypost': 'New York Post', 'nytimes' : 'New York Times - News', 'pbs':'PBS NewsHour', 'pjmedia': 'PJ Media', 'rawstory': 'Raw Story', 'redstate': 'Red State', 'reuters': 'Reuters', 'slate': 'Slate', 'spectator': 'American Spectator', 'techcrunch': 'TechCrunch', 'time': 'Time Magazine', 'townhall': 'Townhall', 'truthdig': 'Truthdig', 'usatoday': 'USA TODAY', 'verge': 'The Verge', 'vice': 'Vice', 'vox': 'Vox', 'wapo': 'Washington Post', 'wsj': 'Wall Street Journal - News'
}


counter = [0, 0, 0, 0, 0]
termlst = {}
avg = 0
cons = 0
libs = 0
for i in data[1:]:
    val = 0
    for j in range(2, len(i)):
        try:
            z = conversiond[data[0][j]]
        except:
            continue

        val += (int(i[j]) * biasvals[ratingdict[conversiond[data[0][j]]]])
        if (biasvals[ratingdict[conversiond[data[0][j]]]] == -2):
            counter[0] += 1
        if (biasvals[ratingdict[conversiond[data[0][j]]]] == -1):
            counter[1] += 1
        if (biasvals[ratingdict[conversiond[data[0][j]]]] == 0):
            counter[2] += 1
        if (biasvals[ratingdict[conversiond[data[0][j]]]] == 1):
            counter[3] += 1
        if (biasvals[ratingdict[conversiond[data[0][j]]]] == 2):
            counter[4] += 1



    termlst[i[0]] = val
    avg += val
avg = avg / len(termlst)
for i in termlst:
    termlst[i] = termlst[i] - avg

print(termlst)

with open('<insert article in .txt file>', 'r') as rart:
    article = rart.read().replace('\n', '')
print(article)
article = article.lower()
art = article.split(" ")

for i in art:
    i = i.lower()

ntlst = {}
for i in termlst:
    ntlst[i.lower()] = termlst[i]

val = 0
for i in art:
    if i in ntlst:
        val += ntlst[i]
        print(i)
for i in range(0, len(art) -1):
    if (" ".join([ art[i], art[i+1] ] )) in ntlst:
        val += ntlst[(" ".join([art[i], art[i+1]]))]
        print((" ".join([art[i], art[i+1]])))

for i in range(0, len(art) -2):
    if (" ".join([art[i], art[i+1], art[i+2]])) in ntlst:
        val += ntlst[(" ".join([art[i], art[i+1], art[i+2]]))]
        print((" ".join([art[i], art[i+1], art[i+2]])))

print()
if (val < 0):
    print("liberal")
else:
    print("conservative")



