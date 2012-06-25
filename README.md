# Sentiment Analysis

## Film Rating API

```python

api = API()

# Perform a generic search for a film. Returns JSON
print(api.search("Toy Story 3"))

# Get ratings for a given film id
result = api.get_ratings(770672122)
 
# Print out all the ratings for Toy Story 3
for res in result['reviews']:
    try:
        print("%s : %s " % (res['critic'], res['original_score']))
    except KeyError: pass
        
```

```python

# Get some basic data on Box office movies
# Format is [id, title, audience_score, critics_score]

api = API()

print(api.list_box_office())

# [['771218292', 'Snow White and the Huntsman', 59, 47], 
#  ['771041419', 'Men in Black III', 74, 69], 
#  ['770740154', "Marvel's The Avengers", 96, 93], 
#  ['770858174', 'Battleship', 57, 34], 
#  ['771219982', 'The Dictator', 56, 58],
#  ['771252912', 'The Best Exotic Marigold Hotel', 84, 77], 
#  ['771242835', "What to Expect When You're Expecting", 53, 22], 
#  ['770783545', 'Dark Shadows', 48, 40], 
#  ['771269700', 'Chernobyl Diaries', 31, 21], 
#  ['771272681', 'For Greater Glory', 85, 18]]

```
