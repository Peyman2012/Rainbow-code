# Rainbow-code
![image](https://github.com/Peyman2012/Rainbow-code/assets/88220773/814b2f6b-2d26-4951-8b74-126d84e3918a)

Find password through hacked hash from server database
SHA, ( Secure Hash Algorithms ) are set of cryptographic hash functions defined by the language to be used for various applications such as password security etc. Some variants of it are supported by Python in the “hashlib” library. These can be found using “algorithms_guaranteed” function of hashlib.

Functions associated :
 encode() : Converts the string into bytes to be acceptable by hash function.
 hexdigest() : Returns the encoded data in hexadecimal format.
SHA Hash
The different SHA hash functions are explained below.

SHA256 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits.
SHA384 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits. This is one of the truncated version.
SHA224 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits. This is one of the truncated version.
SHA512 : This hash function belong to hash class SHA-2, the internal block size of it is 64 bits.
SHA1 : The 160 bit hash function that resembles MD5 hash in working and was discontinued to be used seeing its security vulnerabilities.
Explanation : The above code takes string and converts it into the byte equivalent using encode() so that it can be accepted by the hash function. The SHA hash functions encode it and then using hexdigest(), hexadecimal equivalent encoded string is printed.
