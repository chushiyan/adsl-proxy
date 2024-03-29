# coding=utf-8
# 拨号间隔
ADSL_CYCLE = 420

# 拨号出错重试间隔
ADSL_ERROR_CYCLE = 10

# ADSL命令
ADSL_BASH = 'adsl-stop;adsl-start'

# 代理运行端口
PROXY_PORT = 8888

# 客户端唯一标识
CLIENT_NAME = 'adsl09'

# 拨号网卡
ADSL_IFNAME = 'ppp0'

# Redis数据库IP
REDIS_HOST = '127.0.0.1'

# Redis数据库密码, 如无则填None
REDIS_PASSWORD = None

# Redis数据库端口
REDIS_PORT = 6379

# 代理池键名
PROXY_KEY = 'adsl'

# 测试URL
TEST_URL = 'https://www.baidu.com'

# 测试超时时间
TEST_TIMEOUT = 6

# API端口
API_PORT = 8000
