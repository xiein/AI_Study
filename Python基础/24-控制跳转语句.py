for i in range(1, 11):  # i的值 1 - 10
    if i % 3 == 0:
        continue
    print(f'Hello World! {i}')

print('-' * 28)

for i in range(1, 11):  # i的值 1 - 10
    if i % 3 == 0:
        break
    print(f'Hello World! {i}')