# Dasar Python
# 1. Sequential (berurutan)
print('hello dunia :)')
print('on alvif@kawaii')
print('pada 18 Maret 2021')
print('-' * 10)

# 2. Percabangan: Eksekusi terpilih
ingin_cepat = True
if ingin_cepat:
    print('jalan lurus :v')
else:
    print('another way :3')

# 3. Perulangan
jumlah_anak = 4 # tipe data skalar (sederhana)
for index_anak in range(1, jumlah_anak+1):
    print(f'Halo anak #{index_anak}')

# 4. List
anak = ['Alvif', 'Sandana', 'Mahardika', 'Kawaii']
print(anak)
anak.append('Neko-chan')
print(anak)
## ambil list data berdasarkan index
print('\nambil list data berdasarkan index')
print(f'Hai {anak[1]}')

## ambil semua list data
print('\nambil semua list data')
for a in anak:
    print(f'Hai {a}')

print('\nambil semua list data: index')
for a in range(0, len(anak)):
    print(f'Hai {anak[a]}')
