import matplotlib.pyplot as plt

dataset_filename = "DS8.txt"

points = []
with open(dataset_filename, 'r') as file:  #читаємо дані з файлу
    for line in file:
        x, y = map(int, line.split())
        points.append((x, y))

plt.figure(figsize=(9.6, 5.4)) #розмір вікна

for point in points:
    plt.plot(point[0], point[1], 'bo')  #'bo' - сині точки

#Виведення результату в форматі PNG
output_filename = "output.png"
plt.savefig(output_filename)
plt.show()
