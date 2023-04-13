import functions as f

if __name__ == "__main__":
    
    # try:
        print("Menu Analisis Data Wisatawan")
        
        while True:
            print("Pilih data yang ingin ditampilkan :")
            print("1 - Jumlah Trip per Destinasi")
            print("2 - Distribusi Tipe Akomodasi")
            print("3 - Jumlah Trip per Bulan/Tahun")
            print("4 - Asal Negara Wisatawan")
            print("5 - Durasi Perjalanan dan Harga Akomodasi Berdasarkan Tujuan")
            print("6 - Data Wisatawan Berdasarkan Jenis Kelamin")
            print("7 - Keluar")
            choices = input("> ")
            
            if choices == "1":
                f.show_chart_1()
                
            elif choices == "2":
                f.show_chart_2()
                
            elif choices == "3":
                f.show_chart_3()
            
            elif choices == "4":
                f.show_chart_4()
            
            elif choices == "5":
                f.show_chart_5()
            
            elif choices == "6":
                f.show_chart_6()
            
            elif choices == "7":
                print("Terima kasih telah menggunakan program ini")
                exit()
            else:
                print("Masukkan angka 1-7")
            
    # except KeyboardInterrupt:
    #     print("Anda telah menekan CTRL+C. Program terhenti")
    # except Exception as e:
    #     print("Kesalahan terjadi, pesan error : {}".format(e))