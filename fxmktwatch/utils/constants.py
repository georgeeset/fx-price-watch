
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
    ('CLOSING PRICE IS GREATER THAN SETPOINT','CLOSING PRICE IS GREATER THAN SETPOINT'),
    ('CLOSING PRICE IS LESS THAN SETPOINT', 'CLOSING PRICE IS LESS THAN SETPOINT'),
    ('OPENING PRICE IS GREATER THAN SETPOINT', 'OPENING PRICE IS GREATER THAN SETPOINT'),
    ('OPENING PRICE IS LESS THAN SETPOINT', 'OPENING PRICE IS LESS THAN SETPOINT'),
    ('HIGHEST PRICE IS GREATER THAN SETPOINT', 'HIGHEST PRICE IS GREATER THAN SETPOINT'),
    ('HIGHEST PRICE IS LESS THAN SETPOINT', 'HIGHEST PRICE IS LESS THAN SETPOINT'),
    ('LOWEST PRICE IS GREATER THAN SETPOINT', 'LOWEST PRICE IS GREATER THAN SETPOINT'),
    ('LOWEST PRICE IS LESS THAN SETPOINT', 'LOWEST PRICE IS LESS THAN SETPOINT'),
]

CURRENCY_CHOICES = [
    ('EURUSD', 'EUR/USD'),
    ('EURJPY', 'EUR/JPY'),
    ('USDJPY', 'USD/JPY'),
    ('GBPUSD', 'GBP/USD'),
    ('AUDUSD', 'AUD/USD'),
    ('USDCAD', 'USD/CAD'),
    ('USDCHF', 'USD/CHF'),
    ('CADCHF', 'CAD/CHF'),
    ('USDCNY', 'USD/CNY'),
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
    ('frxXAUUSD', 'GoldUSD'),
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
