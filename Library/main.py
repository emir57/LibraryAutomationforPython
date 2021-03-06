import sqlite3
database= "librarySQL.db"
#Login Screen
def language():
    text = "Please Choose Language(Lütfen bir dil seçiniz)\n 1-English\n 2-Turkish"
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute("Select isOK from languageIsValid")
    languageIsValid = cur.fetchone()
    languageIsValid = languageIsValid[0]
    if languageIsValid == 0:
        print(text)
        numberlanguage = input()
        if (int(numberlanguage) > 0) and (int(numberlanguage) < 3):
            cur.execute("update languageIsValid set isOK=1 where id=1")
            cur.execute("update selectedLanguage set languageID="+numberlanguage+" Where id=1")
            con.commit()
        else:
            print("invalid transaction(geçersiz işlem)")    
    con.close()

def languageChange():
    text = "Please Choose Language(Lütfen bir dil seçiniz)\n 1-English\n 2-Turkish"
    print(text)
    con = sqlite3.connect(database)
    cur = con.cursor()
    numberlanguage = input()
    print(numberlanguage)
    if (int(numberlanguage) > 0) or (int(numberlanguage) < 3):
        cur.execute("update languageIsValid set isOK=1 where id=1")
        cur.execute("update selectedLanguage set languageID="+numberlanguage+" Where id=1")
        con.commit()
    else:
        print("invalid transaction(geçersiz işlem)")
    con.close()

def addingRecord(bookName,author,kind,translator):
    con = sqlite3.connect(database)
    cur = con.cursor()
    command = "insert into Records(id,bookName,author,kind,translator) values(null,'"+bookName+"','"+author+"','"+kind+"','"+translator+"')"
    cur.execute(command)
    con.commit()
    con.close()


def updateRecordBookName(id,bookName):
    con = sqlite3.connect(database)
    cur = con.cursor()

    command = "update Records Set bookName='"+bookName+"' Where id="+id
    cur.execute(command)
    con.commit()
    con.close()

def updateRecordAuthor(id,author):
    con = sqlite3.connect(database)
    cur = con.cursor()

    command = "update Records Set author='"+author+"' Where id="+id
    cur.execute(command)
    con.commit()
    con.close()

def updateRecordKind(id,kind):
    con = sqlite3.connect(database)
    cur = con.cursor()

    command = "update Records Set kind='"+kind+"' Where id="+id
    cur.execute(command)
    con.commit()
    con.close()

def updateRecordTranslator(id,translator):
    con = sqlite3.connect(database)
    cur = con.cursor()

    command = "update Records Set translator='"+translator+"' Where id="+id
    cur.execute(command)
    con.commit()
    con.close()

def listRecords():
    con = sqlite3.connect(database)
    cur = con.cursor()
    command = "Select * from Records"
    cur.execute(command)
    a = cur.fetchall()
    print(a)

def deleteRecords(id):
    con = sqlite3.connect(database)
    cur = con.cursor()

    command = "delete from Records Where id="+id
    cur.execute(command)
    con.commit()
    con.close()


#1 English
#2 Turkish
def numberlanguageGET():
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute("Select languageID from selectedLanguage")
    languageID = cur.fetchone()
    return languageID[0]

###################################################################
language()

###################################################################
#English
if(numberlanguageGET() == 1):
    mode = input("Please select the action you want to do\n1-Adding Records\n2-List Records\n3-Update Record\n4-Delete Recport\n5-Exit\n6-Change Language\n")
    if (int(mode) == 1):
        booknamE = input("Book Name: ")
        authoR = input("Author: ")
        kinD = input("Kind: ")
        translatoR = input("Translator: ")
        addingRecord(booknamE,authoR,kinD,translatoR)

    elif(int(mode) ==2):
        listRecords()
    
    elif(int(mode) == 3):
        listRecords()
        iD = input("The id of the book you want to update: ")
        column = input("#Which column do you want to update? 1.Book Name - 2.Author - 3.Kind - 4.Translator ")
        if int(column) ==1:
            booknamE = input("Book Name: ")
            updateRecordBookName(iD,booknamE)
        if int(column) ==2:
            authoR = input("Author: ")
            updateRecordAuthor(iD,authoR)
        if int(column) ==3:
            kinD = input("Kind: ")
            updateRecordKind(iD,kinD)
        if int(column) ==4:
            translatoR = input("Translator: ")
            updateRecordTranslator(iD,translatoR)
        
    elif(int(mode) == 4):
        listRecords()
        iD = input("The id of the book you want to delete")
        deleteRecords(iD)

    elif(int(mode) == 5):
        exit()

    elif(int(mode) == 6):
        languageChange()
        print("successful")

###################################################################
#Turkish
elif(numberlanguageGET() == 2):
    mode = input("Lütfen yapmak istediğiniz işlemi seçiniz\n1-Kayıt Ekle\n2-Kayıtları Listele\n3-Kayıt Güncelle\n4-Kayıt Sil\n5-Çıkış\n6-Dili Değiştir\n")
    if (int(mode) == 1):
        booknamE = input("Kitap Adı: ")
        authoR = input("Yazar: ")
        kinD = input("Tür: ")
        translatoR = input("Çevirmen: ")
        addingRecord(booknamE,authoR,kinD,translatoR)

    elif(int(mode) ==2):
        listRecords()
        
    
    elif(int(mode) == 3):
        listRecords()
        iD = input("Güncellemek istediğiniz kitabın ID'si: ")
        column = input("#Hangi Kolonu Güncellemek İstiyorsunuz? 1.Kitap Adı - 2.Yazar - 3.Tür - 4.Çevirmen ")
        if int(column) ==1:
            booknamE = input("Kitap Adı: ")
            updateRecordBookName(iD,booknamE)
        if int(column) ==2:
            authoR = input("Yazar: ")
            updateRecordAuthor(iD,authoR)
        if int(column) ==3:
            kinD = input("Tür: ")
            updateRecordKind(iD,kinD)
        if int(column) ==4:
            translatoR = input("Çevirmen: ")
            updateRecordTranslator(iD,translatoR)
        
    elif(int(mode) == 4):
        listRecords()
        iD = input("Silmek istediğiniz kitabın ID'si: ")
        deleteRecords(iD)

    elif(int(mode) == 5):
        exit()
    
    elif(int(mode)==6):
        languageChange()
        print("işlem başarılı")

