states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New york': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'Fl': 'Jacksonville',
    'NY': 'New York',
    'OR': 'Portland'
}

for state, abbrev in list(states.items()):
    print(f"{state} has abbreviation {abbrev}")
    print(f"and has city {cities[abbrev]}")
