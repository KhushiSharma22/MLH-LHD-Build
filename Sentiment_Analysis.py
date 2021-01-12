from textblob import TextBlob

x = input("Hi! I recently gave a public session and found that were one of the attendees! How was the session for you? ")
y = TextBlob(x)
z = y.sentiment.polarity

if z<0:
    x1 = input("Oh okay! Would you like to give in more details about your experience in person!")
    y1 = TextBlob(x1)
    z1 = y1.sentiment.polarity

    if z1<0:
        print("No worries! Thanks for your reply!")
    elif z1==0:
        print("Thanks! Would love to know more!")
    elif z1>0 and z1<=1:
        print("Great! Thank you. We can connect over here!")

elif z==0:
    print("Oh I see! Thank you for attending! Would love to connect with you more")

elif z>0 and z<=1:
    print("Great! Thank you so much for your valuable words! See you soon :)")

    
