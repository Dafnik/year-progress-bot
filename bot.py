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
        print("percentage saved");
        
        sSavedPfpFilename = open("currentPfp.txt", "r").readline(2);
        pfpFilename = "./hourglass";

        if percentage >= 0 and percentage < 33:
            pfpFilename += "-top";
        elif percentage >= 33 and percentage < 66:
            pfpFilename += "-split";
        elif percentage >= 66:
            pfpFilename += "-bottom";

        pfpFilename += ".png";

        print("Current pfp to set: ", pfpFilename)
        print("Saved pfp: ", sSavedPfpFilename)
        
        if sSavedPfpFilename != pfpFilename:
                print("New pfp path found!")
                # Open the image file and read its contents
                with open(pfpFilename, 'rb') as fr:
                    image_data = fr.read()

                mastodon.account_update_credentials(
                    avatar=image_data,avatar_mime_type='image/png'
                )
                
                print("Saving current pfp path...");
                pf = open("currentPfp.txt", "w")
                pf.write(pfpFilename)
                pf.close()
                print("pfp path saved");

        #print("Sending post uptime ping")
        #requests.get("https://url", data = {})

else:
        print("Got nothing to do!");

close()
