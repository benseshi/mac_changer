import subprocess
import optparse

def get_arguments():
	parser=optparse.OptionParser()
	parser.add_option('-i','--interface',dest="interface",help="select interface to mac_address")
	parser.add_option('-m','--mac',dest="new_mac",help="select to destination mac address")
	return parser.parse_args()
def change_mac(interface,new_mac):
	print('[+] changing mac address from '+interface+'to mac address'+new_mac)
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])

(options,arguments)=get_arguments()
change_mac(options.interface,options.new_mac)


