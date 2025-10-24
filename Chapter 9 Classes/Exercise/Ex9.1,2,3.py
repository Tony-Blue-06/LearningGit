import classes_risto as cr

rist_italian = cr.Restaurant('L'' Hostaria', 'Italian')

#rist_italian.describe_restaurant()
#rist_italian.open_restaurant()
rist_japanese = cr.Restaurant('Sushi Zen', 'Japanese')
rist_mexican = cr.Restaurant('El Camino', 'Mexican')
rist_indian = cr.Restaurant('Spice Route', 'Indian')

rist_japanese.describe_restaurant()
rist_mexican.describe_restaurant()
rist_indian.describe_restaurant()

user1 = cr.User('Alice', 'Smith')
user2 = cr.User('Bob', 'Johnson')
user3 = cr.User('Charlie', 'Williams')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
