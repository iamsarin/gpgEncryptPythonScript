# Encrypt Python Script By Sarin Kesphanich http://sarin.me
import os, shutil
source_path = os.path.abspath("Source")
encrypted_path = os.path.abspath("Encrypted")
path_gpg = "C:\Program Files (x86)\GNU\GnuPG\pub"
os.chdir(path_gpg)
pass_phase = "1q2w3e4r"

for file in os.listdir(source_path):
    gpg_cmd = "gpg --yes --batch -a --passphrase=" + pass_phase + " -c " + source_path + "\\" + file
    os.system(gpg_cmd)
    shutil.move(source_path + "\\" + file + ".asc", encrypted_path + "\\" + file + ".asc")
