jenis_komponen = ["mpff form", "control horn", "push rod wire", "brushless motor", "linkage stopper", "esc", "receiver", "carbon fiber", "servo", "rc lipo battery", "fropeller,flysky"]
harga_komponen = [23,3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]

print("HARGA KOMPONEN MPFF=RM23,CONTROL HORN=RM3,PUSH ROD WIRE=RM2,BRUSHLESS MOTOR=RM15.79,LINKAGE STOPPER=RM12,ESC=RM67,RECEIVER=RM61,CARBON FIBER=25.30,SERVO=RM5.20,RC LIPO BATTERY=RM57.56,FROPELLER=RM5.50,FLYSKY=RM161")
a=int(input("Masukkan tempahan untuk mpff form:"))
b=int(input("Masukkan tempahan untuk control horn:"))
c=int(input("Masukkan tempahan untuk rod wire:"))
d=int(input("Masukkan tempahan untuk brushless motor:"))
e=int(input("Masukkan tempahan untuk linkage stopper:"))
f=int(input("Masukkan tempahan untuk esc:"))
g=int(input("Masukkan tempahan untuk receiver:"))
h=int(input("Masukkan tempahan untuk carbon fiber:"))
i=int(input("Masukkan tempahan untuk servo:"))
j=int(input("Masukkan tempahan untuk rc lipo battery:"))
k=int(input("Masukkan tempahan untuk fropeller:"))
l=int(input("Masukkan tempahan untuk flysky:"))

tempahan = [a,b,c,d,e]

def jumlah_harga() :
    for i in range(4):
        jumlah[i] = harga_komponen[i]*tempahan[i]
    return(jumlah) 

def cetak() :
        print("\n\nTempatan anda ialah:")
        print(a,"komponen", jenis_komponen[0])
        print(b,"komponen", jenis_komponen[1])
        print(c,"komponen", jenis_komponen[2])
        print(d,"komponen", jenis_komponen[3])
        print(e,"komponen", jenis_komponen[4])
        print(f,"komponen", jenis_komponen[5])
        print(g,"komponen", jenis_komponen[6])
        print(h,"komponen", jenis_komponen[7])
        print(i,"komponen", jenis_komponen[8])
        print(j,"komponen", jenis_komponen[9])
        print(k,"komponen", jenis_komponen[10])
        print(l,"komponen", jenis_komponen[11])

        print ("\n Jumlah harga untuk tempatan ialan RM",sum (jumlah))
jumlah_harga()
cetak()

