import csv
import random

plate_numbers = [''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + ''.join(random.choices('0123456789', k=3)) + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) for _ in range(100)]
car_models = ['Toyota','Tesla' ,'Fiat' ,'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes-Benz', 'Audi']
energies = ['electric', 'thermal']

with open('/Users/roben/Desktop/Hackaton/github/AI/plate_model_gen.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Plate Number', 'Car Company Model', 'Energy']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for plate_number in plate_numbers:
        writer.writerow({'Plate Number': plate_number, 'Car Company Model': random.choice(car_models), 'Energy': random.choice(energies)})
