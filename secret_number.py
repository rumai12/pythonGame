def secret_number():

    secret_number = 13
    guess = 0
    guess_limit = 3

    while guess < guess_limit:
        User = int(input("Masukkan Angka : "))
        if int(User) == 13:
            print("Anda berhasil, tebakan anda benar")
            break
        else :
            print("Anda salah, coba lagi")
            guess = guess + 1
    else : 
        print ("Kesempatan Anda sudah habis")