# cleanup-download-folder

## Please open config.yml file and update with your information

folder paths that will be used to organize files
```
folder:
  download: 'c:\Users\silas\Downloads'
  music: 'c:\Users\silas\OneDrive\Music'
  document: 'c:\Users\silas\OneDrive\Documentos'
  image: 'c:\Users\silas\OneDrive\Imagens'
```


Mapper between extensions allowed and destination folder

TIP: if you don't put the extension here unknown file will be delete :D
```
extensions:
  image:
    - .jpg
    - .png
    - .jpeg
  document:
    - .pdf
    - .zip
    - .txt
    - .json
    - .xlsx
    - .xls
    - .doc
    - .docx
  music:
    - .mp3
```

When python installation was completed

* pip install -r .\requirements.txt
* py main.py