import time
from plyer import notification

if __name__ == "__main__": 
    while True:
        notification.notify(
            title = "Please Drink Water Now!!",
            message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 3.7 litres of fluids for men and about 2.7 litres of fluids a day for women.",
            #app_icon = "icon.ico",
            timeout = 10
        )
        time.sleep(60*60)