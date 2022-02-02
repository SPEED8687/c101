import dropbox
accessToken= 'sl.BBPD5b2VXnjqw2i5k5_VyDaP5bfAazvwaGFG4vcVXhp8BRuEpWTiueChDi0Lc8SKKwKtAdPJHzQbIkJIsRnfa1w-TT11tpvSRvtvYBsKRXZmx8hhAsrzbcy6jEXAoCPChBqqvWKkPpg'
dbx=dropbox.Dropbox(accessToken)
fileFrom='fcb pfp.jpg'
f=open(fileFrom,'rb')
fileTo='/Rivaan/fcb pfp.jpg'

dbx.files_upload(f.read(),fileTo)

