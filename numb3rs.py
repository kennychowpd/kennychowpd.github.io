def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    check_ip = ip.split(".")
    for i in check_ip:
        try:
            i = int(i)
            if 0 > i or i > 255:
                return False
        except ValueError:
            return False
    return True

if __name__ == "__main__":
    main()
