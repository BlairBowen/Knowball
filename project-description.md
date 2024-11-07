# Knowball

Sports trivia ***with a twist***.

> Brought to you by Ben Cimini (ciminibb@mail.uc.edu), Blair Bowen (bowenbv@mail.uc.edu), Stetson King (king3ss@mail.uc.edu),
> and advisor Will Hawkins PhD (hawkinwh@ucmail.uc.edu).

## Abstract

Knowball is the digital realization of a common game among friends. It is designed to explore how obscurity might be quantified
computationally. The centerpiece of that design is our “obscurity engine,” a logical structure tuned to evaluate athletes based
on achievements, social capital, and more. Knowball, the game, is a fun means of interacting with the engine. Players will name
athletes in response to prompts and be scored per the engine’s outputs. Top scores will appear on leaderboards as a competitive,
sporting bonus. We expect the engine to be a unique solution that agrees with our human interpretation of obscurity, and we expect
the game to be playable online. This project blends our interest in sports with a deep dive into how deterministic models can
handle vague concepts like obscurity.

## Further Discussion

#### Existing Solutions

There is no shortage of sports trivia games you could play right now. Clearly, that isn’t the most interesting aspect of Knowball –
the obscurity engine is. So, does something similar already exist? The short answer is no, not really; the long answer follows. A
knee-jerk reaction to the prospect of computing something subtle and vague like obscurity is “Well, AI could probably handle it!”
Transparently, our first designs were AI-based. With enough prompting, LLMs could estimate an athlete’s obscurity, but without the
consistency or conciseness Knowball is targeting. Still, they could help with the question at hand: “Does Knowball exist?” Here’s what
ChatGPT had to say.

> There are a few approaches and technologies that aim to quantify the "obscurity" or "popularity" of individuals, though none are
> widely recognized as definitive measures of obscurity in the same way your "obscurity engine" in Knowball is designed to be.

Let’s not take that at face value, though. Digging deeper, there are many individual metrics by which you could approximate obscurity.
In that regard, social media analytics, search engine trends, bibliometric analysis, and fan communities are all existing services that,
by design or otherwise, perform a similar computation. Knowball will stand out by consuming several such services for a balanced, richly
informed take on obscurity. It is designed to be a source of truth, not a contributor.

#### Approach

As the above would suggest, most of Knowball’s technical nuance is in backend processes. Major architectural components include the
obscurity engine (of course), a database, and a series of validators. The engine has already been discussed at length, so I’ll save the
details for elsewhere in this repository. Still, I should say that it will ingest search engine data, social media analytics, and in-game
statistics through a combination of API connections and web scraping. Both are approaches this group has experience with. The database,
on the other hand, will serve a few purposes. First, it will cache engine outputs for popular athletes to avoid frequent recomputations.
It will also house leaderboards and a repository of prompts (the trivia). Trivia generation is one reason we need validators. Whether it's
us or an ML model writing the prompts, they must be of appropriate difficulty for players. So, we’ll implement “validator processes” that
either accept or discard prompts based on the quantity and obscurity of athletes they reference.

For the full complement of backend processes, see our design diagrams. Others, like data standardization, also have essential roles in the
system. To avoid a redundant repository, though, I’ll wrap up by discussing the tech stack. At this point in our work, much of the tech stack
is still to be determined. However, the most likely outcome is this: Vue.js in the front end, MySQL for the database, with Python being the
backbone of most, if not all other components. As hinted earlier, there is potential to use ML in generating trivia, which would be written in
Python as well. This section will be updated when such decisions are finalized.
