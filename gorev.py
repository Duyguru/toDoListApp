import tkinter as tk
from tkinter import messagebox, simpledialog
import os

DOSYA_ADI = "gorevler.txt"

def gorevleri_yukle():
    if not os.path.exists(DOSYA_ADI):
        return []
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as f:
            return [satir.strip() for satir in f.readlines()]
    except Exception as e:
        messagebox.showerror("Hata", f"Görevler yüklenirken hata oluştu: {e}")
        return []

def gorevleri_kaydet():
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as f:
            for gorev in gorevler:
                f.write(gorev + "\n")
    except Exception as e:
        messagebox.showerror("Hata", f"Görevler kaydedilirken hata oluştu: {e}")

def listeyi_guncelle():
    liste_kutusu.delete(0, tk.END)
    for i, gorev in enumerate(gorevler, 1):
        liste_kutusu.insert(tk.END, f"{i}. {gorev}")

def gorev_ekle():
    yeni_gorev = simpledialog.askstring("Görev Ekle", "Yeni görev:")
    if yeni_gorev and yeni_gorev.strip():
        gorevler.append(yeni_gorev.strip())
        gorevleri_kaydet()
        listeyi_guncelle()
    else:
        messagebox.showwarning("Uyarı", "Boş görev eklenemez.")

def gorev_sil():
    secili = liste_kutusu.curselection()
    if not secili:
        messagebox.showwarning("Uyarı", "Lütfen silinecek bir görev seçin.")
        return
    indeks = secili[0]
    silinen = gorevler.pop(indeks)
    gorevleri_kaydet()
    listeyi_guncelle()
    messagebox.showinfo("Bilgi", f"'{silinen}' silindi.")

def gorev_duzenle():
    secili = liste_kutusu.curselection()
    if not secili:
        messagebox.showwarning("Uyarı", "Lütfen düzenlenecek bir görev seçin.")
        return
    indeks = secili[0]
    mevcut_gorev = gorevler[indeks]
    yeni_gorev = simpledialog.askstring("Görev Düzenle", f"Yeni görev metni ({mevcut_gorev}):")
    if yeni_gorev and yeni_gorev.strip():
        gorevler[indeks] = yeni_gorev.strip()
        gorevleri_kaydet()
        listeyi_guncelle()
        messagebox.showinfo("Bilgi", "Görev güncellendi.")
    else:
        messagebox.showwarning("Uyarı", "Boş görev eklenemez.")

pencere = tk.Tk()
pencere.title("Görev Yönetim Uygulaması")
pencere.geometry("500x450")
pencere.config(bg="#ffe4f2")  # Pastel pembe arka plan

baslik = tk.Label(pencere, text="To-Do List Uygulaması", font=("Helvetica", 16, "bold"), bg="#ffe4f2", fg="#802bb1")
baslik.pack(pady=10)

liste_kutusu = tk.Listbox(pencere, font=("Helvetica", 12), width=45, height=10, bg="#f3e8ff", fg="#4a004e", selectbackground="#d7bce8")
liste_kutusu.pack(pady=5)

buton_cercevesi = tk.Frame(pencere, bg="#ffe4f2")
buton_cercevesi.pack(pady=10)

# Butonların ortak özellikleri
buton_renk_bg = "#ba68c8"  # Pastel mor
buton_renk_fg = "white"
buton_genislik = 25
buton_font = ("Helvetica", 10, "bold")

tk.Button(buton_cercevesi, text="Görev Ekle", command=gorev_ekle, width=buton_genislik,
          bg=buton_renk_bg, fg=buton_renk_fg, font=buton_font).pack(pady=3)
tk.Button(buton_cercevesi, text="Görev Sil", command=gorev_sil, width=buton_genislik,
          bg=buton_renk_bg, fg=buton_renk_fg, font=buton_font).pack(pady=3)
tk.Button(buton_cercevesi, text="Görev Düzenle", command=gorev_duzenle, width=buton_genislik,
          bg=buton_renk_bg, fg=buton_renk_fg, font=buton_font).pack(pady=3)
tk.Button(buton_cercevesi, text="Çıkış", command=pencere.quit, width=buton_genislik,
          bg=buton_renk_bg, fg=buton_renk_fg, font=buton_font).pack(pady=3)

gorevler = gorevleri_yukle()
listeyi_guncelle()

pencere.mainloop()
