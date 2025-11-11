from clases.auto_electrico import AutoElectrico

auto1 = AutoElectrico(100)

print(auto1.get_bateria())

auto1.conducir(30)

print(auto1.get_bateria())

auto1.cargar(50)

print(auto1.get_bateria())
