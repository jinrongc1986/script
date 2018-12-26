#创建业务
truncate `nem_business`;
INSERT INTO `nem_business` (`id`,`create_time`,`update_time`,`name`,`icon`,`task_type`,`metric_name`,`deleted`) VALUES (1,'2018-12-25 15:00:00','2018-12-25 15:00:00','海外学术资源','2','3','first_screen_time','0');
INSERT INTO `nem_business` (`id`,`create_time`,`update_time`,`name`,`icon`,`task_type`,`metric_name`,`deleted`) VALUES (2,'2018-12-25 15:00:00','2018-12-25 15:00:00','国内学术资源','2','3','first_screen_time','0');
INSERT INTO `nem_business` (`id`,`create_time`,`update_time`,`name`,`icon`,`task_type`,`metric_name`,`deleted`) VALUES (3,'2018-12-25 15:00:00','2018-12-25 15:00:00','互联网MOOC','2','3','first_screen_time','0');
INSERT INTO `nem_business` (`id`,`create_time`,`update_time`,`name`,`icon`,`task_type`,`metric_name`,`deleted`) VALUES (4,'2018-12-25 15:00:00','2018-12-25 15:00:00','新闻门户','2','3','first_screen_time','0');
INSERT INTO `nem_business` (`id`,`create_time`,`update_time`,`name`,`icon`,`task_type`,`metric_name`,`deleted`) VALUES (5,'2018-12-25 15:00:00','2018-12-25 15:00:00','系统及软件下载','3','4','speed_download','0');
INSERT INTO `nem_business` (`id`,`create_time`,`update_time`,`name`,`icon`,`task_type`,`metric_name`,`deleted`) VALUES (6,'2018-12-25 15:00:00','2018-12-25 15:00:00','在线视频','1','6','request_time','0');
INSERT INTO `nem_business` (`id`,`create_time`,`update_time`,`name`,`icon`,`task_type`,`metric_name`,`deleted`) VALUES (7,'2018-12-25 15:00:00','2018-12-25 15:00:00','在线购物','2','3','first_screen_time','0');


#创建任务
truncate `nem_task`;
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (1 ,'2018-12-25 15:00:00','2018-12-25 15:00:00','腾讯','https://v.qq.com/x/cover/mu66s8pwz8m1tlo/o0027qs964g.html','1','1','300','6','0','6','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (2 ,'2018-12-25 15:00:00','2018-12-25 15:00:00','爱奇艺','http://www.iqiyi.com/v_19rqytm5a8.html?vfm=m_103_txsp#curid=1270304300_e4663c7f93796ef71fd9c900ae9b5c9f','1','1','300','6','0','6','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (3 ,'2018-12-25 15:00:00','2018-12-25 15:00:00','优酷','https://v.youku.com/v_show/id_XMzc4NDkwNTIzMg==.html?spm=a2hww.11359951.m_26657.5~5~1~3!2~A','1','1','300','6','0','6','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (4 ,'2018-12-25 15:00:00','2018-12-25 15:00:00','Science','http://www.sciencemag.org/','1','1','300','3','0','1','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (5 ,'2018-12-25 15:00:00','2018-12-25 15:00:00','PNAS','http://www.pnas.org/','1','1','300','3','0','1','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (6 ,'2018-12-25 15:00:00','2018-12-25 15:00:00','SAGE','http://journals.sagepub.com/','1','1','300','3','0','1','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (7 ,'2018-12-25 15:00:00','2018-12-25 15:00:00','CNKI','http://cnki.net/','1','1','300','3','','2','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (8 ,'2018-12-25 15:00:00','2018-12-25 15:00:00','万方数据','http://wanfangdata.com.cn/index.html','1','1','300','3','0','2','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (9 ,'2018-12-25 15:00:00','2018-12-25 15:00:00','北大法宝','http://www.pkulaw.cn/','1','1','300','3','0','2','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (10,'2018-12-25 15:00:00','2018-12-25 15:00:00','中国大学MOOC','https://www.icourse163.org/','1','1','300','3','0','3','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (11,'2018-12-25 15:00:00','2018-12-25 15:00:00','超星慕课','http://mooc.chaoxing.com/','1','1','300','3','0','3','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (12,'2018-12-25 15:00:00','2018-12-25 15:00:00','学堂在线','http://www.xuetangx.com/','1','1','300','3','0','3','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (13,'2018-12-25 15:00:00','2018-12-25 15:00:00','新浪','https://news.sina.com.cn/','1','1','300','3','0','4','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (14,'2018-12-25 15:00:00','2018-12-25 15:00:00','网易','https://news.163.com/','1','1','300','3','0','4','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (15,'2018-12-25 15:00:00','2018-12-25 15:00:00','凤凰网','http://news.ifeng.com/','1','1','300','3','0','4','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (16,'2018-12-25 15:00:00','2018-12-25 15:00:00','Windows下载更新','http://6.au.b1.download.windowsupdate.com/d/upgr/2018/04/17134.1.180410-1804.rs4_release_clientchina_ret_x64fre_zh-cn_de20e00e3402b9c1ac776cc2f449fefcc410e477.esd','1','1','300','4','0','5','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (17,'2018-12-25 15:00:00','2018-12-25 15:00:00','AndroidApp下载','http://appdlc.hicloud.com/dl/appdl/application/apk/cc/cce8806b6c90427591ecf37e276ed6b1/com.netease.dwrg.huawei.1805221614.apk?sign=d9eb1001ed10010520009000000@56197D6CD53CD9B6F33678F6CD347CAA&cno=4010001&source=renew&hcrId=780B2EC1CA30463FB180BEBAA58A9040&extendStr=%3B&encryptType=1&subs','1','1','300','4','0','5','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (18,'2018-12-25 15:00:00','2018-12-25 15:00:00','京东','https://www.jd.com/','1','1','300','3','0','7','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (19,'2018-12-25 15:00:00','2018-12-25 15:00:00','天猫','https://www.tmall.com/','1','1','300','3','0','7','0','1');
INSERT INTO `nem_task` (`id`,`create_time`,`update_time`,`name`,`url`,`url_type`,`enable`,`interval`,`task_type`,`deleted`,`business_id`,`status`,`sync`) VALUES (20,'2018-12-25 15:00:00','2018-12-25 15:00:00','淘宝','https://www.taobao.com','1','1','300','3','0','7','0','1');


