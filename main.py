import functions as f

if __name__ == "__main__":
    
    try:
        print("Welcome to the Travel Details Analysis App")
        
        while True:
            print("Pilih data yang ingin ditampilkan :")
            print("1 - Jumlah trip per destinasi")
            print("2 - Distribusi tipe akomodasi (Darat / Udara)")
            print("3 - Jumlah trip per bulan")
            print("4 - Asal negara turis")
            print("5 - Durasi perjalanan dan harga akomodasi berdasarkan tujuan")
            print("6 - Exit")
            choices = input("> ")
            if choices == "1":
                f.show_chart_1()
                pass
            elif choices == "2":
                f.show_chart_2()
                pass
            elif choices == "3":
                f.show_chart_3()
                pass
            elif choices == "4":
                f.show_chart_4()
                pass
            elif choices == "5":
                f.show_chart_5()
                pass
            elif choices == "6":
                print("Terima kasih telah menggunakan program ini")
                exit()
            else:
                print("Masukkan angka 1-6")
                pass
    except KeyboardInterrupt:
        print("Anda telah menekan CTRL+C. Program terhenti")
    except Exception as e:
        print("Kesalahan terjadi, pesan error : {}".format(e))