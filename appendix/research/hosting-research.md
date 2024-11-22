# Hosting Research

This document summarizes our findings about ***which platform will be best to host Knowball on***.

## Major Providers

> #### Conclusions
> I believe hosting Knowball with a major provider will, in the end, simplify development. Azure and AWS are comprehensive,
> keeping all our resources in one place. Not to mention, they each offer things that the smaller options simply don't. Between
> them, Azure is preferable for our needs. AWS is more complicated and poses a more acure risk of incurring charges. Heck, I
> had a small assignment pick up a $30 bill from them just a few weeks ago... ouch. Regardless of host, we are likely to bleed
> SOME costs. Azure gives us a cushion with $100 of free credits for students. So long as we are mindful of it, I'm confident
> we can remain within those free credits.

#### Azure

The Azure free tier offers 750 hours of B1S virtual machines per month, which is enough for one app. It also includes the
App Service Plan for hosting web applications. Some further offerings are listed below.

- Azure SQL Database for 12 months with 250 GB of storage.
- Free Cosmos DB with 400 RU/s throughput and 5 GB of storage.
- 1 million serverless function executions per month via Azure Functions (which we could use for dumping temporary data).
- 5 GB of storage in Azure Blob Storage (which we could use for caching).
- Benefits for students.

#### AWS

The AWS free tier offers 750 hours of EC2 t2.micro per month. It also includes 1M requests per month and 3.2M seconds of
compute time through AWS Lambda. Some further offerings are listed below.

- Free Amazon Relational Database Service (RDS) with MySQL, PostgreSQL, or MariaDB for 12 months.
- Free DynamoDB with 25 GB of storafe and 25 read/write units.
- 5 GB of S3 storage (which we could use to store media, if needed).
- CloudFront CDN for caching frontend files.
- Elastic Beanstalk to deploy and manage web apps.

## Alternatives

> #### Conclusions
> Trying to be clever with hosting options risks complicating the project. Each of the options below is limited in scope,
> meaning multiple would be needed (e.g., Heroku for the backend AND Vercel for the frontend). Performance might also be
> middling, though that isn't a terrible concern for our small project.

#### Heroku

Heroku's cheapest tier offers free Dynos (their compute resource) with a cap around 1000 hours per month. It also offers a
free PostgreSQL database up to 10,000 rows. This option would be simple to deploy, with Flask, Vue.js, and SQL integration.

#### Render

Render's cheapest tier offers 750 monthly hours of free web services, enough for one app. It also offers a free PostgreSQL
database up to 1 GB of storage. It has faster cold start times than Heroku.

#### Vercel

Vercel's cheapest tier offers serverless hosting which is ideal for the Vue.js frontend. However, note that it is not
designed for backend hosting.

#### Fly.io

Fly.io's cheapest tier offers small VMs for free - they share CPUs and 256 MB of RAM. It is coupled with Docker for easy deployment.

***And many, many more...***
