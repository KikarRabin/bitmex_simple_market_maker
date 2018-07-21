import subprocess
# Constants
XBt_TO_XBT = 100000000
VERSION = 'TEST-1.5'
try:
    VERSION = str(subprocess.check_output(["git", "describe", "--tags"]).rstrip())
except Exception as e:
    git not available, ignore
    pass
