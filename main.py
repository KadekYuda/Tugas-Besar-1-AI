from hillclimb import hillclimb
from simulated_annealing import simulated_annealing
from genetic import genetic_algorithm

print("Daftar algoritma yang akan digunakan:\n" + \
      "1. Hill Climbing\n" + \
      "2. Simulated Annealing\n" + \
      "3. Genetic Algorithm\n")
input_algorithm = int(input("Pilih Algoritma yang diinginkan: "))

while input_algorithm < 0 and input_algorithm > 3:
    print("Algoritma tidak ada dalam pilihan.")
    input_algorithm = input("Pilih Algoritma yang diinginkan: ")

input_file = input("Masukkan nama file input: ")
if input_algorithm == 1:
    hillclimb(input_file)
elif input_algorithm == 2:
    simulated_annealing(input_file)
elif input_algorithm == 3:
    init_pop = input("Masukkan jumlah Initial Population. Harus power of 2 (4096): ")
    epoch_length = input("Masukkan jumlah Epoch Length (1000): ")
    if init_pop == "" and epoch_length == "": 
        genetic_algorithm(input_file)
    else:
        if init_pop == "": genetic_algorithm(input_file, int(epoch_length)) 
        elif epoch_length == "": genetic_algorithm(input_file, int(init_pop))
        else: genetic_algorithm(input_file, int(init_pop), int(epoch_length))