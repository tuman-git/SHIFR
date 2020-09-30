def get_num_word(word):
    num_word = []
    for i in word:
        a = ord(i)
        num_word.append(a)
    return num_word
def creater_nuw_num(num_word):
    SHIFR = [ord('m'), ord('t'), ord('s')]
    new_num = []
    k = 0
    for i in num_word:
        i += SHIFR[k]
        k += 1
        new_num.append(i) 
    return new_num