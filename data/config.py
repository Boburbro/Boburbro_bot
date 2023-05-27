from environs import Env
env = Env()
env.read_env()

# OWNER=12345678
# ADMINS=12345678,12345677,12345676
# CHANELS=-123456789
# GRUPS=-1234566789
# BOT_TOKEN=123452345243:Asdfasdfasf
# ip=localhost

ADMINS=env.list("ADMINS")
BOT_TOKEN=env.str("BOT_TOKEN")
ip=env.str("ip")
