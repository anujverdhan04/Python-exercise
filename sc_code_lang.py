print("Secret Code Language")

def secret_code():
    print("Welcome")
    print("Enter the string you want to send secretly")
    sentence = input(" ")
    words = sentence.split()

    for word in words:
        re_word = word[::-1]
        coding = False

        if coding:
            r1 = "rfg"
            r2 = "gfr"
            if len(word) <= 1:
                print("Can't perform any operation on:", word)
            elif len(word) == 2:
                print(re_word)
            elif len(word) == 3:
                re_word = word[1:] + word[0]
                print(r1 + re_word + r2)
            elif len(word) >= 4:
                re_word = word[2:] + word[0] + word[1]
                print(r1 + re_word + r2)
            else:
                print("The string does not exist for this code language")
        else:
            if len(word) <= 1:
                print("Can't perform any operation on:", word)
            elif len(word) == 2:
                print(re_word)
            elif len(word) == 3:
                re_word = word[2] + word[0:2]
                print(re_word)
            elif len(word) >= 4:
                re_word = word[::-1]
                print(re_word)
            else:
                print("The string does not exist for this code language")

secret_code()
