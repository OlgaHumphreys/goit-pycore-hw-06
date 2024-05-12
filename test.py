from task import Phone, Name, Record, AddressBook

phone1=Phone('1234567890')
print(phone1.value)


record1 = Record('Bob')
record1.add_phone(new_phone='2345678109')
record1.add_phone('2456789012')
print(record1.phones)
record1.remove_phone('2456779012')
print(record1)
record1.edit_phone('2345678109', '1324354667')
print(record1)
phone_object = record1.find_phone('1324354667')
print(phone_object)
ab=AddressBook()
print(ab)
ab.add_record(record1)
print(ab)
print(ab.find('Bob'))
ab.delete('Bob')
print(ab)