unconfirmed_users = ['alice',
                    'paolo',
                    'francesco'
                    ]

confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying users: {current_users.title()}")
    confirmed_users.append(current_users)

print("\nThe following users have been confirmed")
for confirmed in confirmed_users:
    print(confirmed.title())