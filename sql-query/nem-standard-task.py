#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys
import os
import MySQLdb
import datetime
import xlrd
import random
from mysql import connector

reload(sys)
sys.setdefaultencoding('utf8')


class MySQL(object):
    """
    使用方法：

    >>> with MySQL('xvirt') as db:
    >>>     sql = 'select * from instances;'
    >>>     db.execute(sql)
    >>>     for a in db:
    >>>         print a
    """

    def __init__(self, database):
        self.conn = connector.connect(host="nem.fxdata.cn",
                                      user="root1",
                                      passwd="jyUh3Op23zPZF4z9nqj",
                                      database=database,
                                      buffered=True)

    def __enter__(self):
        self.cursor = self.conn.cursor(dictionary=True)
        return self.cursor

    def __exit__(self, *exc):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def get_business_task(name):
    tasks = [{"b_id": 1, "task_id": 4, "name": u"Science"},
             {"b_id": 1, "task_id": 5, "name": u"PNAS"},
             {"b_id": 1, "task_id": 6, "name": u"SAGE"},
             {"b_id": 2, "task_id": 7, "name": u"CNKI"},
             {"b_id": 2, "task_id": 8, "name": u"万方数据"},
             {"b_id": 2, "task_id": 9, "name": u"北大法宝"},
             {"b_id": 3, "task_id": 10, "name": u"中国大学MOOC"},
             {"b_id": 3, "task_id": 11, "name": u"超星慕课"},
             {"b_id": 3, "task_id": 12, "name": u"学堂在线"},
             {"b_id": 4, "task_id": 13, "name": u"新浪"},
             {"b_id": 4, "task_id": 14, "name": u"网易"},
             {"b_id": 4, "task_id": 15, "name": u"凤凰网"},
             {"b_id": 5, "task_id": 16, "name": u"Windows更新"},
             {"b_id": 5, "task_id": 17, "name": u"Android更新"},
             {"b_id": 6, "task_id": 1, "name": u"腾讯"},
             {"b_id": 6, "task_id": 2, "name": u"爱奇艺"},
             {"b_id": 6, "task_id": 3, "name": u"优酷"},
             {"b_id": 7, "task_id": 18, "name": u"京东"},
             {"b_id": 7, "task_id": 19, "name": u"天猫"},
             {"b_id": 7, "task_id": 20, "name": u"淘宝"}]
    for task in tasks:
        if task["name"] in name:
            return (task["b_id"], task["task_id"])
    return 0


def generate_licence(num):
    """
    生成num位字母和数字的随机字符串
    :param num: 生成字符串位数
    :return: string
    """
    s = ""
    for i in range(num):
        n = random.randint(1, 2)  # n=1生成数字, n=2生成字母
        if n == 1:
            s += str(random.randint(0, 9))
        else:
            s += chr(96 + random.randint(1, 26))

    return s


def write_log(custom_name, msg):
    filename = "nem_创建任务_" + custom_name + ".sql"
    f = open(filename, "a")
    f.write(msg)
    f.close


def get_probe_id(probe_sn):
    with MySQL('nem') as db:
        sql = 'select id,probe_sn from probes '
        db.execute(sql)
        probe_infos = db.fetchall()
        for probe_info in probe_infos:
            if probe_sn == probe_info["probe_sn"]:
                probe_id = probe_info["id"]
        return probe_id


def convert_custom_standard(debug=False):
    count = 0
    nowtime = datetime.datetime.now() + datetime.timedelta(hours=-24)
    create_time = nowtime.strftime("%Y-%m-%d %H:%M:%S")
    with MySQL('nem') as db:
        sql = 'select * from custom_tasks where create_time >"%s" order by id' % create_time
        db.execute(sql)
        results = db.fetchall()
        for result in results:
            id_ = result['id']
            fx_task_id = result['fx_task_id']
            task_id = result['task_id']
            period = result['period']
            fx_task_type = result['fx_task_type']
            task_type = result['task_type']
            create_time = result['create_time']
            update_time = result['update_time']
            name = result['name']
            url = result['url']
            start_time = result['start_time']
            end_time = result['end_time']
            interval = result['interval']
            event_time = result['event_time']
            event_id = result['event_id']
            enable = result['enable']
            status = result['status']
            sync = result['sync']
            deleted = result['deleted']
            probe_app_id = result['probe_app_id']
            probe_app_type = result['probe_app_type']
            probe_sn = result['probe_sn']
            probe_id = get_probe_id(probe_sn)
            node_id = result['node_id']
            node_sn = result['node_sn']
            if not get_business_task(name):
                print name + " is not a standard task"
                continue
            business_task = get_business_task(name)
            business_id = business_task[0]
            task_cfg_id = business_task[1]

            ret = {}
            ret["id"] = id_
            ret["fx_task_id"] = fx_task_id
            ret["task_id"] = task_id
            ret["fx_task_type"] = fx_task_type
            ret["task_type"] = task_type
            ret["create_time"] = create_time
            ret["update_time"] = update_time
            ret["name"] = name
            ret["url"] = url
            ret["start_time"] = start_time
            ret["end_time"] = end_time
            ret["interval"] = interval
            ret["event_time"] = event_time
            ret["event_id"] = event_id
            ret["enable"] = 1
            ret["status"] = status
            ret["sync"] = sync
            ret["deleted"] = deleted
            ret["task_cfg_id"] = task_cfg_id
            ret["business_id"] = business_id
            ret["probe_id"] = probe_id
            ret["probe_app_id"] = probe_app_id
            ret["probe_app_type"] = probe_app_type
            ret["probe_sn"] = probe_sn
            ret["node_id"] = node_id
            ret["node_sn"] = node_sn

            # sql = "insert into standard_tasks (`id`,`fx_task_id`,`task_id`,`fx_task_type`,`task_type`,`create_time`,`update_time`,`name`,`url`,`start_time`,`end_time`,`interval`,`event_time`,`event_id`,`enable`,`status`,`sync`,`deleted`,`task_cfg_id`,`business_id`,`probe_id`,`probe_app_id`,`probe_app_type`,`probe_sn`,`node_id`,`node_sn`) values (%d,%d,'%s',%d,%d,'%s','%s','%s','%s','%s','%s',%d,'%s',%d,%d,%d,%d,%d,%d,%d,%d,'%s','%s','%s',%d,'%s')" % (
            #     id, fx_task_id, task_id, fx_task_type, task_type, create_time, update_time, name, url, start_time,
            #     end_time,
            #     interval, event_time, event_id, enable, status, sync, deleted, task_cfg_id, business_id, probe_id,
            #     probe_app_id, probe_app_type, probe_sn, node_id, node_sn)
            sanitied_ret = sanity_dict(ret)
            sql = composed_sql("standard_tasks", sanitied_ret)
            count += 1
            if debug:
                print sql
            else:
                db.execute(sql)
    print count


def sanity_dict(d):
    sanitied_dict = {}
    for k, v in d.iteritems():
        if v is not None:
            sanitied_dict[k] = v
    return sanitied_dict


def sanity_int_list(l):
    sanitied_list = []
    for i in l:
        if i != "":
            try:
                i = int(i)
                sanitied_list.append(i)
            except:
                sanitied_list.append(i)
    return sanitied_list


def composed_sql(sql_table, d):
    base_sql = """INSERT INTO %(sql_table)s (%(fields)s) VALUES (%(values)s);"""
    fields = ",".join([quote_add(k) for k in d.keys()])
    values = ",".join([quote_add(convert_value(v), "'") for v in d.values()])
    try:
        sql_table = "`" + sql_table.split(".")[0] + "`.`" + \
                    sql_table.split(".")[1] + "`"
    except:
        sql_table = "`" + sql_table + "`"
    return base_sql % {"sql_table": sql_table, "fields": fields,
                       "values": values}


def distinct_list(l):
    distinct_list = []
    for i in l:
        if i not in distinct_list:
            distinct_list.append(i)
    return distinct_list


def create_dict(items):
    dict = {}
    print items
    for item in items:
        for itemx, itemy in locals().items():
            if item == itemy and itemx != 'item':
                dict[itemx] = itemy
    print dict
    return dict


def convert_value(value):
    try:
        return str(value)
    except:
        return value


def quote_add(item, symbol="`"):
    return symbol + item + symbol


def get_probe_and_task(node_id):
    with MySQL('nem') as db:
        sql = "select `id`,`name`,`probe_sn` from custom_tasks where enable=1 and node_id='%s' order by id" % node_id
        db.execute(sql)
        custom_results = db.fetchall()
        sql = "select `id`,`name`,`probe_sn` from standard_tasks where enable=1 and node_id='%s' order by id" % node_id
        db.execute(sql)
        standard_results = db.fetchall()
        results = custom_results + standard_results
        return results


def get_task_type(btype):
    if btype == "web":
        return (3, 2, "first_screen_time")
    elif btype == "media":
        return (6, 1, "request_time")
    elif btype == "download":
        return (4, 3, "speed_download")
    else:
        return False


def excel_read(custom_name):
    workbook = xlrd.open_workbook('./tingyun_task.xlsx')
    sh = workbook.sheet_by_name(custom_name)
    customer_hid = sanity_int_list(sh.col_values(0))[1:]
    hid = sanity_int_list(sh.col_values(1))[1:]
    nemid = sanity_int_list(sh.col_values(2))[1:]
    probe_sn = sanity_int_list(sh.col_values(3))[1:]
    typrobeid = sanity_int_list(sh.col_values(4))[1:]
    probe_id = sanity_int_list(sh.col_values(5))[1:]
    probe_name = sanity_int_list(sh.col_values(6))[1:]
    region_id = sanity_int_list(sh.col_values(7))[1:]
    region_name = sanity_int_list(sh.col_values(8))[1:]
    btype = sanity_int_list(sh.col_values(9))[1:]
    task = sanity_int_list(sh.col_values(10))[1:]
    url = sanity_int_list(sh.col_values(11))[1:]
    node_id = int(nemid[2].split('0000')[1])
    return {"customer_hid": customer_hid, "hid": hid, "nemid": nemid,
            "probe_sn": probe_sn, "typrobeid": typrobeid, "probe_id": probe_id,
            "probe_name": probe_name, "region_id": region_id,
            "region_name": region_name, "btype": btype, "task": task,
            "url": url, "node_id": node_id}


def create_all(custom_name):
    nowtime = datetime.datetime.now()
    exptime = datetime.datetime.now() + datetime.timedelta(days=365)
    created_at = nowtime.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at
    expire_time = exptime.strftime("%Y-%m-%d %H:%M:%S")
    tuple_info = excel_read(custom_name)
    hid = tuple_info["hid"][0]
    name = custom_name + "NEM节点"
    licence = generate_licence(16)
    major_alliance = "1"
    customer_name = custom_name
    customer_hid = tuple_info["customer_hid"][0]
    sn = tuple_info["nemid"][0]
    deleted = "0"
    node_id = tuple_info["node_id"]
    region_name = tuple_info["region_name"]
    region_id = tuple_info["region_id"]
    probe_sn = tuple_info["probe_sn"]
    typrobeid = tuple_info["typrobeid"]
    probe_id = tuple_info["probe_id"]
    probe_name = tuple_info["probe_name"]
    btype = tuple_info["btype"]
    task = tuple_info["task"]
    url = tuple_info["url"]

    if "自定义任务" in custom_name:
        msg1 = ("###创建自定义业务\n")
        write_log(custom_name, msg1)
        ret = {}
        ret["id"] = 8
        ret["create_time"] = created_at
        ret["update_time"] = updated_at
        ret["name"] = custom_name.strip("自定义任务") + "校内业务"
        length = len(btype)
        for i in range(length):
            if btype[i] != "web":
                print "存在多种业务类型，需要人工介入创建不同的业务和任务"
                exit(1)
        ret["icon"] = get_task_type("web")[1]
        ret["task_type"] = get_task_type("web")[0]
        ret["metric_name"] = get_task_type("web")[2]
        ret["deleted"] = 0
        sql = composed_sql("xedge.nem_business", ret)
        msg2 = sql + "\n"
        write_log(custom_name, msg2)
        write_log(custom_name, '\n')

    if "自定义任务" in custom_name:
        msg1 = ("###创建自定义任务\n")
        write_log(custom_name, msg1)
        ret = {}
        length = len(task)
        for i in range(length):
            ret["id"] = 21 + i
            ret["create_time"] = created_at
            ret["update_time"] = updated_at
            ret["name"] = task[i]
            ret["url"] = url[i]
            ret["url_type"] = 1
            ret["enable"] = 1
            ret["interval"] = 300
            if not get_task_type(btype[i]):
                print "wrong btype! 请填写正确的类型"
                exit(2)
            ret["task_type"] = get_task_type(btype[i])[0]
            ret["deleted"] = 0
            ret["business_id"] = 8
            ret["status"] = 0
            ret["sync"] = 1
            sql = composed_sql("xedge.nem_task", ret)
            msg2 = sql + "\n"
            write_log(custom_name, msg2)
        write_log(custom_name, '\n')

    ret = {}
    ret["created_at"] = created_at
    ret["updated_at"] = updated_at
    ret["expire_time"] = expire_time
    ret["hid"] = hid
    ret["name"] = name
    ret["licence"] = licence
    ret["major_alliance"] = major_alliance
    ret["customer_name"] = customer_name
    ret["customer_hid"] = customer_hid
    ret["sn"] = sn
    ret["deleted"] = deleted
    sql = composed_sql("nem.nodes", ret)
    # sql = "insert into nem.nodes (`created_at`, `updated_at`, `hid`, `name`, `licence`, `expire_time`, `major_alliance`, `customer_name`, `customer_hid`, `sn`, `deleted`) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
    #     created_at, updated_at, hid, name, licence, expire_time,
    #     major_alliance, customer_name, customer_hid
    #     , sn, deleted)
    msg1 = ("###以下为云端node创建命令\n")
    msg2 = sql + "\n\n"
    write_log(custom_name, msg1)
    write_log(custom_name, msg2)

    ret = {}
    ret["id"] = 1
    ret["created_time"] = created_at
    ret["updated_time"] = updated_at
    ret["hid"] = hid
    ret["name"] = name
    ret["licence"] = licence
    ret["expire_time"] = expire_time
    ret["customer_name"] = customer_name
    ret["customer_hid"] = customer_hid
    ret["sn"] = sn
    sql = composed_sql("xedge.nem_node", ret)
    msg1 = "###以下为CDS端node创建命令\n"
    msg2 = sql + "\n\n"
    write_log(custom_name, msg1)
    write_log(custom_name, msg2)

    ret = {}
    ret["created_at"] = created_at
    ret["updated_at"] = updated_at
    ret["node_id"] = node_id
    ret["node_name"] = name
    ret["deleted"] = deleted
    length = len(region_name)
    msg1 = "###以下为云端region创建命令\n"
    write_log(custom_name, msg1)
    for i in range(length):
        ret["name"] = region_name[i]
        sql = composed_sql("nem.regions", ret)
        msg2 = sql + "\n"
        write_log(custom_name, msg2)
    write_log(custom_name, "\n")

    ret = {}
    ret["create_time"] = created_at
    ret["update_time"] = updated_at
    length = len(region_name)
    msg1 = "###以下为CDS端region创建命令\n"
    write_log(custom_name, msg1)
    msg2 = "truncate xedge.nem_region;\n"
    write_log(custom_name, msg2)
    list_d = []
    for i in range(length):
        ret["id"] = region_id[i]
        if region_id[i] not in list_d:
            list_d.append(region_id[i])
            ret["name"] = region_name[i]
            sql = composed_sql("xedge.nem_region", ret)
            msg2 = sql + "\n"
            write_log(custom_name, msg2)
    write_log(custom_name, "\n")

    ret = {}
    ret["create_time"] = created_at
    ret["update_time"] = updated_at
    ret["probe_type"] = "pc"
    ret["deleted"] = 0
    ret["node_id"] = node_id
    length = len(probe_sn)
    msg1 = "###以下为云端probe创建命令\n"
    write_log(custom_name, msg1)
    for i in range(length):
        ret["licence"] = generate_licence(16)
        ret["probe_sn"] = probe_sn[i]
        ret["region_id"] = region_id[i]
        ret[
            "app"] = '[{"group_id": "", "type": "TY", "id": "%s", "name": "听云APP"}]' % \
                     typrobeid[i]
        sql = composed_sql("nem.probes", ret)
        msg2 = sql + "\n"
        write_log(custom_name, msg2)
    write_log(custom_name, "\n")

    ret = {}
    ret["create_time"] = created_at
    ret["update_time"] = updated_at
    ret["ptype"] = 1
    ret["enable"] = 1
    ret["active"] = 1
    length = len(probe_sn)
    msg1 = "###以下为CDS端probe创建命令\n"
    write_log(custom_name, msg1)
    msg2 = "truncate xedge.nem_probe;\n"
    write_log(custom_name, msg2)
    for i in range(length):
        ret["id"] = probe_id[i]
        ret["probe_sn"] = probe_sn[i]
        ret["name"] = probe_name[i]
        ret["region_id"] = region_id[i]
        sql = composed_sql("xedge.nem_probe", ret)
        msg2 = sql + "\n"
        write_log(custom_name, msg2)
    write_log(custom_name, "\n")


def cds_probe_and_task_insert(custom_name):
    tuple_info = excel_read(custom_name)
    node_id = tuple_info["node_id"]
    cds_probe_sn = tuple_info["probe_sn"]
    cds_probe_id = tuple_info["probe_id"]
    results = get_probe_and_task(node_id)
    write_log(custom_name, "###以下为probe_and_task sql信息\n")
    for result in results:
        id_ = int(result["id"])
        probe_sn = result["probe_sn"]
        task_name = result["name"].split("_")[2]
        probe_sn_index = cds_probe_sn.index(probe_sn)
        probe_id = int(cds_probe_id[probe_sn_index])
        task_id = int(get_business_task(task_name)[1])
        ret = {}
        ret["probe_id"] = probe_id
        ret["task_id"] = task_id
        ret["probe_task_id"] = id_
        sql = composed_sql("xedge.nem_node", ret)
        write_log(custom_name, sql + "\n")
    write_log(custom_name, "\n")


def init_files(custom_name):
    filename = "nem_创建任务_" + custom_name + ".sql"
    cmd = "cp standard_task.sql " + filename
    os.system(cmd)


if __name__ == '__main__':
    custom_name = u"北京交通大学自定义任务"

    # ####自定义任务转标准任务,需要先手动关闭原任务####
    # convert_custom_standard(debug=True)

    # ####生成sql命令#####
    init_files(custom_name)
    create_all(custom_name)
    # cds_probe_and_task_insert(custom_name)
