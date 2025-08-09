#Here we want to stock a hospital pharmacy

medication_stock = []

medication_stock.append("Antibiotics")
medication_stock.append("Insulin")
medication_stock.append("Painkillers")

print("Pharmacy Stock:", medication_stock)

#for_in range(2):

dispensed = medication_stock.pop()

print(f"Dispensed:, {dispensed} Remaining -> {medication_stock} ")