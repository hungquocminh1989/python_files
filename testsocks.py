from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    ('149.28.147.3', 15),
    ssh_username="root",
    ssh_password="pA3?%tjGHy7ttUnj",
    remote_bind_address=('149.28.147.3', 8080),
    local_bind_address=('127.0.0.1', 1080)
)

server.start()

print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

#server.stop()
