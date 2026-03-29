from opcua import Client
from opcua import ua


def main():
    url = "opc.tcp://192.168.250.1:4840"
    print(f"[{url}] adresindeki PLC'ye bağlanılıyor, lütfen bekleyin...")

    client = Client(url)

    client.set_user("alp")
    client.set_password("12345678")

    try:

        client.connect()
        print("BAŞARILI: PLC'ye bağlandık!")

        node_id = "ns=4;s=Motor_Test"
        motor_butonu = client.get_node(node_id)

        ilk_durum = motor_butonu.get_value()
        print(f"Motor_Test butonunun İLK durumu: {ilk_durum}")

        print("Python'dan PLC'ye komut gidiyor: Motoru Çalıştır (True)...")
        motor_butonu.set_value(ua.Variant(True, ua.VariantType.Boolean))

        son_durum = motor_butonu.get_value()
        print(f"Motor_Test butonunun SON durumu: {son_durum}")
        print("\nİŞLEM TAMAM! Projenin en zor kısmı başarıldı, canavar yenildi.")

    except Exception as e:
        print(f"\nEyvah, bir hata oluştu: {e}")
    finally:
        try:
            client.disconnect()
        except:
            pass


if __name__ == "__main__":
    main()