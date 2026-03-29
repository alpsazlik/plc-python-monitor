import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import warnings


warnings.filterwarnings("ignore", category=UserWarning)


fig, ax = plt.subplots(figsize=(10, 6))
x_verisi = []
y_verisi = []


KRITIK_SICAKLIK = 24.5


def veri_cek_simulasyon():

    return round(random.uniform(20.0, 25.5), 2)


def grafik_guncelle(i):
    yeni_deger = veri_cek_simulasyon()

    x_verisi.append(i)
    y_verisi.append(yeni_deger)

    if len(x_verisi) > 20:
        x_verisi.pop(0)
        y_verisi.pop(0)

    ax.clear()


    ax.axhline(y=KRITIK_SICAKLIK, color='red', linestyle='--', linewidth=1.5, alpha=0.7)


    ax.plot(x_verisi, y_verisi, color='#1f77b4', marker='o', linewidth=2, markersize=6)


    if yeni_deger >= KRITIK_SICAKLIK:

        ax.plot(x_verisi[-1], yeni_deger, color='red', marker='o', markersize=12)
        ax.text(x_verisi[-1], yeni_deger + 0.4, f'⚠️ ALARM: {yeni_deger}',
                verticalalignment='bottom', horizontalalignment='center',
                fontweight='bold', color='red', fontsize=12)
    else:
        ax.text(x_verisi[-1], yeni_deger + 0.3, f'{yeni_deger}',
                verticalalignment='bottom', horizontalalignment='center',
                fontweight='bold', color='green', fontsize=10)

    ax.set_title("Advance Industrial Solutions - Akıllı Anomali Tespiti ve İzleme", fontsize=14, fontweight='bold')
    ax.set_ylabel("Sıcaklık Değeri (°C)", fontsize=12)
    ax.set_xlabel("Zaman (Okuma Sayısı)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)

    ax.set_ylim(15, 30)


ani = animation.FuncAnimation(fig, grafik_guncelle, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()