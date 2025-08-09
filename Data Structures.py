# List Data Structures
#Example here is a list of beds in a hospital ward 4A

ward_4a = ["Bed1: Titus", "Bed2: Maria", "Bed3: Johnson"]
#print(ward_4a)

#Admission for patients, Ruby and Dorea

ward_4a.append("Bed4:Ruby")
#print("Ward 4A", ward_4a)

ward_4a.append("Bed5: Dorea")
#print("Ward 4A", ward_4a)

#Discharging of patients

discharged = ward_4a.pop(2)
#print("Ward 4A", ward_4a)
print(f" {discharged} -> Remaining {ward_4a}")