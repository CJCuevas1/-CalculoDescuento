# Creación de la función para utilizarse en los próximos bloques.
def calcular_descuento(precio, descuento=10):
    monto_descuento = precio * (descuento / 100)
    precio_final = precio - monto_descuento
    return monto_descuento, precio_final


# Listado de los autos con sus precios
autos = {
    "1": {"modelo": "Toyota Corolla", "precio": 24500},
    "2": {"modelo": "Hyundai Tucson", "precio": 29500},
    "3": {"modelo": "Ford Mustang Mach-E", "precio": 48995},
    "4": {"modelo": "Volkswagen Tiguan", "precio": 31995},
    "5": {"modelo": "Chevrolet Onix", "precio": 16500}
}

# Bloque que se imprime en pantalla con la elección del auto haciendo uso de un fstring
print("-------------------------------------")
print("🚗✨ CONCESIONARIA 'FAST CARS' ✨🚗")
print("-------------------------------------")
print("🔢 MODELOS DISPONIBLES:")
for clave, auto in autos.items():
    print(f"   {clave}. {auto['modelo']}: 💵 ${auto['precio']:,.2f}")

# Elección del usuario ante un carro en específico según el número dado
opcion = input("\n👉 ¿Qué auto deseas? (1-5): ")
while opcion not in autos.keys():
    opcion = input("⚠️ Elegiste un número no válido. Ingresa un número del 1 al 5: ")

auto_elegido = autos[opcion]

#  Primera llamada a la función que toma en cuenta solo el 10% predeterminado
descuento1, precio_final1 = calcular_descuento(auto_elegido["precio"])  # 10%
print("\n📋💡 OPCIÓN ESTÁNDAR 💡📋")
print(f"   🚘 Auto: {auto_elegido['modelo']}")
print(f"   💲 Precio original: ${auto_elegido['precio']:,.2f}")
print(f"   🔻 Descuento (10%): ${descuento1:,.2f}")
print(f"   ✅ Total a pagar: ${precio_final1:,.2f}")

# Segunda llamada a la función que hace uso del 15% de descuento a modo de promoción
descuento2, precio_final2 = calcular_descuento(auto_elegido["precio"], 15)  # 15%
print("\n🎊🔥 OPCIÓN PROMOCIONAL 🔥🎊")
print(f"   🚘 Auto: {auto_elegido['modelo']}")
print(f"   💲 Precio original: ${auto_elegido['precio']:,.2f}")
print(f"   🔻 Descuento (15%): ${descuento2:,.2f}")
print(f"   ✅ Total a pagar: ${precio_final2:,.2f}")
print("\n💬 ¡Gracias por tu compra! Vuelve pronto. 😊")