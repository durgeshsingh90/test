IndexError at /binblock/
list index out of range
Request Method:	POST
Request URL:	http://localhost:8000/binblock/
Django Version:	5.0.1
Exception Type:	IndexError
Exception Value:	
list index out of range
Exception Location:	C:\Durgesh\Office\Automation\AutoMate\AutoMate\binblock\views.py, line 272, in process_bins
Raised during:	binblock.views.bin_blocking_editor
Python Executable:	C:\Program Files\Python311\python.exe
Python Version:	3.11.9
Python Path:	
['C:\\Durgesh\\Office\\Automation\\AutoMate\\AutoMate',
 'C:\\Program Files\\Python311\\python311.zip',
 'C:\\Program Files\\Python311\\DLLs',
 'C:\\Program Files\\Python311\\Lib',
 'C:\\Program Files\\Python311',
 'C:\\Users\\f94gdos\\AppData\\Roaming\\Python\\Python311\\site-packages',
 'C:\\Users\\f94gdos\\AppData\\Roaming\\Python\\Python311\\site-packages\\win32',
 'C:\\Users\\f94gdos\\AppData\\Roaming\\Python\\Python311\\site-packages\\win32\\lib',
 'C:\\Users\\f94gdos\\AppData\\Roaming\\Python\\Python311\\site-packages\\Pythonwin',
 'C:\\Program Files\\Python311\\Lib\\site-packages']
Server time:	Mon, 16 Sep 2024 02:16:46 +0000
Traceback Switch to copy-and-paste view
C:\Users\f94gdos\AppData\Roaming\Python\Python311\site-packages\django\core\handlers\exception.py, line 55, in inner
                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Users\f94gdos\AppData\Roaming\Python\Python311\site-packages\django\core\handlers\base.py, line 197, in _get_response
                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Durgesh\Office\Automation\AutoMate\AutoMate\binblock\views.py, line 323, in bin_blocking_editor
        processed_bins = process_bins(bin_input)
                              ^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Durgesh\Office\Automation\AutoMate\AutoMate\binblock\views.py, line 272, in process_bins
    start = bins[0]
                 ^^^^^^^ …
Local vars
Request information
USER
AnonymousUser

GET
No GET data

POST
Variable	Value
csrfmiddlewaretoken	
'1zD2T8p7bg87jt6WLq282vnFRRoO4AazmQAQPTXAiK3DW1RPjPW8XQUw79BlbZ4c'
bins	
''
blocked_item	
'Maestro'
search_items	
'JCB'
FILES
No FILES data

COOKIES
Variable	Value
csrftoken	
'********************'
META
Variable	Value
ALLUSERSPROFILE	
'C:\\ProgramData'
APPDATA	
'C:\\Users\\f94gdos\\AppData\\Roaming'
CHROME_CRASHPAD_PIPE_NAME	
'\\\\.\\pipe\\crashpad_14068_KHPZFUVAOZGITPOX'
COLORTERM	
'truecolor'
COMMONPROGRAMFILES	
'C:\\Program Files\\Common Files'
COMMONPROGRAMFILES(X86)	
'C:\\Program Files (x86)\\Common Files'
COMMONPROGRAMW6432	
'C:\\Program Files\\Common Files'
COMPUTERNAME	
'LWDJMQ0J3'
COMSPEC	
'C:\\WINDOWS\\system32\\cmd.exe'
CONTENT_LENGTH	
'171'
CONTENT_TYPE	
'application/x-www-form-urlencoded'
CSRF_COOKIE	
'vr7Y6VIDhE5GNIV3Iz4a5vH1qsnHhz4N'
DJANGO_SETTINGS_MODULE	
'AutoMate.settings'
DLIB_NO_VF_DEFAULTS	
'1'
DLIB_SILENCE	
'1'
DRIVERDATA	
'C:\\Windows\\System32\\Drivers\\DriverData'
EFC_14316	
'0'
FDCBLDG	
'$BUILDING'
FDCCITY	
'$CITY'
FDCCNTRY	
'$COUNTRY'
FDCSTATE	
'$STATE'
FDCSUITE	
'$SUITE'
FDCUNIT	
'$BU'
FPS_BROWSER_APP_PROFILE_STRING	
'Internet Explorer'
FPS_BROWSER_USER_PROFILE_STRING	
'Default'
GATEWAY_INTERFACE	
'CGI/1.1'
GIT_ASKPASS	
'********************'
HOMEDRIVE	
'C:'
HOMEPATH	
'\\Users\\f94gdos'
HTTP_ACCEPT	
'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
HTTP_ACCEPT_ENCODING	
'gzip, deflate, br, zstd'
HTTP_ACCEPT_LANGUAGE	
'en-US,en;q=0.9'
HTTP_CACHE_CONTROL	
'max-age=0'
HTTP_CONNECTION	
'keep-alive'
HTTP_COOKIE	
'********************'
HTTP_HOST	
'localhost:8000'
HTTP_ORIGIN	
'http://localhost:8000'
HTTP_REFERER	
'http://localhost:8000/binblock/'
HTTP_SEC_CH_UA	
'"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"'
HTTP_SEC_CH_UA_MOBILE	
'?0'
HTTP_SEC_CH_UA_PLATFORM	
'"Windows"'
HTTP_SEC_FETCH_DEST	
'document'
HTTP_SEC_FETCH_MODE	
'navigate'
HTTP_SEC_FETCH_SITE	
'same-origin'
HTTP_SEC_FETCH_USER	
'?1'
HTTP_UPGRADE_INSECURE_REQUESTS	
'1'
HTTP_USER_AGENT	
('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/128.0.0.0 Safari/537.36')
ID	
'f94gdos'
IP	
'192.168.0.185'
IPOCTET1	
'192'
IPOCTET2	
'168'
IPOCTET3	
'0'
IPOCTET4	
'185'
JAVA_HOME	
'C:\\Program Files (x86)\\Java\\jre-1.8'
KIX_VER	
'4.60'
LANG	
'en_US.UTF-8'
LOCALAPPDATA	
'C:\\Users\\f94gdos\\AppData\\Local'
LOG4J_FORMAT_MSG_NO_LOOKUPS	
'true'
LOGONDOMAIN	
'1DC'
LOGONDRIVE	
'\\\\W5PVAD1018\\NETLOGON\\'
LOGONSERVER	
'\\\\SYWP2CTIMAD0006'
LOGONTIME	
'2024/08/31 01:16:53'
MAC	
'8038FBBCDC48'
MAVEN_PATH	
'C:\\Program Files\\Maven\\Apache Maven 3.9.4'
NUMBER_OF_PROCESSORS	
'8'
ONEDRIVE	
'C:\\Users\\f94gdos\\OneDrive'
ORIGINAL_XDG_CURRENT_DESKTOP	
'undefined'
OS	
'Windows_NT'
PATH	
('C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\java8path;C:\\Program '
 'Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Program '
 'Files\\Python311\\Scripts\\;C:\\Program '
 'Files\\Python311\\;C:\\HashiCorp_Terraform_1.5.7;C:\\Oracle\\product\\19.0.0\\client_1\\bin;C:\\Program '
 'Files (x86)\\Microsoft '
 'SDKs\\Azure\\CLI2\\wbin;C:\\Oracle\\Ora12c_64\\bin;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program '
 'Files\\PKWARE\\SCCLI;C:\\Program Files\\Kubernetes\\Kubectl '
 'CLI\\1.27\\;C:\\Program Files\\Microsoft VS Code\\bin;C:\\Program '
 'Files\\Amazon\\AWSCLIV2\\;C:\\Program Files\\PuTTY\\;C:\\Program '
 'Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program '
 'Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Program '
 'Files\\Kubernetes\\Kubectl '
 'CLI\\1.30\\;C:\\Users\\f94gdos\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\;C:\\Users\\f94gdos\\AppData\\Local\\Programs\\Python\\Python312\\;C:\\Users\\f94gdos\\AppData\\Local\\Programs\\Python\\Launcher\\;C:\\Users\\f94gdos\\AppData\\Local\\Microsoft\\WindowsApps;')
PATHEXT	
'.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW'
PATH_INFO	
'/binblock/'
PCBUILD	
'22621'
PCOS	
'NT4'
PROCESSOR_ARCHITECTURE	
'AMD64'
PROCESSOR_IDENTIFIER	
'Intel64 Family 6 Model 140 Stepping 1, GenuineIntel'
PROCESSOR_LEVEL	
'6'
PROCESSOR_REVISION	
'8c01'
PRODUCTSUITE	
'256'
PRODUCTTYPE	
'Windows Vista Enterprise Edition'
PROGRAMDATA	
'C:\\ProgramData'
PROGRAMFILES	
'C:\\Program Files'
PROGRAMFILES(X86)	
'C:\\Program Files (x86)'
PROGRAMW6432	
'C:\\Program Files'
PROMPT	
'$P$G'
PSMODULEPATH	
('C:\\Program Files '
 '(x86)\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules;C:\\Program '
 'Files\\Boldon James\\Power Classifier for Files\\')
PUBLIC	
'C:\\Users\\Public'
PYTHONSTARTUP	
'c:\\Users\\f94gdos\\.vscode\\extensions\\ms-python.python-2024.14.1-win32-x64\\python_files\\pythonrc.py'
QUERY_STRING	
''
REMOTE_ADDR	
'127.0.0.1'
REMOTE_HOST	
''
REQUEST_METHOD	
'POST'
RUN_MAIN	
'true'
SCRIPTDIR	
'\\\\W5PVAD1018\\NETLOGON'
SCRIPT_NAME	
''
SERVER_NAME	
'LWDJMQ0J3.fead.one'
SERVER_PORT	
'8000'
SERVER_PROTOCOL	
'HTTP/1.1'
SERVER_SOFTWARE	
'WSGIServer/0.2'
SESSIONNAME	
'Console'
STARTDIR	
'\\\\W5PVAD1018\\NETLOGON'
SYSTEMDRIVE	
'C:'
SYSTEMROOT	
'C:\\WINDOWS'
TEMP	
'C:\\Users\\f94gdos\\AppData\\Local\\Temp'
TERM_PROGRAM	
'vscode'
TERM_PROGRAM_VERSION	
'1.92.2'
TMP	
'C:\\Users\\f94gdos\\AppData\\Local\\Temp'
TNS_ADMIN	
'C:\\Oracle\\Ora12c_64\\network\\admin'
UATDATA	
'C:\\WINDOWS\\CCM\\UATData\\D9F8C395-CAB8-491d-B8AC-179A1FE1BE77'
USER	
'f94gdos'
USERDNSDOMAIN	
'fead.one'
USERDOMAIN	
'FEAD'
USERDOMAIN_ROAMINGPROFILE	
'FEAD'
USERFULL	
'Singh, Durgesh'
USERNAME	
'F94GDOS'
USERPROFILE	
'C:\\Users\\f94gdos'
VSCODE_GIT_ASKPASS_EXTRA_ARGS	
'********************'
VSCODE_GIT_ASKPASS_MAIN	
'********************'
VSCODE_GIT_ASKPASS_NODE	
'********************'
VSCODE_GIT_IPC_HANDLE	
'\\\\.\\pipe\\vscode-git-0c0cf3751b-sock'
WINDIR	
'C:\\WINDOWS'
WSOS	
'NT4'
WSOSVER	
'NT4'
ZES_ENABLE_SYSMAN	
'1'
__COMPAT_LAYER	
'DetectorsAppHealth'
wsgi.errors	
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
wsgi.file_wrapper	
<class 'wsgiref.util.FileWrapper'>
wsgi.input	
<django.core.handlers.wsgi.LimitedStream object at 0x000001F91A473A30>
wsgi.multiprocess	
False
wsgi.multithread	
True
wsgi.run_once	
False
wsgi.url_scheme	
'http'
wsgi.version	
(1, 0)
Settings
Using settings module AutoMate.settings
Setting	Value
ABSOLUTE_URL_OVERRIDES	
{}
ADMINS	
[]
ALLOWED_HOSTS	
[]
APPEND_SLASH	
True
AUTHENTICATION_BACKENDS	
['django.contrib.auth.backends.ModelBackend']
AUTH_PASSWORD_VALIDATORS	
'********************'
AUTH_USER_MODEL	
'auth.User'
BASE_DIR	
WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate')
CACHES	
{'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
CACHE_MIDDLEWARE_ALIAS	
'default'
CACHE_MIDDLEWARE_KEY_PREFIX	
'********************'
CACHE_MIDDLEWARE_SECONDS	
600
CSRF_COOKIE_AGE	
31449600
CSRF_COOKIE_DOMAIN	
None
CSRF_COOKIE_HTTPONLY	
False
CSRF_COOKIE_NAME	
'csrftoken'
CSRF_COOKIE_PATH	
'/'
CSRF_COOKIE_SAMESITE	
'Lax'
CSRF_COOKIE_SECURE	
False
CSRF_FAILURE_VIEW	
'django.views.csrf.csrf_failure'
CSRF_HEADER_NAME	
'HTTP_X_CSRFTOKEN'
CSRF_TRUSTED_ORIGINS	
[]
CSRF_USE_SESSIONS	
False
DATABASES	
{'default': {'ATOMIC_REQUESTS': False,
             'AUTOCOMMIT': True,
             'CONN_HEALTH_CHECKS': False,
             'CONN_MAX_AGE': 0,
             'ENGINE': 'django.db.backends.sqlite3',
             'HOST': '',
             'NAME': WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/db.sqlite3'),
             'OPTIONS': {},
             'PASSWORD': '********************',
             'PORT': '',
             'TEST': {'CHARSET': None,
                      'COLLATION': None,
                      'MIGRATE': True,
                      'MIRROR': None,
                      'NAME': None},
             'TIME_ZONE': None,
             'USER': ''}}
DATABASE_ROUTERS	
[]
DATA_UPLOAD_MAX_MEMORY_SIZE	
2621440
DATA_UPLOAD_MAX_NUMBER_FIELDS	
1000
DATA_UPLOAD_MAX_NUMBER_FILES	
100
DATETIME_FORMAT	
'N j, Y, P'
DATETIME_INPUT_FORMATS	
['%Y-%m-%d %H:%M:%S',
 '%Y-%m-%d %H:%M:%S.%f',
 '%Y-%m-%d %H:%M',
 '%m/%d/%Y %H:%M:%S',
 '%m/%d/%Y %H:%M:%S.%f',
 '%m/%d/%Y %H:%M',
 '%m/%d/%y %H:%M:%S',
 '%m/%d/%y %H:%M:%S.%f',
 '%m/%d/%y %H:%M']
DATE_FORMAT	
'N j, Y'
DATE_INPUT_FORMATS	
['%Y-%m-%d',
 '%m/%d/%Y',
 '%m/%d/%y',
 '%b %d %Y',
 '%b %d, %Y',
 '%d %b %Y',
 '%d %b, %Y',
 '%B %d %Y',
 '%B %d, %Y',
 '%d %B %Y',
 '%d %B, %Y']
DEBUG	
True
DEBUG_PROPAGATE_EXCEPTIONS	
False
DECIMAL_SEPARATOR	
'.'
DEFAULT_AUTO_FIELD	
'django.db.models.BigAutoField'
DEFAULT_CHARSET	
'utf-8'
DEFAULT_EXCEPTION_REPORTER	
'django.views.debug.ExceptionReporter'
DEFAULT_EXCEPTION_REPORTER_FILTER	
'django.views.debug.SafeExceptionReporterFilter'
DEFAULT_FILE_STORAGE	
'django.core.files.storage.FileSystemStorage'
DEFAULT_FROM_EMAIL	
'webmaster@localhost'
DEFAULT_INDEX_TABLESPACE	
''
DEFAULT_TABLESPACE	
''
DISALLOWED_USER_AGENTS	
[]
EMAIL_BACKEND	
'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST	
'localhost'
EMAIL_HOST_PASSWORD	
'********************'
EMAIL_HOST_USER	
''
EMAIL_PORT	
25
EMAIL_SSL_CERTFILE	
None
EMAIL_SSL_KEYFILE	
'********************'
EMAIL_SUBJECT_PREFIX	
'[Django] '
EMAIL_TIMEOUT	
None
EMAIL_USE_LOCALTIME	
False
EMAIL_USE_SSL	
False
EMAIL_USE_TLS	
False
FILE_UPLOAD_DIRECTORY_PERMISSIONS	
None
FILE_UPLOAD_HANDLERS	
['django.core.files.uploadhandler.MemoryFileUploadHandler',
 'django.core.files.uploadhandler.TemporaryFileUploadHandler']
FILE_UPLOAD_MAX_MEMORY_SIZE	
2621440
FILE_UPLOAD_PERMISSIONS	
420
FILE_UPLOAD_TEMP_DIR	
None
FIRST_DAY_OF_WEEK	
0
FIXTURE_DIRS	
[]
FORCE_SCRIPT_NAME	
None
FORMAT_MODULE_PATH	
None
FORMS_URLFIELD_ASSUME_HTTPS	
False
FORM_RENDERER	
'django.forms.renderers.DjangoTemplates'
IGNORABLE_404_URLS	
[]
INSTALLED_APPS	
['django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'first_page',
 'mclogsfilter',
 'sender',
 'django_extensions',
 'certifications',
 'bookings',
 'binblocking',
 'splunkparser',
 'binblock']
INTERNAL_IPS	
[]
LANGUAGES	
[('af', 'Afrikaans'),
 ('ar', 'Arabic'),
 ('ar-dz', 'Algerian Arabic'),
 ('ast', 'Asturian'),
 ('az', 'Azerbaijani'),
 ('bg', 'Bulgarian'),
 ('be', 'Belarusian'),
 ('bn', 'Bengali'),
 ('br', 'Breton'),
 ('bs', 'Bosnian'),
 ('ca', 'Catalan'),
 ('ckb', 'Central Kurdish (Sorani)'),
 ('cs', 'Czech'),
 ('cy', 'Welsh'),
 ('da', 'Danish'),
 ('de', 'German'),
 ('dsb', 'Lower Sorbian'),
 ('el', 'Greek'),
 ('en', 'English'),
 ('en-au', 'Australian English'),
 ('en-gb', 'British English'),
 ('eo', 'Esperanto'),
 ('es', 'Spanish'),
 ('es-ar', 'Argentinian Spanish'),
 ('es-co', 'Colombian Spanish'),
 ('es-mx', 'Mexican Spanish'),
 ('es-ni', 'Nicaraguan Spanish'),
 ('es-ve', 'Venezuelan Spanish'),
 ('et', 'Estonian'),
 ('eu', 'Basque'),
 ('fa', 'Persian'),
 ('fi', 'Finnish'),
 ('fr', 'French'),
 ('fy', 'Frisian'),
 ('ga', 'Irish'),
 ('gd', 'Scottish Gaelic'),
 ('gl', 'Galician'),
 ('he', 'Hebrew'),
 ('hi', 'Hindi'),
 ('hr', 'Croatian'),
 ('hsb', 'Upper Sorbian'),
 ('hu', 'Hungarian'),
 ('hy', 'Armenian'),
 ('ia', 'Interlingua'),
 ('id', 'Indonesian'),
 ('ig', 'Igbo'),
 ('io', 'Ido'),
 ('is', 'Icelandic'),
 ('it', 'Italian'),
 ('ja', 'Japanese'),
 ('ka', 'Georgian'),
 ('kab', 'Kabyle'),
 ('kk', 'Kazakh'),
 ('km', 'Khmer'),
 ('kn', 'Kannada'),
 ('ko', 'Korean'),
 ('ky', 'Kyrgyz'),
 ('lb', 'Luxembourgish'),
 ('lt', 'Lithuanian'),
 ('lv', 'Latvian'),
 ('mk', 'Macedonian'),
 ('ml', 'Malayalam'),
 ('mn', 'Mongolian'),
 ('mr', 'Marathi'),
 ('ms', 'Malay'),
 ('my', 'Burmese'),
 ('nb', 'Norwegian Bokmål'),
 ('ne', 'Nepali'),
 ('nl', 'Dutch'),
 ('nn', 'Norwegian Nynorsk'),
 ('os', 'Ossetic'),
 ('pa', 'Punjabi'),
 ('pl', 'Polish'),
 ('pt', 'Portuguese'),
 ('pt-br', 'Brazilian Portuguese'),
 ('ro', 'Romanian'),
 ('ru', 'Russian'),
 ('sk', 'Slovak'),
 ('sl', 'Slovenian'),
 ('sq', 'Albanian'),
 ('sr', 'Serbian'),
 ('sr-latn', 'Serbian Latin'),
 ('sv', 'Swedish'),
 ('sw', 'Swahili'),
 ('ta', 'Tamil'),
 ('te', 'Telugu'),
 ('tg', 'Tajik'),
 ('th', 'Thai'),
 ('tk', 'Turkmen'),
 ('tr', 'Turkish'),
 ('tt', 'Tatar'),
 ('udm', 'Udmurt'),
 ('ug', 'Uyghur'),
 ('uk', 'Ukrainian'),
 ('ur', 'Urdu'),
 ('uz', 'Uzbek'),
 ('vi', 'Vietnamese'),
 ('zh-hans', 'Simplified Chinese'),
 ('zh-hant', 'Traditional Chinese')]
LANGUAGES_BIDI	
['he', 'ar', 'ar-dz', 'ckb', 'fa', 'ug', 'ur']
LANGUAGE_CODE	
'en-us'
LANGUAGE_COOKIE_AGE	
None
LANGUAGE_COOKIE_DOMAIN	
None
LANGUAGE_COOKIE_HTTPONLY	
False
LANGUAGE_COOKIE_NAME	
'django_language'
LANGUAGE_COOKIE_PATH	
'/'
LANGUAGE_COOKIE_SAMESITE	
None
LANGUAGE_COOKIE_SECURE	
False
LOCALE_PATHS	
[]
LOGGING	
{'disable_existing_loggers': False,
 'formatters': {'standard': {'format': '%(asctime)s [%(levelname)s] %(name)s: '
                                       '%(message)s'}},
 'handlers': {'console': {'class': 'logging.StreamHandler',
                          'formatter': 'standard',
                          'level': 'DEBUG'},
              'file': {'class': 'logging.FileHandler',
                       'filename': 'C:\\Durgesh\\Office\\Automation\\AutoMate\\AutoMate\\logs\\django.log',
                       'formatter': 'standard',
                       'level': 'DEBUG'}},
 'loggers': {'': {'handlers': ['file', 'console'],
                  'level': 'DEBUG',
                  'propagate': True}},
 'version': 1}
LOGGING_CONFIG	
'logging.config.dictConfig'
LOGIN_REDIRECT_URL	
'/accounts/profile/'
LOGIN_URL	
'/accounts/login/'
LOGOUT_REDIRECT_URL	
None
LOG_DIR	
WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/logs')
MANAGERS	
[]
MEDIA_ROOT	
''
MEDIA_URL	
'/'
MESSAGE_STORAGE	
'django.contrib.messages.storage.fallback.FallbackStorage'
MIDDLEWARE	
['django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware']
MIGRATION_MODULES	
{}
MONTH_DAY_FORMAT	
'F j'
NUMBER_GROUPING	
0
PASSWORD_HASHERS	
'********************'
PASSWORD_RESET_TIMEOUT	
'********************'
PREPEND_WWW	
False
ROOT_URLCONF	
'AutoMate.urls'
SECRET_KEY	
'********************'
SECRET_KEY_FALLBACKS	
'********************'
SECURE_CONTENT_TYPE_NOSNIFF	
True
SECURE_CROSS_ORIGIN_OPENER_POLICY	
'same-origin'
SECURE_HSTS_INCLUDE_SUBDOMAINS	
False
SECURE_HSTS_PRELOAD	
False
SECURE_HSTS_SECONDS	
0
SECURE_PROXY_SSL_HEADER	
None
SECURE_REDIRECT_EXEMPT	
[]
SECURE_REFERRER_POLICY	
'same-origin'
SECURE_SSL_HOST	
None
SECURE_SSL_REDIRECT	
False
SERVER_EMAIL	
'root@localhost'
SESSION_CACHE_ALIAS	
'default'
SESSION_COOKIE_AGE	
1209600
SESSION_COOKIE_DOMAIN	
None
SESSION_COOKIE_HTTPONLY	
True
SESSION_COOKIE_NAME	
'sessionid'
SESSION_COOKIE_PATH	
'/'
SESSION_COOKIE_SAMESITE	
'Lax'
SESSION_COOKIE_SECURE	
False
SESSION_ENGINE	
'django.contrib.sessions.backends.db'
SESSION_EXPIRE_AT_BROWSER_CLOSE	
False
SESSION_FILE_PATH	
None
SESSION_SAVE_EVERY_REQUEST	
False
SESSION_SERIALIZER	
'django.contrib.sessions.serializers.JSONSerializer'
SETTINGS_MODULE	
'AutoMate.settings'
SHORT_DATETIME_FORMAT	
'm/d/Y P'
SHORT_DATE_FORMAT	
'm/d/Y'
SIGNING_BACKEND	
'django.core.signing.TimestampSigner'
SILENCED_SYSTEM_CHECKS	
[]
STATICFILES_DIRS	
[WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/first_page/static'),
 WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/mclogsfilter/static'),
 WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/sender/static'),
 WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/bookings/static'),
 WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/bookings/static'),
 WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/binblocking/static'),
 WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/splunkparser/static'),
 WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/binblock/static')]
STATICFILES_FINDERS	
['django.contrib.staticfiles.finders.FileSystemFinder',
 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
STATICFILES_STORAGE	
'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_ROOT	
WindowsPath('C:/Durgesh/Office/Automation/AutoMate/AutoMate/staticfiles')
STATIC_URL	
'/static/'
STORAGES	
{'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
 'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'}}
TEMPLATES	
[{'APP_DIRS': True,
  'BACKEND': 'django.template.backends.django.DjangoTemplates',
  'DIRS': ['C:\\Durgesh\\Office\\Automation\\AutoMate\\AutoMate\\html'],
  'OPTIONS': {'context_processors': ['django.template.context_processors.debug',
                                     'django.template.context_processors.request',
                                     'django.contrib.auth.context_processors.auth',
                                     'django.contrib.messages.context_processors.messages']}}]
TEST_NON_SERIALIZED_APPS	
[]
TEST_RUNNER	
'django.test.runner.DiscoverRunner'
THOUSAND_SEPARATOR	
','
TIME_FORMAT	
'P'
TIME_INPUT_FORMATS	
['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']
TIME_ZONE	
'UTC'
USE_I18N	
True
USE_THOUSAND_SEPARATOR	
False
USE_TZ	
True
USE_X_FORWARDED_HOST	
False
USE_X_FORWARDED_PORT	
False
WSGI_APPLICATION	
'AutoMate.wsgi.application'
X_FRAME_OPTIONS	
'DENY'
YEAR_MONTH_FORMAT	
'F Y'
You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard page generated by the handler for this status code.
