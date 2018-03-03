def adamBasiCiroHesapla():
    a=int(input("satış miktarını giriniz:"))
    b=int(input("birim satış fiyatını giriniz:"))
    c=int(25)
    adamBasiCiro=(a*b)/c
    print("adam başı ciro:",adamBasiCiro)





pus=int(input("planlanmış üretim süresi gir:"))
pd=int(input("plansız duruş gir:"))
scz=int(input("standart çevrim zamanı gir:"))
um=int(input("üretim miktarı gir"))
suM=int(input("sağlam ürün miktarı gir:"))
tum=int(input("toplam üretim miktarı gir:"))

kullanılabilirlik=(pus-pd)/pus
performans=(scz*um)/(pus-pd)
kalite=suM/tum
oee=kullanılabilirlik*performans*kalite
def kullanılabilirlik_():
  print(kullanılabilirlik)
def perf():
  print(performans)
def kalite_():
  print(kalite)
def etkililikOran():
  print("%",oee)





a=int(input("finansman geliri gir:")) 
b=int(input("pazar geliri gir:"))
c=int(input("kira geliri gir:"))

d=int(input("ücret gir:"))
e=int(input("finansman gideri gir:"))
f=int(input("pazar gideri gir:"))
g=int(input("kira gideri gir:"))
h=int(input("muhasebe gideri gir:"))

gelirToplam=a+b+c
giderToplam=d+e+f+g+h
def cikar(gelirToplam,giderToplam):
    print (gelirToplam-giderToplam)
if (gelirToplam-giderToplam)>1000:
    print("kar ettiniz")
else:
    print("zarar")



