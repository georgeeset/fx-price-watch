# fx-price-watch
---
Alx portfolio project By: George Esetevbe\
            Linkedin: [George-Esetevbe](https://www.linkedin.com/in/george-esetevbe-b5447280/)\
            Email: georgeperfect4u@gmail.com\
---

## Forex and Crypto Price alert web application

* Traders who want to stay up-to-date with the latest developments in the forex market rely on forex price alerts. These alerts notify traders of changes in the exchange rates of currency pairs, allowing them to make informed decisions on when to buy or sell. Most Traders lose their money and good trading opportunities due to these reasons:

* Traders do not follow their pre-planned trading principle either because they check the market too often or they get impatient as they spend extended amounts of time in front of their trading computer.

* In forex trading, Profit and loss depends on your entry point. If a trader fails to open his trade at the right time, will either miss out on profit or incure more losses.

* Emotions such as fear and greed can impact a trader’s decision-making process and lead to impulsive trading, increased risk, and ultimately financial losses.

* The stress involved in keeping up with forex price news and technical analyses at different time frame is quite tedious and usually affects the time that should be used for other things in a trader’s life

* Long term forex traders who invest in long term stocks, commodities and currency pairs need to watch the status of all commodities of interest daily and they eventually trade once a couple of times in a year. They need a reliable reminder platform to enable them to make the right long term decision at the right time.

### AIM OF PROJECT

The application solveS the above issues faced by forex traders. All users will be able to set price alerts for supported currency pair and choose any of the supported mediums such as Email, Telegram, Whatsapp, X for alert. This will allow them to take their mind off the market for a significant amount of time without missing out in any entry opportunity.
Traders who trade multiple marketrs will get notified when their expected trade setup has formed. 

### TECHNOLOGIES

The entire web application was build using Django Framework. The following features were also used in the web application.
- User authentication using the django in-built authentication packages for loging user in and registering users.
- The application employs django email package to verify user email.
- Telegram messaging serviece used for sending private telegram messages to user.
- Django ORM database management. the application uses Mysql database.
- HtML, CSS and Javascipt for user interface using the jinja render feature of the Django framework.

### OTHER OPERATIONS
The primary aim of this web app is to interface between alert request database and the users.
They will be able to place and manage alerts.
- In order to achieve complete operations such as sending notifications and checking for currenty prices, some scripts have to run on schedule to fetch price data and query alerts table to see conditions that have been fufilled and send private messages accordingly.
- The backend script project can be accessed at [fx_python_scripts](https://github.com/georgeeset/fx_python_scripts)
