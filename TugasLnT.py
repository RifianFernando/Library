import sys
import os

def cls():
    print("press any key to continue")
    c = sys.stdin.read(1)
    os.system('CLS')

listbook =[]
idbook=[]
i=0
a =0

while True:
    print("WELCOME TO THE LIBRARY\n")
    print("1. Check books\n")
    print("2. Add book\n")
    print("3. Delete books\n")
    print("4. Search book\n")
    print("5. EXIT\n")
    pilihan = input("Masukkan pilihan: ")
    if(pilihan == "1"):
        if(len(listbook)==0):
            print("\n")
            print("No books in the library")
        else:
            print("list books:")
            for i in range (len(listbook)):
                print("%d. Title: %s id: %s" % (i+1, listbook[i],idbook[i]))
        print("\n")
        cls()
    elif(pilihan == "2"):
        namabook =input("Masukkan judul buku: ")
        id = input("Masukkan id buku: ")
        valid = True
        for i in range (len(listbook)):
            if(namabook == listbook[i] or id == idbook[i]):
                valid = False
                print("Book already exist")
        if (valid == True):
                listbook.append(namabook)
                idbook.append(id)
                print("\n")
                print("Book added\n")
        cls()           
    elif(pilihan == "3"):
        destroy = input("Masukkan judul atau id buku yang ingin dihapus: ")
        yn = input("are u sure?(y/n): ")
        if(yn == "y"):
            for i in range (len(listbook)):
                print(listbook[i])
                if(destroy == listbook[i] or destroy == idbook[i]):
                    #a-=1
                    del listbook[i]
                    del idbook[i]
        elif(yn == "n"):
            print("Canceled")
            cls()
        else:
            print("Invalid input\n")
            cls()
        os.system('CLS')
    elif(pilihan == "4"):
        search = input("Masukkan judul atau id buku yang ingin dicari: ")
        valid = False
        for i in range (len(listbook)):
            if(search == listbook[i] or search == idbook[i]):
                print("Title: %s id: %s\n" % ( listbook[i],idbook[i]))
                print("Book Found\n")
                valid = True
        if(valid == False):
            print("Book not found\n")
        cls()
    elif(pilihan == "5"):
        print("Terimakasih telah menggunakan library ini\n")
        cls()
        sys.exit()
    else:
        print("silahkan input angka yang tersedia\n")
        cls()
print("\nThank you for using our library")