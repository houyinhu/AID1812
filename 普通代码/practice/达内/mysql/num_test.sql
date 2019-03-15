

create table num_test(
--显示3位无符号整数，左边0填充
card_type int(3) unsigned,
dist_rate decimal(10,2)
);
insert into num_test values(1,0.88);
insert into num_test values(100,23.456);
insert into num_test values(1000,23.45);
insert into num_test values(2,3);

select * from acct order by balance desc

create table acct(
acct_no varchar(32),-- 账号,字符串
acct_name varchar(128),-- 户名
cust_no varchar(32),-- 客户编号
acct_type int,-- 账户类型
reg_date date,-- 开户日期
status int,-- 状态
balance decimal(16,2)-- 余额,数字最长16,2位小数
)default charset=utf8;





