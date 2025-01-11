# Membuat sebuah program yang dapat membantu seorang mwngidentifikasi jenis segitiga berdasarkan panjanng ketiga sisinya
# Ada beberapa jenis segitiga berdasarkan kondisi masing-masing sisinya
# Misal segitiga sama sisi, segitiga sama kaki, atau pun segitiga sembarang

def jenis_segitiga(a, b, c):
    if a == b == c:
        return "Segitiga sama sisi"
    
    elif a == b or a == c or b == c:
        return "Segitiga sama kaki"
    
    elif a + b > c and a + c > b and b + c > a:
        return "Segitiga sembarang"
    
    else:
        return "Bukan segitiga"

a = int(input("Masukkan panjang sisi a: "))
b = int(input("Masukkan panjang sisi b: "))
c = int(input("Masukkan panjang sisi c: "))

jenis = jenis_segitiga(a, b, c)
print("Jenis segitiga adalah:", jenis)