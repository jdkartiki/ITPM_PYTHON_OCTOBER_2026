# Library System using Datatypes

books=[]

while True:
    print("============ LIBRARY SYSTEM ==========")
    print("1. Add Books")
    print("2. Issue Books")
    print("3. Return Books")
    print("4. Available Books")
    print("5. Display All Books")
    print("6. Exit ")

    ch=input("Enter Choice from above options :: ")

    if ch=="1":
        bid=int(input("Enter Book ID :: "))
        bname=input("Enter Book NAme :: ")
        author=input("Enter Book Author :: ")

        book={
            "id":bid,
            "name":bname,
            "author":author,
            "issued":False
        }

        books.append(book)
        print("Book Added Successfully ")

    elif ch=="2":
        bid=int(input("Enter Book ID :: "))
        found=False

        for b in books:
            if b["id"]==bid:
                found=True

                if b["issued"]:
                    print("Book is already Issued")
                else:
                    b["issued"]=True
                    print("Book Is Issued Successfully")
                    break

            if not found:
                print("Book Not Found")

    elif ch=="3": 
        bid=int(input("Enter Book ID :: "))
        found=False

        for b in books:
            if b["id"]==bid:
                found=True

                if not b["issued"]:
                    print("Book was not Issued")
                else:
                    b["issued"]=False
                    print("Book Returned Successfully")
                    break

            if not found:
                print("Book Not Found")

    elif ch=="4":
        print("====== AVAILABLE BOOKS =======")
        available=False

        for b in books:
            if not b["issued"]:
                print(f"ID :: {b["id"]}\t Name :: {b["name"]}\tAuthor ::{b["author"]} ")
                available=True

            if not available:
                print("Books not Available")
    elif ch=="5":
        print("==== BOOKS ====")

        if len(books)==0:
            print("No Books Found")
        else:
            for b in books:
                status="Issued" if b["issued"] else "Available"
                print(f"ID :: {b["id"]}\t Name :: {b["name"]}\tAuthor ::{b["author"]}\t Status:: {status} ")
    elif ch=="6":
        print("Thank You for Using Our Library")
        break
    else:
        print("Invalid choice")







