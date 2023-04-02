from mastodon import Mastodon
from datetime import datetime
# Only need for uptime monitoring
#import requests

def close():
        #print("Sending run uptime ping")
        #requests.get("https://url", data = {})
        print("Good bye")
        quit()

startTime = datetime.now().replace(month=1, day=1)
endTime = datetime.now().replace(month=12, day=31)

rest = endTime - datetime.now()
total = endTime - startTime
percentage = round((1 - rest.total_seconds()/total.total_seconds()) * 100)
sPercentage = str(percentage)

currentDay = int(datetime.now().strftime("%d"))
currentMonth = int(datetime.now().strftime("%m"))

sSavedPercentage = open("currentPercentage.txt", "r").readline(2);
savedPercentage = int(sSavedPercentage)

print("Current day: ", str(currentDay))
print("Current month: ", str(currentMonth))
print("Saved percentage: ", sSavedPercentage)
print("Current percentage: ", sPercentage)


if percentage == 100:
        print("100% case triggered, checking if its the last day of the year");
        if currentDay != 31 or currentMonth != 12:
                print("It is not the last day of the year! Bye")
                close()
                

#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = "https://mastodon.instance"
)

if savedPercentage != percentage:
        print("New percentage found!")

        percentageToShow = round(percentage / 100 * 20);

        toPostMessage = ""

        for x in range(percentageToShow):
                toPostMessage = toPostMessage + "▓";

        for x in range(percentageToShow, 20):
                toPostMessage = toPostMessage + "░"

        toPostMessage = toPostMessage + " [" + sPercentage + "%]"

        print("Message:")
        print(toPostMessage)

        mastodon.status_post(toPostMessage)
        print("Status sent!")

        print("Saving current percentage...");
        f = open("currentPercentage.txt", "w")
        f.write(sPercentage)
        f.close()
        print("Saved");
        
        
        pfpFilename = "./hourglass";
        
        # trying to update pfp
        if percentageToShow >= 0 & percentageToShow < 25:
                pfpFilename += "-top";
        elif percentageToShow >= 25 & percentageToShow < 50:
                pfpFilename += "-split";
        elif percentageToShow >= 50 & percentageToShow < 75:
                pfpFilename += "-bottom";
        
        pfpFilename += ".webp";

        # Open the image file and read its contents
        with open(pfpFilename, 'rb') as f:
            image_data = f.read()

        # Upload the image to Mastodon and get its ID
        media = mastodon.media_post(image_data, 'image/png')
        image_id = media['id']

        # Update the user's profile picture using the image ID
        mastodon.account_update_credentials(
            avatar=image_id
        )

        #print("Sending post uptime ping")
        #requests.get("https://url", data = {})

else:
        print("Got nothing to do!");

close()
