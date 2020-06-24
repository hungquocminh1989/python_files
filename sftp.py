import pysftp

myHostname = "149.28.147.3"
myPort = 15
myUsername = "root"
myPassword = ""
myCnopts = pysftp.CnOpts()
#myCnopts.hostkeys = None

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, private_key="c:\\private_key.pem", private_key_pass="123456", port=myPort, cnopts=myCnopts) as sftp:
	print("Connection succesfully stablished ... ")

	# Switch to a remote directory
	sftp.cwd('/home/minh/public_html/koolwatch.me')

	# Obtain structure of the remote directory '/var/www/vhosts'
	directory_structure = sftp.listdir_attr()

	# Print data
	for attr in directory_structure:
		print(attr.filename, attr)
	
# connection closed automatically at the end of the with-block
