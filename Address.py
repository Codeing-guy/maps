import webbrowser,sys,pyperclip

sys.argv #['mapit.py','ring','road','jalgaon']
if len(sys.argv) >1:
      #['mapit.py','ring','road','jalgaon']>> ['ring road jalgaon'   ]
      address=' '.join(sys.argv[1:])
      print(address)
else:
     address=pyperclip.paste()
        
#https://www.google.com/maps/place/<Address>
webbrowser.open('https://www.google.com/maps/place/'+ address)
