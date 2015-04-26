import time
import datetime

from ceilometerclient import client as ceilometer_client


cclient = ceilometer_client.get_client('2', os_username='admin', os_password='Pas@123a', os_tenant_name='admin',
                                             os_auth_url='http://10.10.1.100:35357/v2.0',os_endpoint_type='internalURL')
query = [dict(field='resource_id', op='eq', value='456777b2-a953-4348-97d0-01804dab08fc')]

'''
6 hours:5 mins
1 day:  15mins
1 week: 2 hours
1 month:6 hours
0.5year:1 day

ceilometer sample-list -m cpu_util -l 10 -q resource=
.sam
'''
class APIResourceWrapper(object):
    """Simple wrapper for api objects.

    Define _attrs on the child class and pass in the
    api object as the only argument to the constructor
    """
    _attrs = []
    _apiresource = None  # Make sure _apiresource is there even in __init__.

    def __init__(self, apiresource):
        self._apiresource = apiresource

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            if attr not in self._attrs:
                raise
            # __getattr__ won't find properties
            return getattr(self._apiresource, attr)

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__,
                             dict((attr, getattr(self, attr))
                                  for attr in self._attrs
                                  if hasattr(self, attr)))


class Meter(APIResourceWrapper):
    """Represents one Ceilometer meter."""
    _attrs = ['name', 'type', 'unit', 'resource_id', 'user_id',
              'project_id']

    def __init__(self, apiresource):
        super(Meter, self).__init__(apiresource)

        self._label = self.name
        self._description = ""

    def augment(self, label=None, description=None):
        if label:
            self._label = label
        if description:
            self._description = description

    @property
    def description(self):
        return self._description

    @property
    def label(self):
        return self._label


class Sample(APIResourceWrapper):
    """Represents one Ceilometer sample."""

    _attrs = ['counter_name', 'user_id', 'resource_id', 'timestamp',
              'resource_metadata', 'source', 'counter_unit', 'counter_volume',
              'project_id', 'counter_type', 'resource_metadata']

    @property
    def instance(self):
        display_name = self.resource_metadata.get('display_name', None)
        instance_id = self.resource_metadata.get('instance_id', None)
        return display_name or instance_id

    @property
    def name(self):
        name = self.resource_metadata.get("name", None)
        display_name = self.resource_metadata.get("display_name", None)
        return name or display_name or ""


class Statistic(APIResourceWrapper):
    """Represents one Ceilometer statistic."""

    _attrs = ['period', 'period_start', 'period_end',
              'count', 'min', 'max', 'sum', 'avg',
              'duration', 'duration_start', 'duration_end']


def print_list(obj_list):
    for i in obj_list:
        print i.__dict__
    print('lenght is :%d\n'%len(obj_list))

def meter_list():
    meters=cclient.meters.list()
    print_list([Meter(m) for m in meters])
    '''
    <Meter {
        'user_id': u'4ddf86fc2b1643a9967980cfb4c48398',
        'name': u'port.create',
        'resource_id': u'b9200a4f-ec82-495e-8e95-9baa2719110e',
        'source': u'openstack',
        'meter_id': u'YjkyMDBhNGYtZWM4Mi00OTVlLThlOTUtOWJhYTI3MTkxMTBlK3BvcnQuY3JlYXRl\n',
        'project_id': u'e8da2da1c811464bbb73d834049f032a',
        'type': u'delta',
        'unit': u'port'}>
    '''


def sample_list(meter=None):
    samples=cclient.samples.list(meter_name=meter,q=query)
    print_list([Sample(s) for s in samples])
    '''
    meter=None
    <Sample: {
        'source': u'openstack',
        'project_id': u'e8da2da1c811464bbb73d834049f032a',
        'user_id': u'4ddf86fc2b1643a9967980cfb4c48398',
        'resource_id': u'b9200a4f-ec82-495e-8e95-9baa2719110e'}>

    meter=cpu_util
    <Sample: {
        'counter_name': u'cpu_util',
        'user_id': u'4ddf86fc2b1643a9967980cfb4c48398',
        'resource_id': u'02b70f8d-0913-4d08-9fe6-0bc6f83b285a',
        'timestamp': u'2015-02-07T02:45:58',
        'source': u'openstack',
        'counter_unit': u'%',
        'counter_volume': 0.19,
        'project_id': u'e8da2da1c811464bbb73d834049f032a',
        'resource_metadata': {
                u'ramdisk_id': u'None',
                u'flavor.vcpus': u'1',
                u'flavor.ephemeral': u'0',
                u'display_name': u'chenxuewei-006',
                u'flavor.id': u'81b973b8-3f09-4cb0-a536-afceff5f5a46',
                u'ephemeral_gb': u'0',
                u'flavor.name': u'm1.small',
                u'disk_gb': u'45',
                u'kernel_id': u'None',
                u'image.id': u'3cd21cbb-0a00-4e2e-b012-6fab4ca5cec8',
                u'flavor.ram': u'2048',
                u'host': u'b20003b764507711c67912698328b45dab3f84bb3b624296b327ec05',
                u'OS-EXT-AZ.availability_zone': u'nova-vsan',
                u'image.name': u'centos',
                u'image_ref_url': u'http://10.10.1.100:8774/1f3b0c2d26ae4e45892f76619bedcc77/
                    images/3cd21cbb-0a00-4e2e-b012-6fab4ca5cec8',
                u'image.links': u'["{
                    u\'href\': u\'http://10.10.1.100:8774/1f3b0c2d26ae4e45892f76619bedcc77/images/
                                3cd21cbb-0a00-4e2e-b012-6fab4ca5cec8\',
                    u\'rel\': u\'bookmark\'}"]',
                u'flavor.disk': u'45',
                u'root_gb': u'45',
                u'name': u'instance-00000011',
                u'memory_mb': u'2048',
                u'instance_type': u'81b973b8-3f09-4cb0-a536-afceff5f5a46',
                u'vcpus': u'1',
                u'image_ref': u'3cd21cbb-0a00-4e2e-b012-6fab4ca5cec8',
                u'flavor.links': u'["{
                    u\'href\': u\'http://10.10.1.100:8774/1f3b0c2d26ae4e45892f76619bedcc77/flavors/
                                81b973b8-3f09-4cb0-a536-afceff5f5a46\',
                    u\'rel\': u\'bookmark\'}"]'
        },
        'counter_type': u'gauge'}>

    '''

def statistic_list(meter_name, query=None, period=None):
    """List of statistics."""
    query={}
    statistics = cclient.statistics.list(meter_name=meter_name, q=query, period=period)
    return [Statistic(s) for s in statistics]


if __name__=='__main__':
    #meter_list()
    #sample_list('cpu_util')
    print datetime.datetime.utcnow()
    print time.time()
