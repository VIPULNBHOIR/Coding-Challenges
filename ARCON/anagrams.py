def Anagrams(array: list[str]):

    for i in range(0, len(array) - 1):
        strign1 = array[i]
        for j in range(i+1, len(array) ):
            string2 = array[j]
            list_strign1 = list(strign1)
            list_string2 = list(string2)
            if ''.join(sorted(list_strign1)) == ''.join(sorted(list_string2)):
                print(strign1, ' anagram to ' ,string2)
                break

    

Anagrams(['TOP','STOP', 'POST', 'REST', 'SERT', 'POT'])