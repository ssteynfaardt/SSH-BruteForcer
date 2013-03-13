# SSH BruteForcer

Python based SSH BruteForcer, works with a dictionary list, supports multiple connections. Writes all successful usernames & passwords found to a text file.

### Useage 

	> ./bruteForcer.py -h
	usage: bruteForcer.py [-h] [-d DICTIONARY] [-s HOST] [-p PORT] [-t TIMEOUT]
	                      [-c CONNECTIONS] [-o OUTPUT]

	SSH Brute forcer

	optional arguments:
	  -h, --help            show this help message and exit
	  -d DICTIONARY, --dictionary DICTIONARY
	                        path to dictionary file, should be in "user pass"
	                        format
	  -s HOST, --source HOST
	                        Host to scan, default localhost
	  -p PORT, --port PORT  Port to connect to, default 22
	  -t TIMEOUT, --timeout TIMEOUT
	                        Timeout in seconds, default 30 seconds
	  -c CONNECTIONS, --connections CONNECTIONS
	                        Concurrent connections, default 5
	  -o OUTPUT, --output OUTPUT
	                        Output file name, where passwords found gets saved
	                        
### Example

	./bruteForcer.py -s "localhost" -d /path/to/cictionary/file

	[+] Bruteforcing against localhost with dictionary /path/to/cictionary/file
	[-] user pass fail!
	[-] test test fail!
	[-] user1 pass1 fail!
	[!] admin admin is CORRECT!
	[-] admin pass fail!




### DISCLAIMER:

This program is for educational use only.
Don't use it to crack a real server. You could get
into a lot of trouble. This is just a simple demo
to show how to use telnetlib in combination with files.
Use it at your own risk!

### License
MIT-License:

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
