import getopt
import pprint
import sys

from config import ConfigHandler
from single_instance import SingleInstance
import redis_cli

config_file = ''

def help():
    print "main.py -c <config file>"


def arg_check():
    global config_file

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:", ["cfile="])

        if len(opts) < 1:
            raise getopt.GetoptError("Require Agument")

        for opt, arg in opts:
            if opt == '-h':
                help()
            elif opt in ("-c", "--cfile"):
                config_file = arg
            else:
                raise getopt.GetoptError("Wrong Agument")

    except getopt.GetoptError:
        help()
        sys.exit(2)


def initialization():
    config = SingleInstance.get('config')

    addr = config["redis"]["addr"]
    port = config["redis"]["port"]
    auth = config["redis"]["auth"]
    db   = config["redis"]["db"]

    redis = redis_cli.RedisCli(addr, port, auth, db)
    redis = redis.connection()

    SingleInstance.set('redis', redis)


def main():
    arg_check()

    parser = ConfigHandler(config_file)
    config = parser.read_config()
    pprint.pprint(config)

    SingleInstance.set('config', config)

    initialization()



if __name__ == "__main__":
    main()
