def main():
    list = {}
    while True:
        try:
            grocery = input().upper()
            # check if already there
            if grocery in list:
                list[grocery] += 1
            else:
                list[grocery] = 1
        # when press control-d
        except EOFError:
            # sort alphabetical order
            for grocery in sorted(list):
                print(list[grocery], grocery)
            exit()


main()