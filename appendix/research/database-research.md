# Database Research

This document summarizes our findings about ***which database frameworks are most suitable for Knowball***.

## Relational Databases

#### PostgreSQL

#### MySQL

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
