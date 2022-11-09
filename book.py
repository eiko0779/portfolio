# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.

# This program is distributed in the hopes that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.
# 675 Mass Ave, Cambridge, MA 02139, USA.

import os
import time
import csv
import platform

#CSVファイルを読み込みbooksに格納します。
#booksはグルーバル変数（リスト）として使用されます。
filename = "books.csv"
#filename = os.path.abspath(".") + "/book/books.csv" # For VScode
with open(filename, encoding='utf-8') as f:
    books = list(csv.reader(f))

#file_err = open('book.log', 'w')
#ユーティリティ関数を定義します。
#  get_return(): "Press return "を表示して「Enter」キーの入力を待ちます。
#  get_confirm(): "Are you sure? "を表示して y,yes,Y,YESの入力を待ちます。
#  clear_screen(): ターミナル画面を消去します。
def get_return():
    return input("Press return ")

def get_confirm():

    while True:
        x = input("Are you sure? ")
        if x in ['y','yes','Y','Yes','YES']:
            return True

        if x in ['n','no', 'N', 'No', 'NO']:
            print("Cancelled")
            return False

        print("Please enter yes or no ", end="")
        time.sleep(1)

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')    # Windows
    else:
        os.system('clear') # Linux or Mac

#新しい書籍の登録をします。
#  ID: 任意の整数を入力します。
#  Title: 書籍のタイトルを入力します。
#  Price: 書籍の価格を入力します
#  Memo: 書籍に関するメモを入力します。
def add_book():
    print("add_book")
    b_list = [b[0] for b in books]

    while True:
        id = input("Enter ID:")
        if id in b_list:
            print("ERROR!! ID:? already exists")
        else:
            title = input("Enter title:")
            price = input("Enter price:")
            memo = input("Enter memo:")
            abook = [id, title, price, memo]
            print()
            print("About to add new book")
            print("-" * 8)
            print("ID:\t",abook[0])
            print("Title:\t",abook[1])
            print("Price:\t",abook[2])
            print("Memo:\t",abook[3])
            print("-" * 8)
            break

    ans = get_confirm()

    if ans is True:
        print("Entry added")
        books.append(abook)

    get_return()

#
#書籍の一覧を表示します。
#書籍が無い場合は There in no book と表示します。
def list_book():
    if len(books) == 0:
        print("There is no book.")

    else:
        print()
        print("{:^4} {:^6} {}".format("ID","Price","Title"))
        print("-"*26)
        for book in books:
            print("{:>4} {:>6,d} {}".format(book[0],int(book[2]),book[1]))
        print()
    get_return()

#
#指定されたIDの書籍を削除します。
#  Enter ID to remove: 削除する書籍のIDを入力します。
#  IDに一致した書籍のデータを表示して get_confirm()関数で確認して削除します。
#  指定したIDの書籍がデータベース内に存在しないときは There is no book と表示します。
def remove_book():
    print("remove_book")
    b_list = [b[0] for b in books]
    while True:
        id = input("Enter ID to remove:")
        if id not in b_list:
            print("ERROR!! ID:{} is none".format(id))
        else:
            rbook = [b for b in books if b[0] == id][0]
            print("You are about to remove")
            print("-" * 8)
            print("ID:\t",rbook[0])
            print("Title:\t",rbook[1])
            print("Price:\t",rbook[2])
            print("Memo:\t",rbook[3])
            print("-" * 8)
            break 
    
    ans = get_confirm()

    if ans is True:
        print("Entry removed")
        books.remove(rbook)

    get_return()

#指定されたIDの書籍を更新します。
#  Enter ID to update: 更新する書籍のIDを入力します。
#  IDに一致した書籍のデータを表示して get_confirm()関数で確認します。
#  get_confirm()の戻り値がTureの場合書籍の更新をします。
#    ID: 任意の整数を入力します。
#    Title: 書籍のタイトルを入力します。
#    Price: 書籍の価格を入力します
#    Memo: 書籍に関するメモを入力します。
#  指定したIDの書籍がデータベース内に存在しないときは There is no book と表示します。
def update_book():
    print("update_book")
    id = input("Enter ID to update: ")
    if len([b for b in books if b[0] == id]) != 0:
        ubook = [b for b in books if b[0] == id][0]
        print()
        print("You are about to updata")
        print("--------")
        print("ID: ",ubook[0])
        print("Title: ",ubook[1])
        print("Price: ",ubook[2])
        print("Memo: ",ubook[3])
        print("--------")
    else:
        print("There is no book")

    if get_confirm():
        books.remove(ubook)
        nt = input("Enter new title: ")
        np = input("Enter new price: ")
        nm = input("Entre new memo: ")
        books.append([id,nt,np,nm])
        print("Entry added")

    get_return()
#
#書籍のデータを表示します。
def show_book():
    print("show_book")
    id = input("Enter ID: ")

    if len([b for b in books if b[0] == id]) != 0:
        sbook = [b for b in books if b[0] == id][0]
        print()
        print("--------")
        print("ID: ",sbook[0])
        print("Title: ",sbook[1])
        print("Price: ",sbook[2])
        print("Memo: ",sbook[3])
        print("--------")
    else:
        print("There is no book")

    get_return()
#
#メニュー選択
#  main()から呼び出され選択メニューを表示し入力待ちをします。
#  入力選択されたメニュー(a～s,q)を呼び出し元のmain()関数に戻します。
def set_menu_choice() :

    clear_screen()

    print("Options :-")
    print()
    print( "   a) Add new book")
    print( "   l) List book")
    print( "   r) Remove book")
    print( "   u) Update book")
    print( "   s) Show book")

    print( "   q) Quit")
    print()
    ret = input("Please enter choice then press return: ")
    return ret
#
#書籍データの保存
#  Save changes? の入力戻り値が y,yes,Y,Yes ならば booksをファイルに保存します。
#  入力が n,no,N,Noの場合はbooksを保存せずに Changes discarded を表示して終了します。
#  入力が上記以外の場合は、input y or n　を表示して再度入力待ちになります。
def save_changes():
    while True:
        x = input("Save changes? ")
        if x in ['y','yes', 'Y','Yes']:

            with open(filename, 'w', encoding='utf-8') as fp:
                writer = csv.writer(fp, lineterminator='\n')
                writer.writerows(books)

            print("Changes saved")
            time.sleep(1)
            return

        elif x in ['n','no','N','No']:
            print("Changes discarded")
            time.sleep(1)
            return
        else:
            print("input y or n", end="")
            time.sleep(1)

#
#main() メイン関数
#  cleara_screen() 関数でターミナル画面の文字を消去します。
#  set_menu_choice() 関数でメニュー選択入力を待ちます。
#  メニュー選択された(a～s)に対応した処理関数を呼び出します。
#  q が選択されると save_changes()関数を呼び出して処理を終了します。
def main():

    clear_screen()
    print()
    print()
    print("Mini Book manager")
    time.sleep(1)

    quit='n'
    while quit != "y":

        ret = set_menu_choice()
        if ret == "a":
            add_book()
        elif ret == "r":
            remove_book()
        elif ret == "u":
            update_book()
        elif ret == "l":
            list_book()
        elif ret == "s":
            show_book()

        elif ret == "q" or ret == "Q":
            save_changes()
            quit="y"
        else:
            print("Sorry, choice not recognized")
            time.sleep(1)

# Tidy up and leave
if __name__ == "__main__":
    main()
