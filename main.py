shopping_list = []


def add_item(item):
    shopping_list.append(item)
    print(f"{item} به لیست خرید اضافه شد.")


def display_list():
    print("\nلیست خرید شما:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")

while True:
    print("\nلطفاً یکی از گزینه‌های زیر را انتخاب کنید:")
    print("1. اضافه کردن اقلام به لیست")
    print("2. نمایش لیست خرید")
    print("3. خروج")

    choice = input("انتخاب شما: ")

    if choice == '1':
        item = input("نام قلمی که می‌خواهید اضافه کنید: ")
        add_item(item)
    elif choice == '2':
        display_list()
    elif choice == '3':
        print("خروج از برنامه.")
        break
    else:
        print("گزینه نامعتبر است. لطفاً دوباره تلاش کنید.")
