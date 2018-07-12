# counties to abbreviation
counties = {
    'Bihor': 'BH',
    'Brasov': 'BV',
    'Prahova': 'PH',
    'Sibiu': 'SB',
    'Constanta': 'CT'
}

# capitals
cities = {
    'BH': 'Bihor',
    'BV': 'Brasov',
    'PH': 'Ploiesti',
    'SB': 'Sibiu',
    'CT': 'Constanta'
}

for county, abbrev in list(counties.items()):
    print(f"{county} county is abbreviated {abbrev}")
    print(f"and has capital {cities[abbrev]}")