def maxSums(tri, m):
    # en aşağıdan başlayarak en yukarıya doğru çıkıyor
    for i in range(m - 1, -1, -1):
        for j in range(i + 1):
            # her bir eleman için kontrol edip max olan değeri ekleyerek üste çıkıyor
            # eğer max değere soldaki eleman aracılığı ile ulaşıyorsa ise direkt aşağındaki ile
            # eğer sağdaki eleman aracılığı ile ulaşıyorsa 1 fazlası ile işleme sokuyor.
            if tri[i + 1][j] > tri[i + 1][j + 1]:
                tri[i][j] += tri[i+1][j]
            else:
                tri[i][j] += tri[i + 1][j + 1]

    # max değere sahip elemanı döner
    # print(tri) üçgenin son halini görmek için
    return tri[0][0]


# birden fazla satırdan input almamızı sağlıyor, tek dezavantajı 2 kere enter yapma gerekliliği
def multi_input():
    try:
        while True:
            data = input().split()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return


# verilen sayının asal olup olmadığını belirtmek için kullandığım fonksiyon
def isPrime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# bu kısımda yaptığım kullanıcıdan input alıp onu integer liste çevirmek
# maalesef iki kere enter yapmadan kullanıcıdan aldığı inputu işleme sokmuyor
userInput = (list(multi_input()))
count, j, n = 0, 0, 1
length = len(userInput)
liste = [list(map(int, sub)) for sub in userInput]

# burada yapılan şey ise aslında kod her bir dala giriyor asal olsun veya olmasın ama
# bizden asal sayıları hesaba katmamamız isteniyor. Kod her bir dala gireceği için listedeki her bir asal sayıyı
# çok küçük sayılarla değiştirdim böylece eğer asal olan bir yola girerse sonuç çok küçük çıkacak
# bizden en büyük toplamı bulmamız istendiği için asalların önemi kalmamış oluyor
while length > 0:
    for i in range(n):
        if isPrime(liste[j][i]):
            liste[j][i] = -10000
    length -= 1
    n += 1
    j += 1

a = maxSums(liste, len(liste) - 1)
print(a)