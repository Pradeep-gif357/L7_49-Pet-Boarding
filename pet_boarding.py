import math


def parse_booking(text):
    try:
        if not isinstance(text, str):
            return ("Unknown", 0.0)

        parts = text.split(":")
        if len(parts) != 2:
            return ("Unknown", 0.0)

        pet, days = parts
        pet = pet.strip()

        if not pet:
            return ("Unknown", 0.0)

        days = float(days.strip())

        if not math.isfinite(days) or days < 0:
            return ("Unknown", 0.0)

        return pet.title(), days

    except (ValueError, TypeError):
        return ("Unknown", 0.0)


def stay_average(days_csv):
    try:
        if not isinstance(days_csv, str):
            return 0

        values = []

        for item in days_csv.split(","):
            item = item.strip()

            if item:
                try:
                    number = int(item)
                    if number >= 0:
                        values.append(number)
                except ValueError:
                    continue

        if not values:
            return 0

        return sum(values) // len(values)

    except (ValueError, TypeError):
        return 0


def payable_fee(text):
    try:
        if not isinstance(text, str):
            return 0.0

        parts = text.split("|")

        if len(parts) != 2:
            return 0.0

        fee = float(parts[0].strip())
        discount = float(parts[1].strip())

        if not math.isfinite(fee) or not math.isfinite(discount):
            return 0.0

        if fee < 0 or discount < 0:
            return 0.0

        total = fee * 1.18 - discount

        return max(total, 0.0)

    except (ValueError, TypeError):
        return 0.0


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter pet:days (e.g. dog:5): ")
    result = parse_booking(user_input)
    print("Pet and Days:", result)

    print("\n==== Running stay_average ====")
    user_input = input("Enter stay lengths in days as CSV (e.g. 2,5,7): ")
    result = stay_average(user_input)
    print("Average Stay:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 1500|100): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()
