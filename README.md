# RedFlags
RedFlags is an automated version of the service offered by [Red Flag Domains](https://red.flag.domains/). It can be used as a simple monitoring tool to check if malicious actors are targeting your company with future phishing attacks. You can set it up on a cron to receive daily results, and the script will send automated notifications to your Telegram channel

To use RedFlags, you need to put your Telegram token and channel ID in the script, and run it with the command </br>'Python3 script.py [company main domain identity]'. </br>For example, to monitor PayPal, you would run 'Python3 script.py paypal'.

# RedFlags
RedFlags is an automated version of the service offered by [Red Flag Domains](https://red.flag.domains/). It can be used as a simple monitoring tool to check if malicious actors are targeting your company with future phishing attacks. You can set it up on a cron to receive daily results, and the script will send automated notifications to your Telegram channel


<h2 id="installation"> Installation</h2>

```
git clone https://github.com/UncleJ4ck/RedFlags
cd RedFlags
pip3 install -r requirements.txt
python3 script.py [company main domain identity]
```  
