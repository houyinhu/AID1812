

create table student (
stu_no varchar(32),
stu_name varchar(128)
);


create table customer(
cust_no varchar(32) primary key,
cust_name varchar(128) not null,
tel_no varchar(32) not null
)default charset=utf8;




create table ai_test (
id primary key auto_increment,
name varchar(32)
);
create table ai_test(
	    id int primary key auto_increment,
		name varchar(32)
      );
	  insert into ai_test values(null,'Tom');



create table customer(
cust_no varchar(32) primary key,
cust_name varchar(128) not null,
tel_no varchar(32) not null,
status tinyint default 0
)default charset=utf8;


create table account(
acct_no varchar(32) primary key,
cust_no varchar(32) not null,
constraint fk_cust_no foreign key(cust_no)
references customer(cust_no)
);



create table acct_trans_detail(
trans_sn varchar(32) not null,-- 流水号
trans_date datetime not null,-- 交易时间
acct_no varchar(32) not null,-- 账号
trans_type int null,-- 交易类型
amt decimal(10,2) not null,-- 交易金额
unique(trans_sn),-- 交易流水建唯一索引
index(trans_date)-- 交易日期普通索引
);
jiumo search


alter table orders add primary key(order_id);
或者
alter table orders modify order_id varchar(32) primary key;

alter table orders modify(
 cust_id varchar(32) not null,
 order_date varchar(32) not null,
 products_num int(11) not null
 );

alter table orders modify
status set('待付款','待发货','已发货','已收货','申请退货','已退货','废弃')
default '待付款';

alter table orders add index date1(order_date);
后者
create index idx_order_date on orders(order_date);

