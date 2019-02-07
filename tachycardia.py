def is_tachycardic(str_in):

    str_in = str_in.lower()

    word = -1
    word = str_in.find('tachycardic')

    if(word >= 0):
        return True
    else:
        return False

def user_input():
    str_in = input('Enter the word: ')
    return str_in

if __name__ == "__main__":
    str_in = user_input()
    if(is_tachycardic(str_in)):
        print('True!')
    else:
        print('False!')
