# Database Research

This document summarizes our findings about ***which database frameworks are most suitable for Knowball***.

## Relational Databases

#### PostgreSQL

PostgreSQL is robust, capable of handling complex queries and semi-structured data. It is an all-around option, with features
for most, if not all parts of our design. For example, it is good at dealing with concurrent users, which our game will
encounter.

#### MySQL

MySQL is simple, fast, and reliable. It is widely supported with mature tools. For ease-of-implementation, it is hard to beat.
Ultimately, whether or not it's a good choice depends on the complexity of our queries and caching.

#### Head to Head

- I'm seeing that MySQL is good for read-heavy workloads while, again, that PostgreSQL is good for complex queries and transactions.
- MySQL prioritizes speed and performance; PostgreSQL prioritizes data integrity.
- PostgreSQL supports advanced data types like JSON and XML; MySQL also supports JSON.
- In general, the pair are very similar.
- PostgreSQL is usually the preference of enterprise database admins, concerned with business needs at scale.
- MySQL is a popular choice for small to medium sized web applications.

## NoSQL Databases

> #### Conclusions
> The Knowball team is more familiar with relational databases, so we are wary of being reliant on NoSQL. However, it has obvious
> merit - for our purposes, especially Redis. We will consider Redis for a hybrid implementation, where it would handle the part
> of our database for which it is optional: leaderboards. Leaderboards don't need relational logic, so separating them makes
> sense in our design.

#### MongoDB

MongoDB would allow for flexible schema which, given our many data sources, could be beneficial. It is also particularly fast for
read-heavy workloads, which we will likely have. For example, Knowball will need to fetch athlete information often.

#### Redis

Redis has purpose-built features that align perfectly with certain parts of our design. A few examples: sorted sets, which are ideal
for leaderboards; time-to-live (TTL) settings, which is ideal for our caching operations.
