def seq(number: int, iterator: int):
    iterator -= 1
    if iterator != 0:
        number = number ** 2 - 1
        seq(number, iterator)
    else:
        print(number)
    return


turn = int(input("მიმდევრობის მერამდენე რიცხვის ხილვა გსურთ : "))
seq(2, turn)
