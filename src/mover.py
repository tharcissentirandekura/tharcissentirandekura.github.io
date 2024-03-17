import os
import subprocess
import shutil

files = os.listdir()
folders = "/Users/tntirand/Desktop/portfolio/src/"
for file in files:
    if file.endswith(".html"):
        subprocess.run(["mv",file,folders + 'templates/'])
    elif file.endswith(".css"):
        subprocess.run(["mv",file,folders + 'static/'])
    elif file.endswith(".js" or "pdf"):
        subprocess.run(["mv",file,folders + 'estate/'])
    elif file.endswith(".png" or "jpeg"):
        subprocess.run(["mv",file,folders + 'static/'])
    else:
        subprocess.run(["mv",file,folders])