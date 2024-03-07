
hours = 'Hours'
days = 'Days'
months = 'Months'

telegram = 'Telegram'
email = 'Email'

e_mail= 'email'
t_elegram = 'telegram'
telegram_id = 'telegram_id'

username = 'username'
password = 'password'
Invalid_Username_or_Password = 'Invalid Username or Password'
last_name = 'last_name'
first_name = 'first_name'
interests = 'interests'


TIMEUNIT_CHOICES = [
    (hours, hours),
    (days, days),
    (months, months),
]

TIMEFRAME_CHOICES = [
    ('H1', 'H1'),
    ('H4', 'H4'),
    ('D1', 'D1'),
    ('W1', 'W1'),
    ('M1', 'M1'),
]

CONDITION_CHOICES = [
    ('C>TP','CLOSES ABOVE target price'),
    ('C<TP', 'CLOSES BELOW target price'),
    ('H>TP', 'HIGHEST price is ABOVE target price'),
    ('H<TP', 'HIGHEST price is BELOW target price'),
    ('L>TP', 'LOWEST price is ABOVE target price'),
    ('L<TP', 'LOWEST price is BELOW target price'),
]

CURRENCY_CHOICES = [
    ('EURUSD', 'EUR/USD'),
    ('AUDJPY', 'AUD/JPY'),
    ('EURCHF', 'EUR/CHF'),
    ('EURJPY', 'EUR/JPY'),
    ('USDJPY', 'USD/JPY'),
    ('GBPUSD', 'GBP/USD'),
    ('AUDUSD', 'AUD/USD'),
    ('USDCAD', 'USD/CAD'),
    ('USDCHF', 'USD/CHF'),
    ('CADCHF', 'CAD/CHF'),
    ('CHFJPY', 'CHF/JPY'),
    ('USDHKD', 'USD/HKD'),
    ('EURGBP', 'EUR/GBP'),

    # {'id':'frxAUDUSD', 'table': 'AUDUSD'},
    # {'id':'frxEURGBP', 'table': 'EURGBP'},
    # {'id':'frxEURJPY', 'table': 'EURJPY'},
    # {'id':'frxEURUSD', 'table': 'EURUSD'},
    # {'id':'frxGBPUSD', 'table': 'GBPUSD'},
    # {'id':'frxUSDCAD', 'table': 'USDCAD'},
    # {'id':'frxUSDCHF', 'table': 'USDCHF'},
    # {'id':'frxUSDJPY', 'table': 'USDJPY'},

    # must switch this to avioid swapped currency pair name
    #('frxXAUUSD', 'GoldUSD') is the original

    ('GoldUSD', 'frxXAUUSD'),
    ( 'Volatility_50_Index', 'Volatility 50 Index'),
    ( 'Volatility_75_Index', 'Volatility 75 Index'),
    ( 'Volatility_100_Index', 'Volatility 100 Index'),
    ( 'Step_Index', 'Step Index'),
    ( 'Boom_500_Index', 'Boom 500 Index'),
    ( 'Boom_1000_Index', 'Boom 1000 Index'),
    ( 'Crash_500_Index', 'Crash 500 Index'),
    ( 'Crash_1000_Index', 'Crash 1000 Index'),
    ( 'Jump_50_Index', 'Jump 50 Index'),
    ( 'Jump_75_Index', 'Jump 75 Index'),
    ( 'Jump_100_Index','Jump 100 Index'),

    # ('BTC/USDT', 'BTC/USDT'),
    # ('ETH/USDT', 'ETH/USDT'),

    ('ETHUSDT', 'ETH/USD'),
    ('BTCUSDT', 'BTC/USD'),
    ('SOLUSDT', 'SOL/USD'),
    ('FTTUSDT', 'FTT/USD'),
    ('XRPUSDT', 'XRP/USD'),
    ('BNBUSDT', 'BNB/USD'),
    ('LINKUSDT', 'LINK/USD'),
    ('FTTUSDT', 'FTT/USD'),
    ('AVAXUSDT', 'AVAX/USD'),
    ('TIAUSDT', 'TIA/USD'),
    ('AVAXUSDT', 'AVAX/USD')
]

INTERESTSCHOICES = [
    ('Forex','Forex' ),
    ('Crypto', 'Crypto'),
    ('Deriv', 'Deriv'),
    ('Metals', 'Metals'),
]

email_already_exist= 'This Email Alerady Exist'

expiration_value = 'expiration_value'
expiration_unit = 'expiration_unit'
currency_pair = 'currency_pair'
setup_condition = 'setup_condition'
timeframe = 'timeframe'
repeat_alarm = 'repeat_alarm'
target_price = 'target_price'
note = 'note'
time_created_neg = '-time_created'


# Approved candlestick chart patterns
APPROVED_PATTERNS = ['engulfing', 'morningstar', 'morningdojistar', '3blackcrows',
                     'abandonedbaby',  'dojistar', 'dragonflydoji', 'eveningdojistar',
                     'gravestonedoji', 'longleggeddoji', 'morningdojistar', 'kicking',
                     'kickingbylength', 'hammer', 'invertedhammer', '3whitesoldiers',
                     'spinningtop', 'piercing', 'darkcloudcover', 'risefall3methods',
                     'xsidegap3methods', 'shootingstar', 'hangingman', 'harami',
                     'haramicross', 
                     ]