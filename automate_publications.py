import os
import shutil
import re

os.chdir('/Users/michaelosborne/Documents/WWW/MosbWWW/robots-www/')

publication_types = [
    'Journal'
    # ,
    # 'Conference',
    # 'Preprints',
    # 'Reports',
    # 'Workshop',
    # 'Theses'
]

# Compile regex we'll use over and over below
regex = re.compile(r"(?<=file = {).*?(files/)", re.IGNORECASE)

for publication_type in publication_types:
    publication_bib = publication_type + '.bib'
    shutil.copyfile(
        '_bibliography/' + publication_type + '/' + publication_bib,
        '_bibliography/' + publication_bib
    )

    # Read in the file
    filedata = None
    with open(publication_bib, 'r') as file :
      filedata = file.read()

    # Remove unnecessary':application/pdf'
    filedata = filedata.replace(':application/pdf', '')

    # Tidy up file paths : edit file links to eg {162/1403.4640.pdf}
    for line in filedata:
        line = regex.sub("", line)

    # Write the file out again
    with open(publication_bib, 'w') as file:
      file.write(filedata)

    # shutil.copytree( -r _bibliography/Osborne/files/ public/pdf

#  _bibliography/osborne.bib
# rm -rf ./_bibliography/Osborne
# chmod -R a+rx ./public/pdf
# jekyll build
# rsync -avz /Users/michaelosborne/Documents/WWW/MosbWWW/robots-www/_site/ mosb@robots.ox.ac.uk:~/WWW