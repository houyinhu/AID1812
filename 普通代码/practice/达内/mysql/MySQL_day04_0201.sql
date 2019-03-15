



insert into customer values
('c0001','a','13460752737','2'),
('c0002','b','13460752739','1'),
('c0003','c','13460752738','1');


select acct.acct_no,acct.acct_name,customer.cust_no,customer.tel_no
from acct inner join customer on acct.cust_no = customer.cust_no;
或者
select acct.acct_no,acct.acct_name,customer.cust_no,customer.tel_no
from acct, customer where acct.cust_no = customer.cust_no;


select acct.acct_no,acct.acct_name,customer.cust_no,customer.tel_no
from acct left join customer on acct.cust_no = customer.cust_no;

select acct.acct_no,acct.acct_name,customer.cust_no,customer.tel_no
from acct right join customer on acct.cust_no = customer.cust_no;







