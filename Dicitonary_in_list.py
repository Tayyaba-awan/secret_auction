# Dicitonary in list excersie
travel_log=[
{
   "country":"France",
   "visited":12,
   "cities":["Paris","lille","dijon"]
},
{
    "country":"Germany",
    "visited":12,
    "cities":["Berlin","Humburg","Stuttgrat"]
},
]
def add_new_country(country,visited,cities):
    new_country={"country":country,"visited":visited,"cities":cities}
    travel_log.append(new_country)
add_new_country(country="Russia",visited=2,cities=["Moscow","Saint Petersburg"])
print(travel_log)