import subprocess
import sys
import setup_util
import os

def start(args):
  if os.name != 'nt':
    return 1
  
  try:
    setup_util.replace_text("nancy/src/Web.config", "localhost", args.database_host)
    subprocess.check_call("powershell -File setup_iis.ps1 start", cwd="nancy")
    return 0
  except subprocess.CalledProcessError:
    return 1

def stop():
  if os.name != 'nt':
    return 0
  
  subprocess.Popen("powershell -File setup_iis.ps1 stop", cwd="nancy")
  return 0