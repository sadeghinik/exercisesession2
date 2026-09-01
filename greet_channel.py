def main():
    first_name = input("اسم را وارد کنید: ").strip()
    last_name = input("فامیل را وارد کنید: ").strip()

    if not first_name or not last_name:
        print("لطفاً اسم و فامیل را کامل وارد کنید.")
        return

    print(f"به کانال ما خوش آمدید، {first_name} {last_name}. چطور میتونم کمکتون کنم؟")


if __name__ == "__main__":
    main()
