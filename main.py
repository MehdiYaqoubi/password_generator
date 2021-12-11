import string
import argparse

from random import choices


def create_password(
        length=8, upper=False, lower=False, digit=False, punctuation=False
):
    pool = ''
    if upper:
        pool += string.ascii_uppercase

    if lower:
        pool += string.ascii_lowercase

    if digit:
        pool += string.digits

    if punctuation:
        pool += string.punctuation

    if pool == '':
        pool = string.ascii_letters

    return ''.join(choices(pool, k=length))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="password creator")
    parser.add_argument(
        'length', type=int, help="Length of password(default 8 character)"
    )
    parser.add_argument(
        '-u', '--upper', help="Use uppercase characters", action='store_true'
    )
    parser.add_argument(
        '-l', '--lower', help="Use lowercase characters", action='store_true'
    )
    parser.add_argument(
        '-d', '--digit', help="Use digit characters", action='store_true'
    )
    parser.add_argument(
        '-p', '--punctuation', help="use punctuation characters",
        action='store_true'
    )

    args = parser.parse_args()
    print(create_password(
        args.length, args.upper, args.lower, args.digit, args.punctuation
    ))
