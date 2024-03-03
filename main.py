import time
import webbrowser
import schedule

# Songs on sharing

def open_link(link):
    webbrowser.open(link)

def meeting():
    print("Meeting Launching...!");
    open_link('https://us06web.zoom.us/j/8208844066?pwd=RAWyXJVxqb7TV15CCe8paaUmyb3j9s.1')

[schedule.every().day.at("17:50").do(meeting) for _ in range(1, 7)]


# Second meeting
def meeting2():
    print("Batch 1 Launching...!");
    open_link('https://us06web.zoom.us/j/8208844066?pwd=RAWyXJVxqb7TV15CCe8paaUmyb3j9s.1')

[schedule.every().day.at("05:20").do(meeting2) for _ in range(1, 7)]




while True:
    print('Waiting For Meetings...')
    schedule.run_pending()
    time.sleep(1)
