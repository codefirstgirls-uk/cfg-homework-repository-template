**1 Python/SQL theory questions**

1. A thread is a type of instruction can run independently of other codes within a program. Whilst multithreading enables multiple threads to run simultaneously with the assistance of a CPU. 

2. As opposed to sequentially executing each task one by one, concurrency is when multiple tasks are processed simultaneously. While parallelism refers to the execution of tasks in parallel.

3. Garbage collection is the process by which Python periodically frees and reclaims memory blocks that are no longer needed. In Python, the garbage collector runs when the reference count of an object reaches zero. Reference counts of objects change as their aliases change.

4. A database server's transaction management is responsible for processing multiple transactions issued by various clients. An example will be you transferring money from your bank account to your friends account.

5. End points are the digital location where an API receives requests about a specific resource on it's server. This most commonly the URL which provides the location of the server. 

6. Data normalization in SQL ensures that the columns and tables are arranges in such a way that database integrity constraints enforce their dependencies. 

**2. Discuss Exception handing (4 pts) and debugging in Python (4 pts)**
In python exceptions are raised by errors, they are TypeError which is used for an unsupported operation such as diving an integer with a string. Then we have the KeyError which is used for an invalid used key. Overall these exception handlers are there to handle unexpected behavioir or error in our programms as well as debugging them to try an analyse and locate any bugs we may encounter in our code. 

**5. Agile methodology: name and describe any 2 of the main roles in a Scrum Agile team.**

**6. Discuss advantages and disadvantages of TDD (Test Driven Development):**

In TDD we only need to write code that's needed meaning we have to prevent writing code when all test have passed. Moreover as we write code the first time it becomes more easy to test. It is also easy to maintain because different part of the the application are disconnected from one another and have a clear interface. Making code more easy to take care of. A disadvantage is the test has to be maintained and may be hard to write. initially it also slows down the development process. 

**7. What is a Python DB cursor? Provide an example** 

Is an object that is used to make the connection for executing SQL queries. Cursors are objects that help execute queries and fetch records from databases. mysql-connector-python is used to execute statements and communicate with the SQL database

**8. SQL Query**
select MAX(purch_amt), count(customer_id)
from ORDERS
where purch_amt > 1000
AND customer_id BETWEEN '3002' AND '3007'
group by customer_id;