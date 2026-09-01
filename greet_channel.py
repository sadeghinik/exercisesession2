def main():
    first_name = input("نام: ")
    last_name = input("نام خانوادگی: ")
    national_code = input("کد ملی: ")

    if not first_name or not last_name or not national_code:
        print("لطفاً همه ورودی‌ها (نام، نام خانوادگی و کد ملی) را وارد کنید.")
        return

    print(
        f"{first_name} {last_name} ({national_code})"
    )


if __name__ == "__main__":
    main()
