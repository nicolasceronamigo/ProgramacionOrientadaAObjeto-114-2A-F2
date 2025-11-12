from clases.auto_electrico import AutoElectrico

auto1 = AutoElectrico(100)

print(auto1.get_bateria())

print(auto1.conducir(30))

print(auto1.get_bateria())

print(auto1.cargar(10))

print(auto1.get_bateria())

print(auto1.conducir(90))

print(auto1.get_bateria())