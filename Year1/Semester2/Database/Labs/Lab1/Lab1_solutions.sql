--5.
select employee_id,last_name,job_id,hire_date
from employees;

--6.
select employee_id "Cod",last_name "Nume",job_id "Cod job",hire_date "Data angajarii"
from employees;

--7.
select distinct job_id
from employees;

--8.
select last_name || ', ' || job_id "Angajat si titlu"
from employees;

--9.
select employee_id||', '||first_name||', '||last_name||', '||email||', '||phone_number||', '||hire_date||', '||
job_id||', '||salary||', '||commission_pct||', '||manager_id||', '||department_id "Date complete"
from employees;

--10.
select last_name,salary
from employees
where salary>2850;

--11.
select last_name,department_id
from employees
where employee_id=104;

--12.
select last_name,salary
from employees
where salary<1500 or salary>2850;

--13.
select last_name,job_id,hire_date
from employees
where hire_date between '20-FEB-1987' and '1-MAY-1989'
order by hire_date;

--14.
select last_name,department_id
from employees
where department_id in (10,30,50)
order by last_name;

--15.
select last_name "Angajat",salary "Salariu lunar"
from employees
where department_id in (10,30,50)and salary>1500;

--16.
select sysdate
from dual;

select to_char(sysdate,'MON')
from dual;

--17.
select last_name,hire_date
from employees
where to_char(hire_date,'YYYY')='1987';

--18.
select last_name,first_name,hire_date
from employees
where to_char(hire_date,'MON')=to_char(sysdate,'MON');

--19.
select last_name,job_id
from employees
where manager_id is null;

--20.
select last_name,salary,commission_pct
from employees
where commission_pct is not null
order by salary desc,commission_pct desc;

--21.
select last_name,salary,commission_pct
from employees
order by salary desc,commission_pct desc;

--22.
select last_name
from employees
where lower(last_name) like '__a%';

--23.
select last_name
from employees
where lower(last_name) like '%l%l%' and (department_id=30 or manager_id=102);

--24.
select last_name,job_id,salary
from employees
where job_id like '%CLERK%' or job_id like '%REP%' and
salary not in (1000,2000,3000);

--25.
select distinct department_id
from employees
where manager_id is null;