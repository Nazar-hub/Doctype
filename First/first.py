enter = ""
list_a = []
while enter != "exit":
    enter = str(input("choose 1 or 2"))
    alphabet = "ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopstvxyz" \
            "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхчшщьюя"
    if enter.upper() == "1" or enter.upper() == "1":
        a = input().split()
         for i in a:
             if (i not in list_a) and len(i) > 2:
                 list_a.append(i)
         list_a.sort()
         for x in range (0,len(list_a)):
             print(list_a[x])
         print("")
    elif enter.upper() == "2" or enter.upper() == "2":
        a = input().split()
        for x in range(len(alphabet)):
            number = 0
            for i in a:
                number = number + i.count(alphabet[x])
            if number > 0:
                print(alphabet[x] + " - " + str(number))
            print("")


