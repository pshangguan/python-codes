import commands

host = "54.187.190.67"
comms = ["yum update -y","yum install httpd -y"]
comms = ["df -i"]

wf=open("output.txt","w")
for c in comms:
	x = "ssh ec2-user@" + host + " -i /Users/guest1/.ssh/MyEC2KeyPair.pem sudo " + c
	print(x)
	y = commands.getstatusoutput(x)
	print(y)
	wf.write(y)
wf.close()
