import re
import sys


def main():
    thistime = input("Hours:\n")
    print(convert(thistime))


def convert(s):
    start, end = s.split(" to ")
    match = re.match(r"(\d+):(\d+)\s+(AM|PM)", start)

    starthours, startminutes, startperiod = map(int, match.groups())


    if startperiod == PM:
        starthours = starthours + 12

    match = re.match(r"(\d+):(\d+)\s+(AM|PM)", end)

    endhours, endminutes, endperiod = map(int, match.groups())


    if endperiod == PM:
        endhours = endhours + 12

    return f"{starthours:02}:{startminutes:02} to {endhours:02}:{endminutes:02}"


main()
