import classes_risto as c

rist_italian = c.Restaurant('L'' Hostaria', 'Italian')
rist_italian.print_number_served()
rist_italian.update_number_served(5)
rist_italian.print_number_served()
rist_italian.update_number_served(2)
rist_italian.print_number_served()
rist_italian.increment_number_served(10)
rist_italian.print_number_served()
rist_italian.increment_number_served(-3)
rist_italian.print_number_served()