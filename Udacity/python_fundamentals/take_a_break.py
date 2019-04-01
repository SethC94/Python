import time
import webbrowser
total_breaks = 3
break_count = 0

print ("Progaram started on:"+time.ctime())
while (break_count < total_breaks):
    time.sleep(1)
    webbrowser.open("https://music.youtube.com/watch?v=FGBhQbmPwH8&feature=share")
    break_count = break_count + 1
print "Loops have finished"
