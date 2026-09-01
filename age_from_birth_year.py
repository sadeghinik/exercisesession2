def main():
    year_str = input("سال تولد را وارد کنید (مثلا 1370): ").strip()

    try:
        birth_year = int(year_str)
    except ValueError:
        print("ورودی نامعتبر است. لطفاً یک عدد وارد کنید.")
        return

    # سال جاری را از سیستم می‌گیریم
    from datetime import datetime
    current_year = datetime.now().year

    age = current_year - birth_year
    if age < 0:
        print("به نظر می‌رسد سال تولد نمی‌تواند در آینده باشد.")
        return

    print(f"سن شما: {age} سال")


if __name__ == "__main__":
    main()
