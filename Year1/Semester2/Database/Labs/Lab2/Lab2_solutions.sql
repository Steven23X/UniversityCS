--1.
select concat(first_name,last_name)||'castiga'||salary||
concat('lunar dar doreste',salary*3) "Salariu ideal"
from employees;

--2.
select initcap(first_name),upper(last_name),length(last_name)
from employees
where lower(first_name) like 'j%' or
lower(first_name) like 'm%' or
lower(first_name) like '__a%'
order by length(last_name) desc;

select initcap(first_name),upper(last_name),length(last_name)
from employees
where substr(first_name,1,1)='J' or
substr(first_name,1,1)='M' or
substr(first_name,3,1)='a'
order by length(last_name) desc;

--3.
select upper(first_name), employee_id, last_name, department_id
from employees
where trim(both ' ' from (upper(first_name))) =  'STEVEN';

--4.
select employee_id "Cod",last_name "Nume",length(last_name) "Lungime nume",
department_id "Cod departament",instr(last_name,'a') "Pozitie a"
from employees
where substr(last_name,-1)='e';

--5.
select last_name,hire_date
from employees
where mod(round(sysdate)-round(hire_date),7)=0;

--6.
select employee_id,last_name,salary,trunc(salary+15*salary/100,2) 
"Salariu nou",round(trunc(salary+15*salary/100,2)/100,2)"Numar sute"
from employees;

--7.
select last_name "Nume angajat",rpad(hire_date,20) "Data angajarii"
from employees
where commission_pct is not null;

--8.
select to_char(sysdate+30,'MONTH DAY YYYY MI SS')
from dual;

--9.
select round(months_between('1-JAN-2024',sysdate)*30)
from dual;

--10.
select to_char(sysdate+0.5,'DAY MONTH YYYY HH MI SS')
from dual;

select to_char(sysdate+0.003472,'DAY MONTH YYYY HH MI SS')
from dual;

--11.
select concat(concat(last_name,' '),first_name),hire_date,
next_day(add_months(hire_date,6),'Monday') "Negociere"
from employees;

--12.
select last_name,round(months_between(sysdate,hire_date))"Luni lucrate"
from employees
order by "Luni lucrate";

--13.
select last_name,hire_date,to_char(hire_date,'DAY')"ZI"
from employees
order by to_char(hire_date,'D');

--14.
select last_name,nvl(commission_pct,0)"Comision"
from employees;

--15.
select last_name,salary,nvl(commission_pct,0)
from employees
where salary+salary*nvl(commission_pct,0)>10000;

--16.
select last_name,job_id,salary,
case job_id
    when 'IT_PROG' then
        1.2*salary
    when 'SA_REP' then
        1.25*salary
    when 'SA_MAN' then
        1.35*salary
    else
        salary
    end "Salariu renegociat"
from employees;

--17.
select e.last_name,e.department_id,d.department_name
from employees e, departments d
where e.department_id=d.department_id;

--18.
select distinct e.job_id,j.job_title
from employees e,jobs j
where e.job_id=j.job_id and e.department_id=30;

--19.
select e.last_name,d.department_name,l.city
from employees e,departments d,locations l
where e.department_id=d.department_id and d.location_id=l.location_id and
e.commission_pct is not null;

--20.
select e.last_name,d.department_name
from employees e , departments d
where e.department_id=d.department_id and
lower(e.last_name) like '%a%';

--21.
select e.last_name,j.job_title,d.department_name
from employees e,departments d,jobs j,locations l
where e.department_id=d.department_id and
e.job_id=j.job_id and d.location_id=l.location_id and
l.city='Oxford';

--22.
select e1.employee_id "Ang#",e1.last_name "Angajat",e2.employee_id
"Mgr#",e2.last_name "Manager"
from employees e1 join employees e2
on e2.employee_id=e1.manager_id;

--23.
select e1.employee_id "Ang#",e1.last_name "Angajat",e2.employee_id
"Mgr#",e2.last_name "Manager"
from employees e1
left outer join employees e2
on e1.manager_id=e2.employee_id;

--24.
select e1.last_name "Nume angajat",e1.department_id "ID Departament",
e2.last_name "Nume coleg"
from employees e1 
inner join employees e2
on e1.department_id=e2.department_id and e1.employee_id <> e2.employee_id
order by e1.department_id, e1.last_name;

--25.
select e1.last_name,e1.job_id,j.job_title,d.department_name,e1.salary
from employees e1 join jobs j
on e1.job_id=j.job_id
left outer join departments d
on e1.department_id=d.department_id;

--26.
select e1.last_name,e1.hire_date
from employees e1 join employees e2
on e1.department_id=e2.department_id
and lower(e1.last_name)!='gates' and
lower(e2.last_name)='gates' and
e1.hire_date >e2.hire_date;

--27.
select e1.last_name "Angajat",e1.hire_date "Data_ang",e2.last_name "Manager",
e2.hire_date "Data_mgr"
from employees e1 inner join employees e2
on e1.department_id=e2.department_id and
e1.manager_id=e2.employee_id and
e1.hire_date<e2.hire_date;