import subprocess
import datetime

def process_scan_output(output):
	output=output.decode()
	lines=output.split("\n")

	devices=[]
	i=0

 	# cut the scanning line
	lines=lines[1:]

	# process remaining lines, each containing device
	for line in lines:
		line=line.split("\t")
		devices.append(line[i+1:])
	return devices


def scan():
	run_scan=subprocess.Popen(["sudo", "iwlist", "wlan0", "scan"], stdout=subprocess.PIPE)
	output, err = run_scan.communicate()
	output=output.decode()
	index=output.find("\n")
	output=output[index+1:]
	return output

logged_devices = set()

while True:
	devices=scan()
	for device in devices:
		if device[0] not in logged_devices:
			logged_devices.add(device[0])
			info=scan()
			print(datetime.datetime.now())
			print (info)
			print()
																				

