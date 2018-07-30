import cgi,os,cgitb,sys
cgitb.enable()

port='hey how have you been?'

def say(something):
    try:
        import subprocess#customizable voice quality voice,talk speed, pitch,volume
        voice1=subprocess.Popen(["espeak", "-v", 'en-us1',"-s",'175',"-p",'75',"-a",'80', something])
        #os.system('sudo espeak  "{0}"'.format(something))
    except Exception as e:
        print(e.message)

print(port)
say(port)

