def main():
    camelCase = input("> ")
    if camelCase.islower():
        print(camelCase)
        exit()
    # check for uppercase letter
    for i in range(len(camelCase)):
        if (camelCase[i]).isupper() == True:
            # swap to snake_case
            camelCase = camelCase.replace(camelCase[i], "_" + camelCase[i].lower())
    print(camelCase)


main()