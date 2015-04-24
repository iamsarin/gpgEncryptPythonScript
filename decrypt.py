# Decrypt Python Script By Sarin Kesphanich http://sarin.me
import glob, os, shutil
decrypted_path = os.path.abspath("Decrypted")
encrypted_path = os.path.abspath("Encrypted")
path_gpg = "C:\Program Files (x86)\GNU\GnuPG\pub"
os.chdir(path_gpg)
pass_phase = "1q2w3e4r"

for file in os.listdir(encrypted_path):
    gpg_cmd = "gpg --yes --batch -a --passphrase=" + pass_phase + " " + encrypted_path + "\\" + file
    os.system(gpg_cmd)
    file_decrypted = os.path.splitext(file)[0]
    shutil.move(encrypted_path + "\\" + file_decrypted, decrypted_path + "\\" + file_decrypted)
