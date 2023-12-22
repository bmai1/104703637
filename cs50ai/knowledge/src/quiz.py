from logic import *


harry = Symbol("harry")
hermione = Symbol("hermione")
ron = Symbol("ron")

logic = [
    Implication(hermione, harry),
    hermione,
    And(ron, Not(ron)),
    harry,
    Or(Not(harry), hermione),
    Or(ron, hermione)
]

print(model_check(logic[4], logic[5]))
print(model_check(logic[0], logic[1]))
print(model_check(logic[1], logic[4]))
print(model_check(logic[5], logic[2]))
print(model_check(logic[0], logic[3]))
print(model_check(logic[5], logic[1]))