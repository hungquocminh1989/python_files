import sshtunnel
import requests

tunnels  = [
    ('149.28.147.3', 80),
    ('149.28.147.3', 443),
]
localPorts  = [
    ('127.0.0.1', 1080),
    ('127.0.0.1', 1081),
]

server = sshtunnel.SSHTunnelForwarder(
    ('149.28.147.3', 15),
    ssh_username="root",
    ssh_password="pA3?%tjGHy7ttUnj",
    #ssh_config_file="/etc/ssh/ssh_config",
    remote_bind_addresses=tunnels ,
    local_bind_addresses=localPorts ,
    logger=sshtunnel.create_logger(loglevel=1),
)


server.start()

#print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
proxies = {
    'http': "socks5://127.0.0.1:1080",
    'https': "socks5://127.0.0.1:1081"
}
r = requests.get('https://api.ipify.org/',proxies=proxies, headers=headers).content
print(r)

server.stop()

