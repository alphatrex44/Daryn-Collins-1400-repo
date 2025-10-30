from datetime import datetime, date, timedelta
import calendar
import os

def today(format: str) -> str:
    return datetime.today().strftime(format)

def days_plus_or_minus(given_date: date, days: int) -> date:
    return given_date + timedelta(days=days)

def date_diff(datetime1: datetime, datetime2: datetime, units: str) -> str:
    delta = abs(datetime2 - datetime1)
    seconds = delta.total_seconds()

    if units == 'seconds':
        value = int(seconds)
    elif units == 'minutes':
        value = int(seconds // 60)
    elif units == 'hours':
        value = int(seconds // 3600)
    elif units == 'days':
        value = delta.days
    elif units == 'months':
        value = int(seconds // (60 * 60 * 24 * 30.44))
    elif units == 'years':
        value = int(seconds // (60 * 60 * 24 * 365.25))
    else:
        raise ValueError("Unsupported unit. Choose from 'seconds', 'minutes', 'hours', 'days', 'months', 'years'.")
    return f"{value} {units}"

def day_of_week(my_date: date) -> str:
    return my_date.strftime("%A")

def leap_years_between(date1: date, date2: date) -> list:
    start_year = min(date1.year, date2.year) + 1
    end_year = max(date1.year, date2.year)
    return [year for year in range(start_year, end_year) if calendar.isleap(year)]

def num_of_special_days(date1: date, date2: date, day_of_week: str, day_of_month: int) -> list:
    start_date = min(date1, date2)
    end_date = max(date1, date2)
    weekday_map = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
        'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6
    }
    target_weekday = weekday_map.get(day_of_week)
    if target_weekday is None:
        raise ValueError("Invalid weekday name.")

    results = []
    year = start_date.year
    month = start_date.month

    while date(year, month, 1) <= end_date:
        try:
            candidate = date(year, month, day_of_month)
            if start_date <= candidate <= end_date and candidate.weekday() == target_weekday:
                results.append(candidate)
        except ValueError:
            pass
        month += 1
        if month > 12:
            month = 1
            year += 1
    return results

def translate_format(user_format: str) -> str: #you arent requiring this but i want it
    replacements = {
        'YYYY': '%Y',
        'YY': '%y',
        'MM': '%m',
        'DD': '%d',
    }
    for key, val in replacements.items():
        user_format = user_format.replace(key, val)
    return user_format

def parse_date(date_str: str) -> date:
    formats = ["%Y-%m-%d", "%Y/%m/%d", "%m-%d-%Y", "%m/%d/%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date format: '{date_str}'. Try YYYY-MM-DD, YYYY/MM/DD, MM-DD-YYYY, or MM/DD/YYYY.")

def parse_datetime(datetime_str: str) -> datetime:
    formats = ["%Y-%m-%dT%H:%M", "%Y/%m/%dT%H:%M", "%m-%d-%Y %H:%M", "%m/%d/%Y %H:%M"]
    for fmt in formats:
        try:
            return datetime.strptime(datetime_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Invalid datetime format: '{datetime_str}'. Try YYYY-MM-DDTHH:MM or MM/DD/YYYY HH:MM.")

def main():
    print("this is a date calculator thingy")
    log = []

    while True:
        prompt = (
            "Enter operation (1–6) and required input, or press Enter to quit:\n"
            "1: Get today's date in a custom format.\n"
            "   Input: format string (e.g. MM/DD/YYYY, DD-MM-YYYY, YYYY/MM/DD)\n"
            "2: Add or subtract days from a given date.\n"
            "   Input: date and number of days (e.g. 10/30/2025 5)\n"
            "3: Calculate the difference between two datetimes in a specific unit.\n"
            "   Input: datetime1 and datetime2 and unit (e.g. 10/30/2025 08:00 10/30/2025 10:00 hours)\n"
            "4: Get the day of the week for a given date.\n"
            "   Input: date (e.g. 10/30/2025)\n"
            "5: List all leap years between two dates.\n"
            "   Input: date1 and date2 (e.g. 01/01/2020 01/01/2030)\n"
            "6: Find all dates between two dates that fall on a specific weekday and day of the month.\n"
            "   Input: date1, date2, weekday name, and day of month (e.g. 01/01/2020 01/01/2030 Monday 15)"
        )

        answerforthing = input(prompt + "\n")
        if answerforthing.strip() == "":
            break

        log.append(f"> {answerforthing}")
        parts = answerforthing.strip().split()

        try:
            op = int(parts[0])
            if op == 1:
                format_str = translate_format(" ".join(parts[1:]))
                result = today(format_str)

            elif op == 2:
                given_date = parse_date(parts[1])
                days = int(parts[2])
                result = days_plus_or_minus(given_date, days)

            elif op == 3:
                dt1 = parse_datetime(parts[1] + " " + parts[2])
                dt2 = parse_datetime(parts[3] + " " + parts[4])
                units = parts[5]
                result = date_diff(dt1, dt2, units)

            elif op == 4:
                d = parse_date(parts[1])
                result = day_of_week(d)

            elif op == 5:
                d1 = parse_date(parts[1])
                d2 = parse_date(parts[2])
                result = leap_years_between(d1, d2)

            elif op == 6:
                d1 = parse_date(parts[1])
                d2 = parse_date(parts[2])
                weekday = parts[3]
                day_of_month = int(parts[4])
                result = num_of_special_days(d1, d2, weekday, day_of_month)

            else:
                result = "Invalid operation number. Choose between 1 and 6."

        except ValueError as ve:
            result = f"Error: {ve}\nAccepted formats: YYYY-MM-DD, YYYY/MM/DD, MM-DD-YYYY, MM/DD/YYYY for dates; add time for datetimes."
        except Exception as e:
            result = f"Unexpected error: {e}"

        print(result)
        log.append(str(result))

    os.makedirs("text_files", exist_ok=True)
    with open("text_files/date_calculator_logs.txt", "w") as f:
        for entry in log:
            f.write(entry + "\n")

    print("\nLog saved to text_files/date_calculator_logs.txt. Goodbye!")


if __name__ == "__main__":
    main()
