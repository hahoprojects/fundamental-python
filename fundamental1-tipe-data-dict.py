"""
Tipe data dictionary mirip seperti JSON
(menghubungkan KEY dan VALUE)
Key Value Pair
"""

kamus_id_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_id_eng)
print(kamus_id_eng['ibu'])
print(kamus_id_eng['ayah'])

print('\nData from server:')
data_from_server_gojek = {
    'tangal': '2021-03-18',
    'driver_list': [
        {'nama': 'John', 'jarak': 10},
        {'nama': 'Lennon', 'jarak': 40},
        {'nama': 'Pimpom', 'jarak': 60}
    ]
}
print(data_from_server_gojek)
print(f"Driver sekitar {data_from_server_gojek['driver_list']}")
print(f"Driver #1 {data_from_server_gojek['driver_list'][0]}")
print(f"Driver #2 {data_from_server_gojek['driver_list'][2]}")
print(f"Jarak Driver #1 : {data_from_server_gojek['driver_list'][0]['jarak']}")

