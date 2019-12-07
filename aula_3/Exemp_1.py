# Classes - Detalhes sobre contexto
# https://pastebin.com/uwB4gbuL

kind = "blank"

def test_kind():
    print("Test Kind:", kind)

class Dog:
    kind = 'canine'
#Definir todas as váriaveis e atributos da classe no init 
    def __init__(self, name):
        self.name = name

    def what_kind(self):
        print("Name:", self.name)
        print("Geral:", kind)
        print("Self:", self.kind)

# Testes...
d = Dog('Fido')
e = Dog('Buddy')

test_kind()
print('-' * 40)

Dog.kind = "Chitsu"
d.what_kind()
print('-' * 40)
e.what_kind()
print('-' * 40)

print(Dog)
print(Dog.what_kind)
print(e)
print(e.what_kind)