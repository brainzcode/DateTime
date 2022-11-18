import datetime as dat
import yagmail, random


my_email = "testpythonmailer1@gmail.com"
password = "foanjireptgrxvox"

now = dat.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quotes = random.choice(all_quotes)

    print(quotes)

    try:
        # initializing the server connection
        yag = yagmail.SMTP(user=my_email, password=password)
        # sending the email
        yag.send(to='testpythonmailer2@yahoo.com',
                 subject='Monday Motivation',
                 contents=f"<h1>{quotes}</h1>"
                                                                                       'worked!</h1> '
                                                                                       '<p>Just Running multiple tests</p>')
        print("Email sent successfully")
    except:
        print("Error, email was not sent")