#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anlamsız Hayat Tavsiyesi Jeneratörü
Gerçekten çalışır, gerçekten anlamsız.
"""

import random

tavsiyeler = [
    "Sabahları kahve yerine hava iç, daha hafif.",
    "Ayakkabılarını ters giy, dünyayı farklı gör.",
    "Her gün bir şeye 'hayır' de, sonra 'evet' de, sonra unut.",
    "Duvara bak ve 'neden?' diye sor, cevap gelmezse devam et.",
    "Saatin tersine yürü, zaman kazanırsın (kazanmazsın).",
    "Çoraplarını kaybet, özgürlük hissi yaşa.",
    "Bir taşa isim ver ve onunla konuş, kimse duymasın.",
    "Yemek yerken sayı say, ama yanlış say.",
    "Aynaya bak ve 'sen kimsin?' diye sor, cevap verme.",
    "Rüzgara karşı bağır, rüzgar da bağırsın.",
    "Kitap oku ama sayfaları karıştır, hikaye değişsin.",
    "Telefonunu kapat, sonra aç, sonra tekrar kapat. Özgürsün.",
    "Bir kuşu izle, o da seni izlesin, sonra ikiniz de unutun.",
    "Gökyüzüne tükür, yerçekimi seni affetsin.",
    "Hiçbir şey yapma, en iyi tavsiye bu."
]

# Gizli mesaj (ters çevrilmiş, sadece meraklılar için)
gizli = "isarkomed alzaf ahad"  # tersi: daha fazla demokrasi

def tavsiye_al():
    return random.choice(tavsiyeler)

if __name__ == "__main__":
    print("Anlamsız Hayat Tavsiyesi:")
    print(tavsiye_al())
    print("\nTekrar çalıştır, belki daha anlamsız olur.")
    # Gizli çıktı yok: print(gizli[::-1])  # yorumda kalsın, merak eden çözsün
