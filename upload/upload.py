import dropbox
import sysaccess_token='j18KPM4-3RAAAAAAAAAACGmBAasG7AI-9X5SFctd_BQ5y8oUzQXyKvJMwqqRVK4V'
client = dropbox.client.DropboxClient(access_token)
f=open(sys.arg[1].'rb')
response=client.put_file('/media/'+argv[1],f)
print "uploaded",response