def main():

    # write your code below this line
    Year = int(input("Give a year:\n"))
    if (Year % 4 == 0):
        print("This year is a leap Year")
    else:
        print("This year is not a leap Year")


if __name__ == '__main__':
    main()
