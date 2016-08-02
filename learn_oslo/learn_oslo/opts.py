__author__ = 'evan'
from oslo_config import cfg
import learn_oslo.cmd.api as api


def list_opts():
    return[('DEFAULT', api.apilog_opts),
           (api.api_opts_group, api.api_opts),
           (api.mongo_opts_group, api.mongo_opts)]


opts1 = [
    cfg.StrOpt('foo'),
    cfg.StrOpt('bar'),
]

opts2 = [
    cfg.StrOpt('baz'),
]

baz_group = cfg.OptGroup(name='baz_group',
                         title='Baz group options',
                         help=u'Baz group help text')
cfg.CONF.register_group(baz_group)

cfg.CONF.register_opts(opts1, group='blaa')
cfg.CONF.register_opts(opts2, group=baz_group)

# def list_opts():
#     # Allows the generation of the help text for
#     # the baz_group OptGroup object. No help
#     # text is generated for the 'blaa' group.
#     return [('blaa', opts1), (baz_group, opts2)]


if __name__ == '__main__':
    print(list_opts())
