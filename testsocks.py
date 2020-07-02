import sshtunnel
import requests


server = sshtunnel.SSHTunnelForwarder(
    ('149.28.147.3', 15),
    ssh_username="root",
    ssh_password="pA3?%tjGHy7ttUnj",
    ssh_config_file="/etc/ssh/ssh_config",
    remote_bind_address=('149.28.147.3', 15),
    local_bind_address=('127.0.0.1', 1080),
    logger=sshtunnel.create_logger(loglevel=1),
    
)


server.start()

print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
proxies = {
  "http": "http://127.0.0.1:1080",
  "https": "https://127.0.0.1:1080",
}
#r = requests.get('https://www.google.com',proxies=proxies, headers=headers).content
#print(r)

#server.stop()

