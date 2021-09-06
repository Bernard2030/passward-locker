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

* Behaviour	* Input	* Output
Run the application in the terminal of your code editor	$ ./run.py	Welcome to passward-locker!!
select a short code to continue: ca - create a/c, li - login to a/c, 
input ca	Get Account, enter your user name enter your email.
ep - enter passward, gp - generate random passward
enter passward
invalid try again
welcome your account is successfully created! Your passward is:
 enter your user name and your passward
 Hello{user_name}welcome to passward-locker
 Use these short codes:
 cc create a new credential
 fc find credential
 dc display credential
 gp generate random passward
 d delete credential
 ex Exit the application

Create new Credential
account name
your account user name
ep enter passward if already have an account
gp generate random passward
invalid passward try again
account credential for: {account} username {user_name} passward {passward} created succesfully

short_code dc
here is your list of accounts
Account {account.account}, username {user_name}, passward {passward}
You dont have any credentials...
enter account name you want to search...
account name, username, passward
Credential does not exist
Enter the account name of the credential you want to delete
your  credential for: successfully deleted!!!
Credential you want to delete does not exist
Has successfully been generated you can proceed to use it in your account.
Thanks for using passward lock welcome next time
Wrong entry....check your entry again and match it with those in the menu
Enter valid input

## Known Bugs
The application works perfectly well,there are no known bugs if you find any let me know.
## Technologies used
- Python
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
