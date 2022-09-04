import re


def main():
    print(search(input("Hours: ")))


def search(s):
    if matches := re.search(
        r"^(\d{1,2}(?::\d{2})? [AP]M) to (\d{1,2}(?::\d{2})? [AP]M)$", s, re.IGNORECASE):
        # 9 AM to 5 PM|9:00 AM to 5:00 PM
        time1 = matches.group(1).split(" ")
        time2 = matches.group(2).split(" ")
        # (['10:30', 'AM'], ['1:15', 'PM'])
    else:
        raise ValueError
    return " to ".join([convert(time1), convert(time2)])


def convert(s):
    time_digit = [*s[0]]
    if ":" in time_digit:
        time_digit.remove(":")
        hour = "".join(time_digit[:-2])
        minute = "".join(time_digit[-2:])
        hour = int(hour)
    else:
        hour = int("".join(time_digit))
        minute = "00"
    if int(hour) > 12 or int(minute) >= 60:
         raise ValueError
    else:
        if s[1] == "PM":
            hour += 12
        if hour < 10:
            hour = f"0{hour}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()