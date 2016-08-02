__author__ = 'evan'
import sys

from oslo_config import cfg
from oslo_log import log as logging


api_opts = [
        cfg.ListOpt('a',
                    default=['default'],
                    help='help a'),
        cfg.ListOpt('b',
                    default=['default'],
                    help='help b'),
        cfg.StrOpt('apilog2',
                   default='default',
                   help='help c')
]
api_opts_group = cfg.OptGroup(name='api', title='API v1 Options')

apilog_opts = [
    cfg.StrOpt('apilog',
                default='default',
                help='help c')
]

mongo_opts = [
    # cfg.StrOpt('db',
    #            default='learn_oslo',
    #            help='help c'),
    # cfg.StrOpt('username',
    #            default='default',
    #            help='help c'),
    # cfg.StrOpt('password',
    #            default='default',
    #            help='help c'),
    cfg.StrOpt('host',
               default='mongodb://learn_oslo:RM_DBPASS@30.161.221.245/learn_oslo',
               help='help c'),
    cfg.IntOpt('port',
               default=27017,
               help='help c')
]
mongo_opts_group= cfg.OptGroup(name='mongo', title='mongo connection')

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
PROG = 'learn_oslo-api'
CONF.register_group(api_opts_group)
CONF.register_group(mongo_opts_group)
CONF.register_opts(api_opts, api_opts_group)
CONF.register_opts(mongo_opts, mongo_opts_group)
CONF.register_opts(apilog_opts)





def main():
    # prepare(cfg.CONF)
    logging.register_options(CONF)
    # extra_log_level_defaults = [
    #     'requests=INFO',
    #     'mongoengin=INFO'
    #     ]
    #
    # logging.set_defaults(
    #     default_log_levels=logging.get_default_log_levels() +
    #     extra_log_level_defaults)

    CONF(project='learn_oslo', prog=PROG)

    logging.setup(CONF, PROG)
    logging.set_defaults()
    for i in cfg.CONF:
        if i in ['api', 'mongo']:
            group = getattr(cfg.CONF, i)
            for j in group:
                LOG.info('{0} = {1}'.format(j, getattr(group, j)))
        LOG.info('{0} = {1}'.format(i, getattr(cfg.CONF, i)))


if __name__ == '__main__':
    sys.exit(main())