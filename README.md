<p align=center>
  <img src="./images/logo.png" width=600 height=461 />
  <br>
  <span>OSINT - Gather information about target.</span>
  <br>
  <img src="https://img.shields.io/badge/platforms-Windows%20%7C%20Linux%20%7C%20OSX-success.svg">
  <img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg">
  <img src="https://img.shields.io/badge/License-GMT3.0-blue.svg">
</p>

---- 

**God's Eye** is an email, nickname and IP OSINT and breach hunting tool. Everything with clear and simple GUI.

----
 
## Steganography

Let’s understand what is steganography.

### What is steganography?

> [Steganography](https://en.wikipedia.org/wiki/Steganography) is the practice of concealing a file, message, image, or video within another file, message, image, or video.

### What is the advantage of steganography over cryptography?
> The advantage of steganography over [cryptography](https://en.wikipedia.org/wiki/Cryptography) alone is that the intended secret message does not attract attention to itself as an object of scrutiny. Plainly visible encrypted messages, no matter how unbreakable they are, arouse interest and may in themselves be incriminating in countries in which [encryption](https://en.wikipedia.org/wiki/Encryption) is illegal.

In other words, steganography is more discreet than cryptography when we want to send a secret information. On the other hand, the hidden message is easier to extract.

## Installation

```console
# clone the repo
$ git clone https://github.com/Loiuy123/Tartarus.git

# change the working directory to tartarus
# cd tartarus
```

## Usage

```console
$python tartarus.py
commands:
  help - List of all commands with descriptions
  zwc - Hidden messages using Zero Width Characters
  siEncode - Steganography; Hide message in image
  siCheck - Steganography Check; Look for hidden message in image
  pipMerge - Merge two images into one
  pipUnmerge - Unmerge images
  swEncode - Encode text inside of wav file
  swRecover - Recover text from the wav file
```

## WAV Steganography

Secret to be known to recover data from the steganographic output is the number of LSBs used and the number of bytes hidden.

## Zero Width Characters

Hide or extract hidden message made out of zero with characters:
```
Message before: 
Hey I contain top secret message!

After running zwc decode:
Hey I contain top secret message! It's me - secret message
```
(You might see some weird symbols in the terminal after pasting message containing zero width characters but don't worry - they are invisible in other apps)

## Contributing
We would love to have you help me with the development of Tartarus. Each and every contribution is greatly valued! Contact me via Discord - Theos#2613
