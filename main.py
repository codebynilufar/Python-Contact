from printer import print_menu
from contact import add_contact, show_all_contact, search_contact, delete_contact,update_contact
from sys import exit

def main():
    contacts: list[dict] = [
        {"first_name": 'ali', 'last_name': 'valiyev', 'phone': '3241234123', "group": 'other'}
    ]
    
    while True:
        print_menu()

        choice = input("Menu tanlang: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            print(contacts)  
            show_all_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        elif choice == '6':
            print("Dasturdan chiqilmoqda...")
            exit(0)
        else:
            print("Noto‘g‘ri tanlov! Iltimos menyudagi raqamlardan birini kiriting.")

            
if __name__ == "__main__":
    main()
