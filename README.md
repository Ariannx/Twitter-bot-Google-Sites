# Twitter Bot with Google Sites

***By: Armijos Arianna / Román Stadyn***

The objective of this project is to create a **Twitter bot** that publish tweets about information that can be inside of a 
**Google Sites** through a virtual machine with **Raspberry**.
This bot will publish the link and the principal phrase of first paragraph of each sub web page of your Google Sites.
The techinque will be use is **Scraping Web**

### Example
![](/Pictures/Capture_google_sites1.png)
<p align="center">
  <img src="/Pictures/Capture_twitter_bot.png">
</p>

## Steps for Twitter :feet: 
* Creating a New Account in [Twitter](https://twitter.com/). This account will be for the bot.
* Creating a Account in [Twitter Developer](https://developer.twitter.com/en) in order to have access to our Api for any app.
* In [Twitter Developer](https://developer.twitter.com/en) we have to register our bot app on Twitter.
* In this step we have to the Keys and Tokens 

## Steps for Google Sites :feet:
* Creating a [Google Sites](https://sites.google.com/new)
* Creating a site that contain sub web pages (for more facility)
* You can modify your site in your own way

## VM Raspberry :computer:
* Memory Ram: 1 GB
* Storage: 32 GB
* Clock Speed: 1.4 GHz
* OS: Raspbian


## Installation :computer:
We have to create a virtual environment within VM
```
sudo pip3 install virtualenv
virtualenv <name-your-env> -p python3
source <your-env>/bin/activate
<your-env>/bin/<editor> <name-file-bot>.py
<your-env>/bin/<editor> <name-file-credentials-twitter-developer>.py
<your-env>pip3 install <necessary-libraries>

```

## Supported Python Versions :snake:
From Python 3.7 onwards are fully supported.

## Libraries and Modules :page_facing_up:
* [requests](https://pypi.org/project/requests/)
* [twitter](https://pypi.org/project/twitter/)
* [lxml](https://lxml.de/lxmlhtml.html)
* [nltk](https://www.nltk.org/)
* [time](https://docs.python.org/3/library/time.html)
* [credentials](https://developer.twitter.com/en) of your app 
```
<your-env>pip3 install <each-library-or-module>
```
## Preview :exclamation:
A little example about: How the bot works in the console.
![](/Pictures/preview_1.jpeg)
![](/Pictures/preview_2.jpeg)

## More information about it :file_folder:
https://www.blog.binaria.uno/2019/07/29/escrapear-paginas-web-y-publicar-contenido-en-twitter-con-python/
https://scrapinghub.com/what-is-web-scraping
https://www.w3schools.com/xml/xpath_intro.asp
