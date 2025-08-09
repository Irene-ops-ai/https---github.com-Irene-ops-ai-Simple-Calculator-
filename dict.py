staff = {
         
       101:{"name": "Dr. Mary", "role": "neuro", "Station": "ER"},
       102:{"name": "Dr. Sharn", "role": "physio", "station": "ICU"}
       
         


}

patient = {
            "P1": {"name": "John", "allergy": "smoke", "ward": "ICU"},
            "P2": {"name": "Sally", "allergy": "eggs", "ward": "Ward 4A"}
}

patient["P3"] = {"name": "Dee", "allergy": "protein", "ward": "ward 3B"}

#print("Patient name:", patient["P2"]["name"]["ward"])

print("Patient allergy:", patient["P3"]["allergy"])