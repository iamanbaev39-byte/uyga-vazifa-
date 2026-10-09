son = int(input("Juft son kiriting: "))
if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas")

print()

yosh = int(input("Yoshingizni kiriting: "))
if yosh >= 4 and yosh <= 60:
    if yosh < 18:
        print("10000 so'm")
    else:
        print("20000 so'm")
else:
    print("Bepul")

print()

son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
if son1 < son2:
    print(son1, "<", son2)
else:
    if son1 > son2:
        print(son1, ">", son2)
    else:
        print(son1, "==", son2)

print()

mahsulotlar = []
print("Do'kondagi 10 ta mahsulotni kiriting:")
for i in range(10):
    mahsulot = input("Mahsulot: ")
    mahsulotlar.append(mahsulot)

savat = []
print("Savatga 5 ta mahsulot kiriting:")
for i in range(5):
    mahsulot = input("Mahsulot: ")
    savat.append(mahsulot)

for i in range(5):
    if savat[i] in mahsulotlar:
        print(savat[i], "- do'konda bor")
    else:
        print(savat[i], "- do'konda yo'q")
