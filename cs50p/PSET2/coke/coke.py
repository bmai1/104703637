def main():
    # price of coke
    amount = 50
    # loop until paid for
    while amount > 0:
        # get valid coin that is integer
        while True:
            try:
                coin = int(input("> "))
            except ValueError:
                continue
            if coin != 25 and coin != 10 and coin != 5:
                print(f"Amount due: {amount}")
            if coin == 25 or coin == 10 or coin == 5:
                break

        # print amount due or change owed
        amount -= coin
        if amount <= 0:
            print("Change owed: " + str(0 - amount))
            break
        print(f"Amount due: {amount}")


main()

