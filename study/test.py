from __future__ import division
from pprint import pprint
from collections import defaultdict
from influxdb import InfluxDBClient

def json_body_create(dict_p):
	json_body=[
	{
	"measurement":"df_value_bk",
	"tags":{
	"host":dict_p['host'],
	"type":dict_p['type'],
	"instance":dict_p['instance'],
	"type_instance":dict_p['type_instance']
	},
	"time":dict_p['time'],
	"fields":{
	"percent":str(dict_p['percent']),
	"value":str(dict_p['value'])
	}
	}
	]
	return json_body

inf = InfluxDBClient('30.30.32.4', database='collectd')

iql = '''
select
    sum(value) as val_inst_one_min
from
    df_value
where
    time > now() - 5m
group by
    time(1m),
    instance
'''

ret = inf.query(iql)

search_map = defaultdict(dict)
for key in ret.keys():
    for p in ret.get_points(tags=key[1]):
        search_map[key[1]['instance']][p['time']] = p['val_inst_one_min']


iql_1 = '''
select
    *
from
    df_value
where
    time < now() - 1m
    and
    time > now() - 5m
'''

ret1 = inf.query(iql_1)

for p in ret1.get_points():
    try:
        p['percent'] = p['value'] / search_map[p['instance']][p['time'][:17] + '00Z']
        p['time']=p['time'].split('.')[0]+'Z'
    except Exception:
        continue
    #pprint(p)
    json_body=json_body_create(p)
    print '#####################'
    print json_body
    #inf.write_points(json_body)
