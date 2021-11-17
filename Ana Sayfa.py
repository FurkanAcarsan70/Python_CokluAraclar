import tkinter as Main
Sayfa = Main.Tk()
Sayfa.configure(background='dark grey')
Sayfa.geometry("500x500+500+200")
Sayfa.title('Kullanışlı Araçlar')
Sayfa.iconphoto(True, Main.PhotoImage(file='D:\Python Projelerim\Çoklu Araçlar\Blue-Utilities-icon.png'))
def Hesap_Makinesi():
    SayıGirişi = Main.Entry(Sayfa, width=70, justify='right')
    SayıGirişi.place(x=40, y=150)
    Butonlar = []

    def Sayılar(B):
        i = len(SayıGirişi.get())
        SayıGirişi.insert(i, str(B))

    for A in range(1, 10):
        Butonlar.append(
            Main.Button(Sayfa, text=str(A), fg='light blue', command=lambda B=A: Sayılar(B), width=5, height=3))
    Sayaç = 0
    for C in range(1, 4):
        for D in range(1, 4):
            Butonlar[Sayaç].place(x=20 + D * 50, y=60 * C + 140)
            Sayaç += 1
    Sıfır = Main.Button(Sayfa, text='0', fg='light blue', command=lambda Z=0: Sayılar(Z), width=5, height=3)
    Sıfır.place(x=70, y=380)
    Nokta = Main.Button(Sayfa, text='.', fg='red', command=lambda G='.': Sayılar(G), width=5, height=3)
    Nokta.place(x=120, y=380)
    İkinciSayı = 0

    def Hesaplama():
        global İlkSayı
        global Numara
        global İkinciSayı
        İkinciSayı = float(SayıGirişi.get())
        if (Numara == 0):
            Toplam = İlkSayı + İkinciSayı
        elif (Numara == 1):
            Toplam = İlkSayı - İkinciSayı
        elif (Numara == 2):
            Toplam = İlkSayı / İkinciSayı
        else:
            Toplam = İlkSayı * İkinciSayı
        SayıGirişi.delete(0, Main.END)
        SayıGirişi.insert(0, str(Toplam))

    Eşittir = Main.Button(Sayfa, text='=', fg='red', command=Hesaplama, width=5, height=3)
    Eşittir.place(x=170, y=380)
    İşaret = []
    Numara = 0
    İlkSayı = 0

    def İşaretler(e):
        global Numara
        Numara = e
        global İlkSayı
        İlkSayı = float(SayıGirişi.get())
        SayıGirişi.delete(0, Main.END)

    for E in range(0, 4):
        İşaret.append(Main.Button(Sayfa, fg='dark red', command=lambda e=E: İşaretler(e), width=5, height=3))
    İşaret[0]['text'] = '+'
    İşaret[1]['text'] = '-'
    İşaret[2]['text'] = '/'
    İşaret[3]['text'] = '*'
    for a in range(0, 4):
        İşaret[a].place(x=220, y=60 * a + 200)

    def silme():
        Uzunluk = len(SayıGirişi.get())
        SayıGirişi.delete(Uzunluk - 1, Main.END)

    Silme = Main.Button(Sayfa, text='Sil', fg='dark red', command=silme, width=5, height=3)
    Silme.place(x=270, y=200)

    def temizle():
        SayıGirişi.delete(0, Main.END)

    Temizleme = Main.Button(Sayfa, text='Temizle', fg='dark red', command=temizle, width=5, height=3)
    Temizleme.place(x=270, y=260)
Hesapla = Main.Button(Sayfa, text='Hesap Makinesi', fg='dark blue', command=Hesap_Makinesi, width=15, height=2)
Hesapla.place(x=20, y=10)
def Oto_Kapat():
    Kapatma_Sınıfı()
def Kapatma_Sınıfı():
    import tkinter as Home
    import os as Kodlar
    from tkinter import messagebox
    global Sayfa
    Sayfa.destroy()
    Page = Home.Tk()
    Page.title('Otomatik Kapatma')
    Page.geometry('500x500+500+200')
    Page.iconphoto(False, Home.PhotoImage(file='D:\Python Projelerim\Çoklu Araçlar\Kapat.png'))
    Page.configure(background = 'dark grey')
    def AnaSayfa():
        pass
    GeriDön = Home.Button(Page, text = 'Ana Sayfa', fg = 'red', command = AnaSayfa, width = 15, height = 2)
    GeriDön.place(x = 10, y = 10)
    Bilgi = Home.Label(Page, text = 'Lütfen Saat Giriniz.', fg = 'silver')
    Bilgi.place(x = 20, y = 130)
    Saat = Home.Entry(Page, width = 70, justify = 'right')
    Saat.place(x = 20, y = 150)
    İkinciBilgi = Home.Label(Page, text = 'Lütfen Dakika Giriniz.', fg = 'silver')
    İkinciBilgi.place(x = 20, y = 170)
    Dakika = Home.Entry(Page, width = 70, justify = 'right')
    Dakika.place(x = 20, y = 190)
    def PcKapat():
        if(Saat != '' and Dakika != ''):
            saat = int(Saat.get())
            dakika = int(Dakika.get())
            Uyarı = Home.messagebox.askquestion('Kapatma', 'Bilgisayarı Kapatmak İstediğinize Emin misiniz')
            if(Uyarı == 'yes'):
                saatsan = saat * 3600
                dakikasan = dakika * 60
                Toplam_Süre = saatsan + dakikasan
                Kodlar.system('shutdown /s -t %s'% Toplam_Süre)
                messagebox.showinfo('Kapatma', f'Bilgisayarınız {saat}saat, {dakika}dakika sonra kapatılacaktır.')
        else:
            messagebox.showerror('Hata', 'Saat ve Dakika girmeden bu işlemi gerçekleştiremezsiniz!')
    Kapatma = Home.Button(Page, text = 'Bilgisayarı Kapat', fg = 'blue', command = PcKapat, width = 15, height = 2)
    Kapatma.place(x = 20, y = 220)
    def PcYenidenBaşlat():
        if(Saat != '' and Dakika != ''):
            saat = int(Saat.get())
            dakika = int(Dakika.get())
            Uyarı = messagebox.askquestion('Yeniden Başlatma', 'Bilgisayarı Yeniden Başlatmak İstediğinize Emin misiniz?')
            if(Uyarı == 'yes'):
                saatsan = saat * 3600
                dakikasan = dakika * 60
                Toplam_Süre = saatsan + dakikasan
                Kodlar.system('shutdown /r -t %s' %Toplam_Süre)
                messagebox.showinfo('Yeniden Başlatma', f'Bilgisayarınız {saat}saat, {dakika}dakika sonra yeniden başlatılacaktır.')
        else:
            messagebox.showerror('Hata', 'Saat ve Dakika girmeden işlem yapamazsınız!')
    YenidenBaşlat = Home.Button(Page, text = 'Yeniden Başlat', fg = 'blue', command = PcYenidenBaşlat, width = 15, height = 2)
    YenidenBaşlat.place(x = 140, y = 220)
    def PcKapatmaİptal():
        Kodlar.system('shutdown -a')
        messagebox.showinfo('Kapatma', 'Bilgisayarı otomatik kapatma iptal edildi.')
    İptalEt = Home.Button(Page, text = 'İptal et', fg = 'red', command = PcKapatmaİptal, width = 15, height = 2)
    İptalEt.place(x = 260, y = 220)
    Page.mainloop()
Kapat = Main.Button(Sayfa, text='Oto Kapat', fg='dark blue', command=Oto_Kapat, width=15, height=2)
Kapat.place(x=140, y=10)
Sayfa.mainloop()
