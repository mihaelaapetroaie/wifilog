import subprocess
import datetime

def scan():
        run_scan=subprocess.Popen(["sudo", "iwlist", "wlan0", "scan"], stdout=subprocess.PIPE)
        output, err = run_scan.communicate()
        output=output.decode()
        index=output.find("\n")
        output=output[index+1:]
        return output

	

def is_start(line):
	return line.strip()[:4]=="Cell"
	

def nicer(lines):
	index=0
	devices=[]
	for i,line in enumerate(lines):
		if is_start(line):
			if i>=1:
				devices.append(lines[i-index:i])
			index=1
		else:
			index=index+1
	devices.append(lines[len(lines)-index:])
	return devices

a_log=[]
																	
while True:
	devices=scan()
	lines=devices.split("\n")
	devices=nicer(lines)
	for device in devices:
		a=device[0].strip().split()
		a=a[len(a)-1:]
		if a not in a_log:
			a_log.append(a)
			print ("\n".join(device))
			print()
		
