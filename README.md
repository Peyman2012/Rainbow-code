# Rainbow-code
![image](https://github.com/Peyman2012/Rainbow-code/assets/88220773/814b2f6b-2d26-4951-8b74-126d84e3918a)

Find password through hacked hash from server database
SHA, ( Secure Hash Algorithms ) are set of cryptographic hash functions defined by the language to be used for various applications such as password security etc. Some variants of it are supported by Python in the “hashlib” library. These can be found using “algorithms_guaranteed” function of hashlib.

Functions associated :
 encode() : Converts the string into bytes to be acceptable by hash function.
 hexdigest() : Returns the encoded data in hexadecimal format.
 
SHA Hash:
The different SHA hash functions are explained below.
SHA256 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits.
SHA384 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits. This is one of the truncated version.
SHA224 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits. This is one of the truncated version.
SHA512 : This hash function belong to hash class SHA-2, the internal block size of it is 64 bits.
SHA1 : The 160 bit hash function that resembles MD5 hash in working and was discontinued to be used seeing its security vulnerabilities.

Explanation : The above code takes string and converts it into the byte equivalent using encode() so that it can be accepted by the hash function. The SHA hash functions encode it and then using hexdigest(), hexadecimal equivalent encoded string is printed.
You are expected to be able to do the hacking project in this course; You have a csv file that is divided into two parts. One part of that name and the other part is a hash of the password.

How to do the project:

Hash is a one-way function that outputs y based on input x. But there is no mathematical formula to get from y to x. Its use is that you hash something and arrive at y.

If someone hacks function x, they won't get your real password. We have different hash function. Each hash function works in a specific way. (As a note: all passwords are 4 digits and digits can be numbers 0 to 9. We also know that sha256 algorithm is used for hashing.) So it is expected that you can open this file and read the file information. Separate it and specify its name and password. In fact, it is enough to write a for loop that works from 0-9999, for example. Each time, it encodes the desired number with the above algorithm and returns a string, and compares this string with the codes given in the file, and if the number is equal, it stores this string as a password in the output.
This method is called rainbow hacking.
