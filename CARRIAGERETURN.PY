import time
clear ="\033[2J"
clear_and_return="\033[H"
def alram(seconds):
  time_elapsed=0
  print(clear)
  while time_elapsed < seconds:
    time.sleep(1)
    time_elapsed+=1
    
    time_left=seconds-time_elapsed
    minutes_left=time_left//60
    seconds_left=time_left%60
    
    print(f"{minutes_left:02d}{seconds_left:02d}\033[H")
user_input=int(input(" \033[0;31mEnter the time of the elasped of the alarm please"))
alram(user_input)    