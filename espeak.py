import cgi,os,cgitb,sys
cgitb.enable()

port='hey how have you been?'

def say(something):
    try:
        os.system('sudo espeak  "{0}"'.format(something))
    except Exception as e:
        print(e.message)

print(port)
say(port)

