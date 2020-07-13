import pysftp
from base64 import decodebytes
import paramiko

myHostname = "149.28.147.3"
myPort = 15
myUsername = "root"
myPassword = ""
myCnopts = pysftp.CnOpts(knownhosts='known_hosts')
myCnopts.hostkeys = None

#keydata = b"""AAAAB3NzaC1yc2EAAAADAQABAAABAQC7Ol+V2SMygAknXSx4/fPKmre0rwBXH3j44BGVlZeOVOzstY0LGO9NhjX5eB1y4H1fJZKyc2PyKEe6KC77NmfOewlfLSIJo6KzJ95JC6KE+8rWbJrbleU3Bv+3+Vh4hcmh3R3e3oQ61ufpjfaLI2cp9MHXstkI1KPWvvFzFXmkG30QQdwsrk3Tob2GsNyzycXcMg7IBJInpML25y3LhHBd8fP37Yy12x9hZg+tAwF+IIUH7Ka0ygCB+mAShBa0h1Ju7B//G18gkYBehUGZ1Th2HPBU+wDYXoQew2gTkgLxwklDAo1MJujSI1atn6NepalYVDshzTf+oHm7IiirspBz"""
#key = paramiko.RSAKey(data=decodebytes(keydata))
#myCnopts = pysftp.CnOpts()
#myCnopts.hostkeys.add('149.28.147.3', 'ssh-rsa', key)


with pysftp.Connection(
        host=myHostname,
        username=myUsername,
        password=myPassword,
        #private_key="id_rsa",
        port=myPort,
        cnopts=myCnopts) as sftp:

	print("Connection succesfully stablished ... ")

	# Switch to a remote directory
	sftp.cwd('/home/minh/public_html/koolwatch.me')

	# Obtain structure of the remote directory '/var/www/vhosts'
	directory_structure = sftp.listdir_attr()

	# Print data
	for attr in directory_structure:
		print(attr.filename, attr)
	
# connection closed automatically at the end of the with-block
