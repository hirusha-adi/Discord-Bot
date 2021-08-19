from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  # return "Hello, I am alive!"
  return """<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title> Hirusha Adikari </title>

<style>
* { color: #333; font-family: verdana,monospace }
body { max-width: 75rem; margin: 0 auto; padding: 1rem; display: flex; flex-wrap: wrap }
h1, h2 { width: 100%; font-weight: normal; border-bottom: 1px dotted #ddd }
h1 { font-size: 1.5rem; padding: 0.5rem }
h2 { font-size: 1rem; margin: 0; padding: 0 0 0.5rem 0 }
info, tool { flex-grow: 1; flex-basis: 20rem; display: flex; margin: 1rem; padding: 1rem }
info { align-items: center }
info > a { display: flex; flex-direction: column; justify-content: center; }
info > a > img:not(.full) { max-width: 2.5rem; max-height: 2.5rem; margin-right: 1rem }
hint { cursor: help; text-decoration: underline dotted }
tool { flex-direction: column; padding-bottom: 0.5rem; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0px 2px 2px rgba(0,0,0,0.2) }
about { flex-grow: 1; display: flex }
logo { padding: 1rem 1rem 0 0 }
logo > a { font-size: 3.2rem; text-decoration: none }
logo > img, logo > a > img { height: 4rem; max-width: 4rem }
deeds { flex-grow: 1; display: flex; flex-direction: column }
deeds > .more { flex-grow: 1; display: flex; flex-direction: column-reverse; text-align: right }
</style>

<body>

<h1> hello </h1>

<info> My name is&nbsp;<hint title="Some call be ZeaCeR">Hirusha</hint>. </info>
<info> I'm a student. </info>
<info> I create simple projects for fun. </info>

<h1> My Projects </h1>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Hack-with-pendrive target=blank> The Hacking Pendrive </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Hack-with-pendrive target=blank> <img src=https://user-images.githubusercontent.com/36286877/127767173-b22f217f-8bf9-471a-a99f-ce65b923f66f.png /> </a> </logo>
    <deeds>
      <p> Follow the give steps in the <a href=https://github.com/hirusha-adi/Hack-with-pendrive/blob/main/README.md target=blank>ReadMe</a> file and create a little hacking device </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Hack-with-pendrive target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Discord-Bot target=blank> Discord Bot </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Discord-Bot target=blank> <img src=https://user-images.githubusercontent.com/36286877/127767330-d3e68d90-67a0-4672-b3e1-6193b323bc21.png> </a> </logo>
    <deeds>
      <p> Named <a href="https://discord.com/api/oauth2/authorize?client_id=858303945167208448&permissions=8&scope=bot">YourBot</a> has over 150 commands for users to ENJOY!</p>
      <span class=more> <a href=https://github.com/hirusha-adi/Discord-Bot target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/windows-11-setup-virus target=blank> Windows 11 Setup Virus </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/windows-11-setup-virus target=blank> <img src=https://user-images.githubusercontent.com/36286877/127767591-1ee427a9-6aa4-4c47-9d15-454bfcf51a9a.png> </a> </logo>
    <deeds>
      <p> A complete python program that runs malicious code while mimmicking the look the original windows inatller tool </p>
      <span class=more> <a href=https://github.com/hirusha-adi/windows-11-setup-virus target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/iFake target=blank> iFake </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/iFake target=blank> <img src=https://user-images.githubusercontent.com/36286877/127768584-d94d0a78-15e7-4861-ac60-bd94b9da7608.png> </a> </logo>
    <deeds>
      <p> The mass Fake/Random Information Generator </p>
      <span class=more> <a href=https://github.com/hirusha-adi/iFake target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/ikmanLK-Scrapper target=blank> ikman.lk web scrapper </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/ikmanLK-Scrapper target=blank> <img src=https://user-images.githubusercontent.com/36286877/127768735-14d8a4c3-7bcb-448b-927d-185609b34a77.png> </a> </logo>
    <deeds>
      <p> The easy to use ikman.lk scraper - just a web scraper </p>
      <span class=more> <a href=https://github.com/hirusha-adi/ikmanLK-Scrapper target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/IP-Lookup target=blank> IP Lookup Tool </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/IP-Lookup target=blank> <img src=https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png> </a> </logo>
    <deeds>
      <p> lightweight IP lookup program made using a <a href="http://ip-api.com/json/" target=blank>Public API</a> ( my first time using an API ) </p> 
      <span class=more> <a href=https://github.com/hirusha-adi/IP-Lookup target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Simple-Calculator-with-Python target=blank> Calculator </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Simple-Calculator-with-Python target=blank> <img src=https://user-images.githubusercontent.com/36286877/127769028-80ad6ff6-9a89-4265-94d5-fb0182a4edda.png> </a> </logo>
    <deeds>
      <p> The most simple calculator with a GUI. Very first project using tkinter </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Simple-Calculator-with-Python target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://hirusha-adi.github.io/bsoderrorcodes target=blank> BSOD Error Codes Websites </a> </h2>
  <about>
    <logo> <a href=https://hirusha-adi.github.io/bsoderrorcodes target=blank> <img src=https://user-images.githubusercontent.com/36286877/127769772-8ebf5e52-c366-4acd-9943-badbe8f37be9.png> </a> </logo>
    <deeds>
      <p> A simple <a href=https://hirusha-adi.github.io/bsoderrorcodes target=blank>website</a> that lists all windows BSOD error codes </p>
      <span class=more> <a href=https://github.com/hirusha-adi/bsoderrorcodes target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Userphone-Fun-Discord target=blank> Userphone Abuse </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Userphone-Fun-Discord target=blank> <img src=https://user-images.githubusercontent.com/36286877/127774939-785cea51-1c98-426e-aeff-25cf91448f29.png> </a> </logo>
    <deeds>
      <p> Abuse the discord bot named <a href=https://ygg.fun target=blank>Yggdrasil</a>. This belongs to the category of spam </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Userphone-Fun-Discord target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Contact-Manager-CLI target=blank> Contact Manager CLI </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Contact-Manager-CLI target=blank> <img src=https://uxwing.com/wp-content/themes/uxwing/download/10-brands-and-social-media/google-contacts.png> </a> </logo>
    <deeds>
      <p> A simple robust method to manage your contacts without leaving the terminal </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Contact-Manager-CLI target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Python3-NmapScanner target=blank> Nmap Automation </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Python3-NmapScanner target=blank> <img src=https://user-images.githubusercontent.com/36286877/127775183-f9209289-cd3c-4185-abc1-3e11471dc20a.png> </a> </logo>
    <deeds>
      <p> Improved version of the original script by <a href=https://github.com/AlexisAhmed/Python3-NmapScanner target=blank>Hackersploit/AlexisAhmed</a> </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Python3-NmapScanner target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/json-formatter target=blank> JSON Formatter </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/json-formatter target=blank> <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/JSON_vector_logo.svg/2048px-JSON_vector_logo.svg.png> </a> </logo>
    <deeds>
      <p> Format bad/unformatted json files. Useful for working with APIs that return unformatted JSON </p>
      <span class=more> <a href=https://github.com/hirusha-adi/json-formatter target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>


<tool>
  <h2> <a href=https://github.com/hirusha-adi/Dictionary target=blank> Simple Smart Dictionary </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Dictionary target=blank> <img src=https://user-images.githubusercontent.com/36286877/127775392-c178b583-879e-4912-992b-8f1a26141bad.png> </a> </logo>
    <deeds>
      <p> I think this is somewhat smart over other beginner level dictionaries out there and this has a GUI </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Dictionary target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Riyasewana-Scraper target=blank> Riyasewana.com web scrapper </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Riyasewana-Scraper target=blank> <img src=https://user-images.githubusercontent.com/36286877/127775590-107fc644-b036-4845-9980-1d3d605967c2.png> </a> </logo>
    <deeds>
      <p> The easy to use riyasewana.com scraper - just a web scraper </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Riyasewana-Scraper target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Intel-Scraper target=blank> ark.intel.com web scrapper </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Intel-Scraper target=blank> <img src=https://raw.githubusercontent.com/hirusha-adi/Intel-Scraper/main/intel_logo.ico> </a> </logo>
    <deeds>
      <p> Scrap processor/CPU information from <a href="https://ark.intel.com/content/www/us/en/ark/products/212325/intel-core-i9-11900k-processor-16m-cache-up-to-5-30-ghz.html" target=blank>ark.intel.com/content</a> - just a web scraper </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Intel-Scraper target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/xTable-CLI target=blank> xTable </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/xTable-CLI target=blank> <img src=https://user-images.githubusercontent.com/36286877/127775685-ad53f444-162c-4e74-a4c2-9352022d4451.png> </a> </logo>
    <deeds>
      <p> Generate any multiplication table upto any number to a txt,csv file </p>
      <span class=more> <a href=https://github.com/hirusha-adi/xTable-CLI target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/bat-code-generator target=blank> .bat Code Generator </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/bat-code-generator target=blank> <img src=https://user-images.githubusercontent.com/36286877/127776088-0d756f33-37df-4bd1-b69b-1444dc363f45.png> </a> </logo>
    <deeds>
      <p> Generate harmful batch code to run that will destroy windows </p>
      <span class=more> <a href=https://github.com/hirusha-adi/bat-code-generator target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Image-Resizer target=blank> Image Resizer 1 </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Image-Resizer target=blank> <img src=https://www.graphicpie.com/wp-content/uploads/2020/11/red-among-us-png.png> </a> </logo>
    <deeds>
      <p> Resize images easily with this lightweight script - PIL based </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Image-Resizer target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/Image-Resizer-2 target=blank> Image Resizer 2 </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/Image-Resizer-2 target=blank> <img src=https://www.graphicpie.com/wp-content/uploads/2020/11/red-among-us-png.png> </a> </logo>
    <deeds>
      <p> Resize images easily with this lightweight script - cv2/OpenCV base </p>
      <span class=more> <a href=https://github.com/hirusha-adi/Image-Resizer-2 target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/encode-and-decode/tree/main/Base64 target=blank> Base64 Stuff </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/encode-and-decode/tree/main/Base64 target=blank> <img src=https://onlinepngtools.com/images/examples-onlinepngtools/bomb.png> </a> </logo>
    <deeds>
      <p> Encode and Decode </p>
      <span class=more> <a href=https://github.com/hirusha-adi/encode-and-decode/tree/main/Base64 target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/arp-spoofer target=blank> ARP Spoofer </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/arp-spoofer target=blank> <img src=https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png> </a> </logo>
    <deeds>
      <p> a simple ARP spoofer </p>
      <span class=more> <a href=https://github.com/hirusha-adi/arp-spoofer target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/ftp-sniffer target=blank> FTP Sniffer </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/ftp-sniffer target=blank> <img src=https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png> </a> </logo>
    <deeds>
      <p> a simple FTP sniffer </p>
      <span class=more> <a href=https://github.com/hirusha-adi/ftp-sniffer target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>

<tool>
  <h2> <a href=https://github.com/hirusha-adi/http-sniffer target=blank> HTTP Sniffer </a> </h2>
  <about>
    <logo> <a href=https://github.com/hirusha-adi/http-sniffer target=blank> <img src=https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png> </a> </logo>
    <deeds>
      <p> a simple HTTP sniffer </p>
      <span class=more> <a href=https://github.com/hirusha-adi/http-sniffer target=blank> more… </a> </span>
    </deeds>
  </about>
</tool>




<h1> more </h1>

<info> <a href=https://github.com/hirusha-adi><img src=https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png></a> I write code. </info>
<info> <a href=https://twitter.com/hirusha_adikari><img src="https://i1.wp.com/www.apacph.org/wp/wp-content/uploads/2014/03/Twitter-Logo-New-.png?fit=518%2C518&ssl=1&w=640"></a> I tweet cool things. </info>
<info> <a href=https://www.youtube.com/channel/UC6rhQaniYiHId_x7HsHbX_A><img src=https://user-images.githubusercontent.com/36286877/127772778-32629ae4-da34-4cb2-8054-23840b4bfcec.png></a> I upload useful videos sometimes. </info>
<info> <a href=https://www.instagram.com/hirusha.adikari.photography><img src=https://assets.stickpng.com/images/580b57fcd9996e24bc43c521.png></a> I have this for photgraphy stuff.  </info>
<info> <a href=https://www.instagram.com/hirusha.adikari.private><img src=https://assets.stickpng.com/images/580b57fcd9996e24bc43c521.png></a> I have this for my projects + IT stuff. </info>
<info> <a href=https://www.instagram.com/hirusha.adikari><img src=https://assets.stickpng.com/images/580b57fcd9996e24bc43c521.png></a> I lost this account. </info>
<info> <a href=https://linkedin.com/in/jankeromnes><img src=https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Linkedin.svg/1200px-Linkedin.svg.png></a> Im still a 10th grader. </info>


</body>
"""

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
