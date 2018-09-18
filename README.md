# AvidLiker

> To be liked you first need to like others. -- the wise.

Life is short. How can I make smart use of my time to express my respect to people I follow on Twitter promptly without making myself exhausted?
This script helps you login into your Twitter account, and click the favorite button on tweets that appear on your timeline. Sounds wonderful huh?
## Usage
It is pretty straight forward. 
1) Make a text file 'username' containing your login email.
2) Make a text file 'password' (preferrably only readable to the script run-as user) containing your login password.
3) Just fire and see!!
```
% python like_your_timeline.py
```
A sample output
```
2018-09-17 18:32:38,226 [MainThread  ] [INFO ] Using username: abc@gmail.com
2018-09-17 18:32:38,227 [MainThread  ] [INFO ] Password read from file
2018-09-17 18:32:53,516 [MainThread  ] [INFO ] Login OK
2018-09-17 18:32:53,543 [MainThread  ] [INFO ] Found 49 clickable heart buttons
2018-09-17 18:33:00,236 [MainThread  ] [INFO ] clicked like for TicToc by Bloomberg
2018-09-17 18:33:01,564 [MainThread  ] [INFO ] clicked like for Stephanie Hurlburt
...
...
2018-09-17 18:34:10,257 [MainThread  ] [INFO ] Successfully clicks: 49
```

Of course you will need to install some dependency packages first. If you have some prioror experience working with web scraping, this will not be a problem for you.

## Disclaimer
You can use or modify the code in anyway you want. Just don't be too aggresive or you may get blocked by Twitter. Be a good internet citizen.
