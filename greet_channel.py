def main():
    first_name = input("نام را وارد کنید: ")
    last_name = input("نام خانوادگی را وارد کنید: ")
    national_code = input("کد ملی را وارد کنید: ")

    if not first_name or not last_name or not national_code:
        print("لطفاً همه اطلاعات (نام، نام خانوادگی، کد ملی) را وارد کنید.")
        return

    print(f"{first_name} {last_name} ({national_code})")


if __name__ == "__main__":
    main()
