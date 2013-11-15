
"""
height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count # => 120
"""

# Rewrite the code above using map, reduce and filter

# Expected answer: 120

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_people = filter(lambda person: 'height' in person, people)
height_total = reduce(lambda a, x: a+x['height'], height_people, 0)
height_avg = height_total / len(height_people)

print height_avg
