---Join
--1.
select e1.last_name,to_char(e1.hire_date,'MONTH YYYY')
from employees e1 join employees e2
on e1.department_id=e2.department_id
where lower(e1.last_name) like '%a%' and
lower(e1.last_name) != 'gates' and
lower(e2.last_name) = 'gates';

--2.
select unique e1.employee_id,e1.last_name,e1.department_id,d.department_name
from employees e1 join employees e2
on e1.department_id=e2.department_id
join departments d
on e1.department_id=d.department_id
where lower(e2.last_name) like '%t%'
order by e1.last_name;

--3.
select e1.last_name,e1.salary,j.job_title,l.city,c.country_name
from employees e1 join employees e2
on e1.department_id=e2.department_id
join departments d
on e1.department_id=d.department_id
join jobs j
on e1.job_id=j.job_id
join locations l
on d.location_id=l.location_id
join countries c
on l.country_id=c.country_id
where lower(e2.last_name)='king'
and e1.manager_id=e2.employee_id;

--4.
select e.department_id,d.department_name,e.last_name,j.job_title,
to_char(e.salary,'$99,999.00')
from employees e join departments d
on e.department_id=d.department_id
join jobs j
on e.job_id=j.job_id
where lower(d.department_name) like '%ti%'
order by d.department_name,e.last_name;

--5.
select e.last_name,d.department_id,d.department_name,l.city,j.job_title
from employees e join departments d
on e.department_id=d.department_id
join locations l
on l.location_id=d.location_id
join jobs j
on j.job_id=e.job_id
where lower(l.city)='oxford';

--6.
select unique e1.employee_id,e1.last_name,e1.salary
from employees e1 join employees e2
on e1.department_id=e2.department_id
join departments d
on e1.department_id=d.department_id
join jobs j
on e1.job_id=j.job_id
where lower(e2.last_name) like '%t%' and
e1.salary > (j.min_salary+j.max_salary)/2
order by e1.last_name;

--7.
select e.last_name,d.department_name
from employees e
left outer join departments d
on e.department_id=d.department_id;

select e.last_name,d.department_name
from employees e
join departments d
on e.department_id=d.department_id(+);

select e.last_name,d.department_name
from departments d
right outer join employees e
on e.department_id=d.department_id;

--9.
select d.department_name,e.last_name
from departments d
left outer join employees e
on e.department_id=d.department_id;

select d.department_name,e.last_name
from departments d
join employees e
on e.department_id(+)=d.department_id;