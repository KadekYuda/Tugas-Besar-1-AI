from hillclimb import hillclimb
from simulated_annealing import simulated_annealing
from genetic import genetic

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
    # isi sama GA
    print("In progress...")
