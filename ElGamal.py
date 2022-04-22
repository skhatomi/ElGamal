#SHIDDIQ_KHATOMI_HALIM(1606895796)
from math import gcd
import random
print('''
====================================ElGamal=====================================
Selamat datang di Program ElGamal !
a       : elemen primitif dari Z_p
d       : bilangan random ; d < p
e       : (a^d)mod p
p       : bilangan prima sebagai basis modulus
(e,a,p) : kunci publik
(d,p)   : kunci privat''')
x = "y"
y = 1
while y > 0:
    if x == "y":
        print('''================================================================================
Ketik:
Angka 1 jika ingin membuat kunci
Angka 2 jika ingin mengenkripsi pesan (ASCII)
Angka 3 jika ingin mendekripsi pesan (ASCII)
Angka 4 jika ingin membubuhkan ttd (standard)
Angka 5 jika ingin memverifikasi ttd (standard)
''')
        x = "y"
        y = 1
        pilihan = int(input("Ketik disini: "))

        #Pembangkit Elemen Primitif
        def Elemen_Primitif(p):
            a = []
            koprima = set(i for i in range (1, p) if gcd(i, p) == 1)
            for g in range(1, p):
                Primitif = set(pow(g, pangkat, p) for pangkat in range (1, p))
                if koprima == Primitif:
                    a.append(g)
            return a
        
        #Invers Modulo
        def Invers_Modulo(a, b):
            c = 1
            while (c % a > 0):
                c += b
            return c // a

        #Menginput data list
        def Input_List(a, var):
            print("Masukkan kata 'stop' jika "+var+" sudah lengkap")
            stop = False
            b = 0
            while(not stop):
                a_i = input("Masukkan "+var+" ke-{}: ".format(b+1))
                a.append(a_i)
                b += 1
                if a_i == "stop":
                    stop = True
            a.remove("stop")
            for i in range (0 , len(a)):
                a[i] = int(a[i])
            return a[i]

        #Pembangkit variabel k
        def Variabel_k(y_, p):
            a = 1
            for i in range(0, len(y_)):
                while a > 0:
                    k = random.randint(1, p-2)
                    if gcd(k, p-1) != 1:
                        continue
                    else:
                        k_.append(k)
                        break
            return k_
        
        #Pembuatan kunci
        if pilihan == 1:
            while y > 0:
                if x == "y":
                    p = random.randint(200, 300) #Nilai p dapat diatur disini
                    for i in range(2, p):
                        if p%i == 0:
                            break
                    else:
                        print("Nilai p:" , p)
                        break
                if x == "n":
                    break
                x = "y"
            a = random.choice(Elemen_Primitif(p))
            print("Nilai a:" , a)
            d = random.randint(1, p-1)
            print("Nilai d:" , d)
            e = pow(a, d, p)
            print("Nilai e:" , e)

        #enkripsi
        elif pilihan == 2:
            p = int(input("Masukkan nilai p: "))
            a = int(input("Masukkan nilai a: "))
            e = int(input("Masukkan nilai e: "))
            m = input("Masukkan pesan (plaintext): ")
            y_ = []
            x_ = []
            k_ = []
            for i in range(0, len(m)): 
                y_.append(m[i])
                x_.append(m[i])
            Variabel_k(y_, p)
            for i in range (0, len(y_)):
                y_[i] = ord(y_[i])*pow(e, k_[i])%p
                x_[i] = pow(a, k_[i], p)
            for i in range(0, len(y_)):
                y_.insert(2*i , x_[i])
            print("Ciphertext:" , y_)

        #dekripsi
        elif pilihan == 3:
            p = int(input("Masukkan nilai p: "))
            d = int(input("Masukkan nilai d: "))
            c = []
            Input_List(c, "ciphercode")
            print("Ciphertext : ", c)
            c1 = []
            for i in range(0, len(c)):
                c1.append(c[i])
            a = c1
            for i in range (0, (int((len(a)) / 2))):
                a.pop(i+1)
            b = c
            for i in range (0, (int((len(b)) / 2))):
                b.pop(i)
            pl = []
            for i in range (0, int(len(a))):
                m_ = (b[i] * (pow(a[i], (p - 1 - d)))) % p
                pl.append(m_)
            for i in range (0 , len(pl)):
                pl[i] = chr(int(pl[i]))
            print("Plaintext :", "".join(pl))

        #pembubuhan ttd
        elif pilihan == 4:
            p = int(input("Masukkan nilai p: "))
            a = int(input("Masukkan nilai a: "))
            d = int(input("Masukkan nilai d: "))
            m_ = []
            r_ = []
            t_ = []
            m = input("Masukkan pesan (plaintext): ")
            for i in range(0, len(m)): 
                m_.append(m[i])
                r_.append(m[i])
                t_.append(m[i])
            k_ = []
            Variabel_k(m_, p)
            for i in range(0 , len(m_)):
                r_[i] = pow(a, k_[i], p)
                t_[i] = ((Invers_Modulo(k_[i], p-1))*((ord(m_[i]))-(d*r_[i]))) % (p-1)
            print("m: ",m)
            print("r: ",r_)
            print("t: ",t_)
        #verif ttd
        elif pilihan == 5:
            p = int(input("Masukkan nilai p: "))
            a = int(input("Masukkan nilai a: "))
            e = int(input("Masukkan nilai e: "))
            r_ = []
            t_ = []
            Input_List(r_, "r")
            print("r: ", r_)
            Input_List(t_ , "t")
            print("t: ", t_)
            v = []
            f1 = []
            f2 = []
            m = input("Masukkan pesan: ")
            for i in range(0, len(m)):
                v.append(m[i])
                f1.append(m[i])
                f2.append(m[i])
            for i in range(0 , len(m)):
                f1[i] = (pow(e, r_[i]) * pow(r_[i], t_[i])) % p
                f2[i] = pow(a, ord(v[i]), p)
            if f1 == f2:  
                print("Tanda tangan digital BENAR")
            else:
                print("Tanda tangan digital SALAH")
        else:
            print("Tidak ada pilihan" , pilihan)
    elif x == "n":
          if x == "n":
                break        
    else:
         print("Tidak ada pilihan", x)
    x = input("Kembali ke menu utama?(y/n): ")

