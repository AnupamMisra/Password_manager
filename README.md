# Password_manager
DSP project for PGPDS at Praxis. I created the backend and the frontend for this project.

Features:

1.	No. of encoding schemes used: 12
'blake2b','blake2s','md5','sha1','sha224','sha256','sha384','sha3_224','sha3_256','sha3_384','sha3_512','sha512'

2.	Password can be generated in two ways
  a. A keyphrase to be encoded
  b. A random 10 digit no. is generated

3.	Password structure: (0:14)(Random_alphabet_in_caps)(*)(15:29)
The digits are the first n digits from the hashed password generated. Total size: 32 bits

4.	Every time a new website login is set up, a different hashing scheme is selected from the available ones, in a round robin fashion. 
    This counter is also stored in a database in the cloud.

5.	User only needs to remember the master password; this is hashed using SHA224. After login, a message will be sent to the user that the user has logged in.

6.	On forgetting the master password, it can be reset by answering the security question and OTP(Need to set this up).

7.	Passwords are stored in a SQL database in the cloud.

8.	Security question’s answer is hashed using SHA224 and stored locally.

9.	In case a website login is compromised, the password can be regenerated on answering the security question.

10.	After login, if the user wants to retrieve a website’s password, on authentication, it is automatically copied to the clipboard.

11.	This was my first project on flask. I loved it.

