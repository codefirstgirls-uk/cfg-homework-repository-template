### Assesment two - Christelle Utt

## Theory Questions

## 1. What is Thread and Multithreading?
# Thread is executing. Multithreading is same as concurrency, so switching fast between threads. 

## 2. What is Concurrency and Parallelism and what are the differences?
# A: Concurrency is when program execute threads so fast, that it seems like its running
# parallel, but it is actually switching between them. Parallelism is when program executes multiple
# threads at the same time, like name says parallel way. 

## 3. What is Garbage collector? How does it work?
# A: Garbage collector helps with memory and managing that. It collects garbage and also counts refrences.

## 4. What is Transaction Management in a relational database (give an example)?

## 5. What is an endpoint and what are the most common methods to interact with 
the API data source?
# Endpoint in API is where we one computer gets that information/function/application from another who provides it. 
# Most common ways to interact with API data source is when we make request from there. 

## 6. What is data normalization in SQL? Please provide an example (any) of a 
database restructuring using primary/foreign keys to maintain data integrity. 
# A: It means you seperate data to different smaller databases so that there is less opportunities that something
# happens all the data and there is easier to modify it, if the databases are smaller. 
# Example: We have customer_id is primary_key in customer information DB and also that as foreign key
# in orders So we can actually track down the customer if we have accsess to the databases. 

## 2.Discuss Exception handling (4 pts) and debugging in Python (4 pts)
# A: Exeption handeling is helping to prevent cases that we can see coming. Like if it is dividing,
then we can also raise exeption before it happens and we can prevent that code would not break.
Debugging is helping to see, where we went wrong in our code and how the code plays step by step,
so we could see how it works and where we can repair it. 

## 3.Write a function that takes in a non-empty array of integers...
# A: Answer in coding file

## 4.Write tests for the newly created Sorted Squared Numbers function (in Q3). Provide a brief explanation for your test case options. 
# A: Answer in test file. For testing i took one positive case and the other one is case when Exception is thrown because there are negative
# numbers in array

## 5.Agile methodology: name and describe any 2 of the main roles in a Scrum Agile team.
# A: Scrum Master- helps the team with coaching, initiating meetings, troubleshooting, leading the meetings and being kind of
# team leader. Is one of the links between Product Manager and also Management. Development team - they are greating the 
# end-product (desing, testing, developing, publishing, maintaining).

## 6.Discuss advantages and disadvantages of TDD (Test Driven Development):
# A: Advantages for Test Driven Development is that we can test all the components fast
# and make them better if needed. We can test them by little pieces, which makes it fast. 
# Disadvantageses are that in bigger projects where we need more planning and thinking ahead
# we can't use TDD, because it's meant for more spontaneous and not that rigid development. 

## 7.What is a Python DB cursor? Provide an example 
# A: It acts like the typical cursor in computer, so letting know where it is (when you have
# connected DB and Pyhton) if you want to make queries from DB to Python. 


## 8. Write a SQL query to find the maximum order (purchase) amount for 
each customer.
# A:
````
SELECT customer_id, max(purch_amt)
FROM orders
WHERE customer_id >= 3002 and customer_id <= 3007 
GROUP BY customer_id
HAVING max(purch_amt) > 1000

````