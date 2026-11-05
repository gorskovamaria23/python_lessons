from smartphone import Smartphone
catalog = []
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79001112233"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79004445566"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79007778899"))
catalog.append(Smartphone("Google", "Pixel 8", "+79002223344"))
catalog.append(Smartphone("OnePlus", "12", "+79005556677"))
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")