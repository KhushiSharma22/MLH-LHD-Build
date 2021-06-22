from win10toast import ToastNotifier
notification = ToastNotifier()

resolutions = [
    ["Focus on personal branding!"],
    ["Expand your network professionally!!"],
    ["Develop the habit of meditation!"],
    ["Learn and grow!"],
    ["Grow EQUICODE!!!!"]
]

for quote in resolutions:
    notification.show_toast(quote[0], quote[1], duration = 10)
