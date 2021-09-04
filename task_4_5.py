from task_4_3 import currency_rates as cr


def main(argv):
    program, *args = argv  # через терминал работает
    cr(*args)

    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
