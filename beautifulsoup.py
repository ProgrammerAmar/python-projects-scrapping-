from bs4 import BeautifulSoup


SIMPLE_HTML = """

	<html>
		<head>
			<title>
				You made for large bro
			</title>
		</head>
		<body>
			<p> You made for large </p>
			<p> Bro you are going to make that </p>
			<h1>Time back </h1>
		</body>
	</html>
"""

simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')

data = simple_soup.find_all('p')
for friend in data:
	print(friend.string)
