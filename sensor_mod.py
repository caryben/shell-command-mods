# I wanted a continuous update on processor temp and fan speed and I knew about a terminal command called 'sensors'
# that gave one instance of cpu temp and fan speed, so I wrote a script that continuously calls the 'sensors' command 
# so that I get a terminal continuously updating information. 

# uses ~0.0% of the processor and 0.1% of memory so it can run silently in the background
import subprocess, time
subprocess.check_call(['echo', '-ne', '\e[8;15;60t'])
temp = "room temp = 21 C"
while(True):
	subprocess.check_call(['sensors'])
	time.sleep(0.1)
	subprocess.check_call(['clear'])
