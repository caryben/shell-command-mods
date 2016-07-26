# uses ~0.0% of the processor and 0.1% of memory so it can run silently in the background ( ͡° ͜ʖ ͡°)
import subprocess, time
subprocess.check_call(['echo', '-ne', '\e[8;20;60t'])
while(True):
	subprocess.check_call(['sensors'])
	time.sleep(0.5)
