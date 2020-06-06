# cipher-tools
cipher-tools is a python script which allows you to encrypt/decrypt messages using various ciphers

# usage

use the script using the following command **python3 cipher-tools.py [cipher] [mode] [plaintext] [extra]**  

## [cipher]
### railfence cipher
**[cipher] = -rf**  
**[extra]** = number of rails


### caesar cipher
**[cipher] = -c**  
**[extra]** = shift number

## [mode]
**-e**: encryption  
**-d**: decryption

use **--help** for usage help  
  
## example uses

> **python3 cipher-tools.py -rf -e hello-this-is-cipher-tools 5**

this command will encrypt the phrase *hello-this-is-cipher-tools* with the railfence cipher using a rail number of 5  

> **python3 cipher-tools.py -c -d yvccf-kyzj-zj-tzgyvi-kffcj 9**  

this command will decrypt the phrase *yvccf-kyzj-zj-tzgyvi-kffcj* using caesar cipher and a shift of 9, producting *hello-this-is-cipher-tools*


