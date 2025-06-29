from printer import print_status, print_all_contact

def add_contact(contacts: list[dict]):
    first_name = input("first name: ")
    last_name = input("last name: ")
    phone = input("phone: ")
    group = input("group (family, friend, work, other): ")

    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "group": group,
    })

    print_status('success')

def show_all_contact(contacts: list[dict]):

    if contacts:
        print_all_contact(contacts)
    else:
        print_status('error')

def search_contact(contacts: list[dict]):
    query = input("Qidiriladigan so‘zni kiriting (ism, familiya, telefon yoki guruh): ").lower()
    found = False
    for contact in contacts:
        if (
            query in contact['first_name'].lower() or
            query in contact['last_name'].lower() or
            query in contact['phone'] or
            query in contact['group'].lower()
            ):
            print(f"{contact['first_name'].title()} {contact['last_name'].title()} | {contact['phone']} | {contact['group'].title()}")
            found = True


def delete_contact(contacts: list[dict]):
    query = input("O‘chirmoqchi bo‘lgan kontakt ismini yoki telefon raqamini kiriting: ").lower()
    for contact in contacts:
        if (
            query in contact['first_name'].lower() or
            query in contact['last_name'].lower() or
            query in contact['phone'] or
            query in contact['group'].lower()
            ):
            print(f"Topildi: {contact['first_name']} {contact['last_name']} |{contact['phoone']}| {contact['group']}")
            confirm = input("Haqiqattan ham bu kontaktni o'chirmoqchimisiz? ha/yuq ").lower()
            if confirm == 'ha':
                contacts.remove(contact)
                print("Kontact muvaffaqiyatli o'chirildi")
            else:
                print("O'chirish bekor qilindi!")
                break
        else:
            print("Hech qanday Kontact topilmadi!")

                


def update_contact(contacts: list[dict]):
    query = input("Qidiriladigan so‘zni kiriting (ism, familiya, telefon yoki guruh): ").lower()
    found = False

    for contact in contacts:
        if (
            query in contact["first_name"].lower()
            or query in contact["last_name"].lower()
            or query in contact["phone"]
            or query in contact["group"].lower()
        ):
            found = True
            print(
                f'{contact["first_name"].title()} {contact["last_name"].title()} '
                f'| {contact["phone"]} | {contact["group"].title()}'
            )

            confirm = input("Ushbu kontaktni yangilashni istaysizmi? (ha/yo‘q): ").strip().lower()
            if confirm == "ha":
                new_name = input("Yangi ism (o‘zgartirmaslik uchun Enter bosing): ").strip()
                new_surname = input("Yangi familiya (o‘zgartirmaslik uchun Enter bosing): ").strip()
                new_phone = input("Yangi telefon (o‘zgartirmaslik uchun Enter bosing): ").strip()
                new_group = input("Yangi guruh (o‘zgartirmaslik uchun Enter bosing): ").strip()

                if new_name:
                    contact["first_name"] = new_name
                if new_surname:
                    contact["last_name"] = new_surname
                if new_phone:
                    contact["phone"] = new_phone
                if new_group:
                    contact["group"] = new_group

                print("Kontakt yangilandi.\n")

    if not found:
        print("Mos keluvchi kontakt topilmadi.")

