class Main(object):
    def __init__(self, place, num, sport, comp):
        self.place = place
        self.num = num
        self.sport = sport
        self.comp = comp
with open('helsinki.txt') as f:
    data_read = [i.strip().split(" ") for i in f.readlines()]
data = []
for i in data_read:
    data.append(Main(i[0], i[1], i[2], i[3]))

#3.Fel
print("3.feladat\nPontszerző helyezések száma:", len(data))
#4.Fel
gold = 0
silver = 0
bronze = 0
for i in data:
    if i.place == '1':
        gold = gold + 1
    elif i.place == '2':
        silver = silver + 1
    elif i.place == '3':
        bronze = bronze + 1
print("4.feladat\nArany:", str(gold), "\nEzüst:", str(silver), '\nBronz:', str(bronze), '\nÖsszesen:', str(gold + silver + bronze))
#5.fel
score = 0
for i in data:
    if i.place == '1':
        score = score + 7
    elif i.place == '2':
        score = score + 5
    elif i.place == '3':
        score = score + 4
    elif i.place == '4':
        score = score + 3
    elif i.place == '5':
        score = score + 2
    elif i.place == '6':
        score = score + 1
print('5.feladat\nOlimpiai pontok száma:', str(score))
#6.fel
sports = []
for i in data:
    if i.sport in sports:
        pass
    sports.append(i.sport)
print(sports)
#idk hogy kell meguntam
