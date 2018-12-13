# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, BigInteger, DATETIME
from sqlalchemy.orm import sessionmaker
import os
import xlrd

# 创建数据库vpec
cmd = "mysql -e 'CREATE DATABASE IF NOT EXISTS `vpec` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;'"
os.system(cmd)

engine = create_engine("mysql+mysqldb://root@localhost:3306/vpec")
Base = declarative_base()


class Ipservice(Base):
    __tablename__ = "ip_service"
    sn = Column(String(13), primary_key=True)
    date = Column(DATETIME, primary_key=True)
    http_ip = Column(Integer)
    demand_ip = Column(Integer)
    live_ip = Column(Integer)
    all_ip = Column(Integer)
    http_service = Column(BigInteger)
    demand_service = Column(BigInteger)
    live_service = Column(BigInteger)
    http_cache = Column(BigInteger)
    demand_cache = Column(BigInteger)
    live_cache = Column(BigInteger)


# 若无数据表则新建，有则不会更新
Base.metadata.create_all(engine)
# 建立会话
DBSession = sessionmaker(bind=engine)
session = DBSession()

workbook = xlrd.open_workbook("test.xlsx")
sheet = workbook.sheet_by_name("test")

index_list = sheet.row_values(0)
sn_index = index_list.index("SN")
date_index = index_list.index("date")
http_ip_index = index_list.index("cnc_http_ip_sum")
demand_ip_index = index_list.index("cnc_demand_ip_sum")
live_ip_index = index_list.index("cnc_live_ip_sum")
all_ip_index = index_list.index("all_ip")
http_service_index = index_list.index("server_16")
demand_service_index = index_list.index("server_14")
live_service_index = index_list.index("server_15")
http_cache_index = index_list.index("cache_16")
demand_cache_index = index_list.index("cache_14")
live_cache_index = index_list.index("cache_15")

nrows = sheet.nrows
for row in range(1, nrows):
    row_values = sheet.row_values(row)
    sn = row_values[sn_index]
    date = xlrd.xldate.xldate_as_datetime(sheet.cell(row, date_index).value, 0)
    http_ip = int(row_values[http_ip_index])
    demand_ip = int(row_values[demand_ip_index])
    live_ip = int(row_values[live_ip_index])
    all_ip = int(row_values[all_ip_index])
    http_service = int(row_values[http_service_index])
    demand_service = int(row_values[demand_service_index])
    live_service = int(row_values[live_service_index])
    http_cache = int(row_values[http_cache_index])
    demand_cache = int(row_values[demand_cache_index])
    live_cache = int(row_values[live_cache_index])
    info = Ipservice(sn=sn, date=date, http_ip=http_ip, demand_ip=demand_ip, live_ip=live_ip, all_ip=all_ip,
                     http_service=http_service, demand_service=demand_service, live_service=live_service,
                     http_cache=http_cache, demand_cache=demand_cache, live_cache=live_cache)
    session.add(info)
    session.commit()
session.close()
