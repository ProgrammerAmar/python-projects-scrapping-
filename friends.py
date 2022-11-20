

friends = input("Enter three friends name separated by commas (no space,please): ").split(',')

people_file = open('people.txt','r')

people_data = [data.strip() for data in people_file.readlines()]
people_file.close()

print(people_data)

friends_set = set(friends)
people_set = set(people_data)

nearby_me = friends_set.intersection(people_set)

nearby_me_file = open('nearby_friends.txt','w')

for friend in nearby_me:
	print(f'{friend} is nearby you')
	nearby_me_file.write(f'{friend}\n')

nearby_me_file.close()
