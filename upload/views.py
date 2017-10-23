from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import dropbox
from dropbox import files
import os
from fileupl.settings import MEDIA_ROOT

DROP_BOX_TOKEN = 'j18KPM4-3RAAAAAAAAAACGmBAasG7AI-9X5SFctd_BQ5y8oUzQXyKvJMwqqRVK4V'


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        # upload script #
        dbx = dropbox.Dropbox(DROP_BOX_TOKEN)
        file_tobe_up = (os.path.join(MEDIA_ROOT, filename))
        with open(file_tobe_up, 'rb+') as f:
            data = f.read()
        dbx.files_upload(data, path='/{}'.format(filename), mode=files.WriteMode.add)
        # upload script #

        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'simple_upload.html')
