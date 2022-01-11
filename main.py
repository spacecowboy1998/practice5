def sequence(number: int, iterator: int):
    while iterator != 0:
        iterator -= 1
        number = number ** 2 - 1
        sequence(number, iterator)
    return number


turn = int(input("მიმდევრობის მერამდენე რიცხვის ხილვა გსურთ : "))
print(sequence(2, turn-1))
