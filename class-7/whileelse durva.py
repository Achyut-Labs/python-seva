petStore = [
    {'pet': 'dog', 'qty': 10},
    {'pet': 'cat', 'qty': 5},
    {'pet': 'bird', 'qty': 3}
]

pet = input('Enter a pet:')

index = 0

while index < len(petStore):
    item = petStore[index]
    # check the pet name
    if item['pet'] == pet:
        print(f"The petStore has {item['qty']} {item['pet']}(s)")
        found_it = True
        break

    index += 1
else:
    qty = int(input(f'Enter the qty for {pet}:'))
    petStore.append({'fruit': pet, 'qty': qty})
    print(petStore)
 