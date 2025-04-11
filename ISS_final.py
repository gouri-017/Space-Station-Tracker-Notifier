# Add your own email address to log in to your account create an app password if using two-factor authentication
mail1 = "your-email-address"
new_gmail_pass = 'your-app-password'
# Add the email Address you would want to send the Mail
mail2 = "destination-mail-address"

# Find your current Latitude and Longitude and fill these variable(remove string)
latitude = 'your place latitude in float'
longitude = 'your place longitude in float'


url = 'http://api.open-notify.org/iss-now.json'
import requests
from _datetime import datetime
import time
import smtplib



parameters = {
    'lat':latitude,
    'lng':longitude,
}

def send_mail():
    # location of our email providers smtp server
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=mail1, password=new_gmail_pass)
        connection.sendmail(from_addr=mail1, to_addrs=mail2,
                            msg=f"Subject:Look Up!!\n\n  Hey, ook up ath the sky!!"
                                f"Can you see it??;]")
def check_position():
    # diff_latitude = iss_latitude - latitude
    # diff_longitude = iss_longitude - longitude
    if now_time >= sunset or now_time <= sunrise:
        if  (latitude-5 <= iss_latitude <= latitude+5 and
             longitude-5 <= iss_longitude <= longitude+5):
            return True
        else:
            print('latitudes did not match')
            return False
    else:
        print('sunset did not match')
        return False

while True:
    time.sleep(60)
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    now_time = datetime.now().hour

    response = requests.get(url = 'https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0')
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    # send_mail() - to check if everything works fine
    if check_position():
        print('go out side')
        send_mail()

