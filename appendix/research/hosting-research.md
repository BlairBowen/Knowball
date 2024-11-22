# Hosting Research

This document summarizes our findings about ***which platform will be best to host Knowball on***.

## Major Providers

#### Azure

#### AWS

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
