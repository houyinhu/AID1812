
create database eshp default charset = utf8

create table order_from(
  order_id varchar(32),
  cust_id varchar(32),
  order_date datetime,
  status enum('待付款','待发货','已发货','已收货','申请退货','已退货','废弃'),
  products_num int,
  amt decimal(16,2)
)default charset=utf8;

insert into order_from values
('100001','4102241000',now(),'待付款',5,150),
('100002','4102241001',now(),'待发货',6,200),
('100003','4102241002',now(),'待付款',1,20),
('100004','4102241003',now(),'已发货',2,400),
('100005','4102241004',now(),'待付款',1,20),
('100006','4102241005',now(),'申请退货',3,500),
('100008','4102241006',now(),'已退货',1,10),
('100009','4102241007',now(),'已收货',4,100),
('100010','4102241008',now(),'已退货',2,40),
('100011','4102241009',now(),'已收货',2,40),
('100012','4102241010',now(),'废弃',2,40),
('100013','4102241000',now(),'待发货',5,150),
('100014','4102241000',now(),'已发货',5,150);

select * from order_from where status='待付款';
select * from order_from where status='已发货' or status='已收货' or status='申请退货';
select * from order_from where cust_id = '4102241000' and status = '待发货';
select order_date,status from order_from where order_id = '100003';
select * from order_from where cust_id = '4102241000'order by order_date desc ;
select status '状态',count(*) from order_from group by status;
select max(amt) from order_from ;
select min(amt) from order_from ;
select sum(amt) from order_from ;
select avg(amt) from order_from ;
select * from order_from order by amt desc limit 3;
update order_from set status = '已收货' where order_id = '100014';
delete from order_from where status = '废弃';




