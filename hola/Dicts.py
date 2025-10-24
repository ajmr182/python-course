party_planning = {
    'Yes': 10,
    'No': 15,
    'Maybe': 30,
    'Location': 'Our Backyard',
    'Date': '2022/05/01'
}

print(party_planning["Location"])
party_planning['Location'] = "Mi casa"
party_planning["Regalo"] = "Dinero"


party_planning.pop("Regalo")
pop_item = party_planning.popitem()
print(pop_item)
print(party_planning)

for i in party_planning:
    print(party_planning[i])