# cipher-tools
cipher-tools is a python script which allows you to encrypt/decrypt/crack messages using various ciphers

# usage

use the script using the following command **python3 cipher-tools.py [cipher] [mode] [plaintext] [extra]**  

## [cipher]
### railfence cipher
**[cipher] = -rf**  
**[extra]** = number of rails


### caesar cipher
**[cipher] = -ca**  
**[extra]** = shift number

## [mode]
**-e**: encryption  
**-d**: decryption  
**-c**: cracking (try to crack ciphertext using all availible ciphers)

use **--help** for usage help  
  
## example uses

> **python3 cipher-tools.py -rf -e hello-this-is-cipher-tools 5**

this command will encrypt the phrase *hello-this-is-cipher-tools* with the railfence cipher using a rail number of 5, producing *hsreiietlhsholtcposoil*  

> **python3 cipher-tools.py -ca -d yvccf-kyzj-zj-tzgyvi-kffcj 9**  

this command will decrypt the phrase *yvccf-kyzj-zj-tzgyvi-kffcj* using caesar cipher and a shift of 9, producing *hello-this-is-cipher-tools*

> **python3 cipher-tools.py -c hsreiietlhsholtcposoil 5**

this command will try to crack the message *hsreiietlhsholtcposoil* using all availible ciphers and an accuracy of 5 (must contain 5 words to be considered a potential solution). this produces 2 possible solutions. One of which is *hellothisisciphertools*


