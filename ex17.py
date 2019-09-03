from sys import argv
from os.path import exists

script,sfile,dfile = argv

print(f"Copying from {sfile} to {dfile}")
sofile = open(sfile)
srfile = sofile.read()
print(srfile)

print(f"the input file is {len(srfile)} bytes long")

print(f"Does the output file exists? {exists(dfile)}")
print(f"Hit ENTER to continue or CTRL_C to quit file transfer")
input()

dofile = open(dfile,'w')
drfile = dofile.write(srfile)

print("File transfer complete")

sofile.close()
dofile.close()