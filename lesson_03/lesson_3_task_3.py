from address import Address
from mailing import Mailing


from_addr = Address("123456", "Москва", "Ленина", "10", "5")
to_addr = Address("654321", "Самара", "Буянова", "14", "57")

mail = Mailing(to_address=to_addr, from_address=from_addr, cost=7, track=20262027)
print(f"Отправление {mail.track} из {mail.from_address} в {mail.to_address}. Стоимость {mail.cost} рублей")