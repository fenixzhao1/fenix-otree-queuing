from os import environ

SESSION_CONFIGS = [
    dict(
        name='queuing_experiment',
        display_name='queuing_experiment',
        num_demo_participants=6,
        app_sequence=['queuing_experiment'],
        config_file='production_swap_nocomm_6p.csv',
        num_silos=1,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

ROOMS = [
    dict(
        name='session_room',
        display_name='Session Room',
        participant_label_file='_rooms/participant_label.txt',
        # use_secure_urls=True
    ),
]

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 1

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'admin'

DEMO_PAGE_INTRO_HTML = """ """
# STATIC_ROOT = '__static_root'
SECRET_KEY = '2408944957260'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
EXTENSION_APPS = ['otree_redwood']
# each time the experiment is deployed on the redwood env `set DJANGO_SETTINGS_MODULE=mysite.settings`
