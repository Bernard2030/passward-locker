## Password-Locker
## Developer
## Bernard Opiyo
## Project Description
An application that manages user passwards and generates new ones and save them.
## Setup Requirements
* Github
* Code Editor of your choice
## Setup Installation
* Fork app from github
* Clone the app in your terminal using $git clone command
* Run the code in your code editor  using :
 * $ chmod +x run.py
 * $ ./run.py command
## BDD
 Behaviour        | Input          | Output |
| ------------- |:-------------:| -----:|
| col 3 is      | $ ./run.py	 | Welcome to passward-locker!! |
| select a short code to continue:     | ca      |   create account|
|login | li       |    login to a/c |
|                 |   ca            |  Get account enter your user name|
|                 |  ep             |  Enter passward|
|                  | gp           |generate random passward|
|saving user     |username, passward|Welcome your account is successfully created your passward is:|
|loging in     |    li  |  Enter your user name and passward to log in|
|success log in|  username | Hello welcome to passward locker|
|creating  a new credential|  cc|  create a new credential|
|           |            |  account name...|
|          |             |   Your account user name|
| if true   | ep  |enter your passward if you have an account|
|   else     |gp  |generate passward|
|save credential|account  |Account credential for account{} created successfully|
|displaying account|  dc|  Here is your list of accounts|
|find account| fc  | enter the account name you want tosearch|
|delete account|  d  | Enter the account name of the credential you want to delete|
|generate random passward|  gp  | has successfuly been generate
| exiting the application|  ex  | Thanks for using passward lock|


## Known Bugs
The application works perfectly well,there are no known bugs if you find any let me know.
## Technologies used
- Python3.9
## Contacts:
Email :brobernard.254@gmail.com
## LICENCE
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) [2021] [Bernard Opiyo]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
