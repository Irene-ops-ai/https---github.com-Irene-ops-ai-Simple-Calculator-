sterile_lab_equipment = {"Syringe", "Scisors", "Pipettes"}
sterile_er_equipment = {"Scalpel", "Stethoscope", "Sutures"}

contaminated = {"Defibrillator", "Sutures", "Scalpel"}

sterile_er_equipment -= contaminated
print(f"Sterile ER Equipment:", sterile_er_equipment)

#combine all sterile tools

all_sterile = sterile_lab_equipment | sterile_er_equipment

print("All Sterile:", all_sterile)


