from mastodon import Mastodon
from datetime import datetime

startTime = datetime.now().replace(month=1, day=1)
endTime = datetime.now().replace(month=12, day=31)

rest = endTime - datetime.now()
total = endTime - startTime
percentage = round((1 - rest.total_seconds()/total.total_seconds()) * 100)

if percentage == 100:
	print("100% triggered");
	currentDay = int(datetime.now().strftime("%d"))
	currentMonth = int(datetime.now().strftime("%m"))
	print("Current day: ", str(currentDay))
	print("Current month: ", str(currentMonth))

	if currentDay != 31 or currentMonth != 12:
		print("It is not the last day of the year! Bye")
		quit()

#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://voi.social/'
)

f = open("currentPercentage.txt", "r")
currentPercentage = f.readline(2);

print("Saved percentage: ", currentPercentage)
print("Current percentage: ", str(percentage))

iCurrentPercentage = int(currentPercentage)

if iCurrentPercentage != percentage:
	print("New percentage found!")
	#mastodon.status_post()

	percentageToShow = round(percentage / 10);

	toPostMessage = ""

	for x in range(percentageToShow * 2):
		toPostMessage = toPostMessage + "▓";

	for x in range(percentageToShow * 2, 10*2):
		toPostMessage = toPostMessage + "░"

	toPostMessage = toPostMessage + " [" + str(percentage) + "%]"

	print(toPostMessage)

	mastodon.status_post(toPostMessage)

	print("Saving current percentage");
	f = open("currentPercentage.txt", "w")
	f.write(str(percentage))
	f.close()
	print("Saving new percentage...");


else:
	print("Got nothing to do!");

print ("Good bye")
