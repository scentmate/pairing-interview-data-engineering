# Data Engineering pairing exercise

The purpose of this repo is to present you a situation close to the real life where you can show us how do you
work and that we can show also the way we work.

## Greetings!

Hello, beloved human being! Thanks a lot for taking the time to work on our code assignment ❤️

## The plan

The plan for this session is to go through a real world problem and have a good time coding in pair

### The problem

Before anything, just relax, take your time and read this description carefully before our pairing session.

Now, about us: Scentmate is a company that is using algorithms and machine learning to recommend fragrances (scents). The collection of this fragrances has been mocked (simulated) for this test and they are stored in a database. The service that handles the information in this database is the `Smart Library` service. It's the core of our platform and many other services depend on it.

The situation is described by the diagram below:

![diagram](/assets/assignment_diagram.png)

Our main service is called **Smart Library** (in yellow). This service is in charge of providing information to the
front end, mainly recommendations based on the code developed by our data scientists. It is hence a mix between OLTP (_Online transaction processing_) and OLAP (_Online analytical processing_). All the data related with fragrances and features about these fragrances is stored in a postgres database.

On the other edge you can see that our platform is currently using a cloud-based **CMS** (content management system) (in green) that is
using its own database and to which we do not have any access. The people from product and operations use this CMS to
modify the data related with fragrances because it is more convenient to use.

We have discovered that the CMS allows the usage of a Webhook (Webhooks are HTTP callbacks) to keep track of all the
changes that happened in the data and synchronize the two edges. 

Your general task will be to design a system that will be able to ensure the quality of the data and the sync between different data sources, i.e. the CMS and the smart-library

This general task has been split in different tickets within our sprint that we will share with you during the pair programming session.

### The tools

In this repository you can find the tools that you will need for creating a solution:

- `cms_simulator` -> It contains the code that "simulates" data changes on the CMS by the product and operations teams.
  It is a simple python service using an API layer implemented with FastAPI. You can check the code (similar to
  python with a sloppy encapsulation), but please do not modify it and always assume that you do not have the possibility to
  act on that side. (unless you think there is a bug)

  We will assume that the CMS has a UI describing the available endpoints similar to the one below:
  ![diagram](/assets/cms_openapi.png)

  The POST to `/listener` allows to attach the webhook to a given endpoint. If one passes a valid endpoint, everytime that there is a change in the CMS that change will be sent to that endpoint as a json payload.

- `database_config` -> Contains the `sql` files that define the schemas needed for the setting. These schemas can be
  really useful, and we recommend taking a look directly or using your preferred database client (dbeaver, pgAdmin,
  etc.). This folder contains a short script that we used to generate the dummy data.

- `smart_library` -> Contains the edge of the system that we want to synchronize with the content of the
  CMS. There is no reason for that name... it is just a fun name we picked :)
  You have control on this folder so <ins>feel free to modify it or even integrate your own solution here.</ins>

- `your_solution` -> It could (not must) contain your solution if you need it to achieve the desired result. You are the owner within this piece of code so feel free to follow your own criteria.

All these services are combined using docker compose. We recommend taking a look at the logs. 

We expect that your solution could be integrated within the existing docker compose structure, so that if needed you will need to dockerize it and create
your own service within the `docker-compose.yaml`.

## The setup you need
You will need:

- An IDE. We use mainly [visualcode](https://code.visualstudio.com/) and [pycharm](https://www.jetbrains.com/pycharm/), but feel free to pick whatever suits you best
- [Python 3.8](https://www.python.org/) or superior and [pipenv](https://pipenv.pypa.io/en/latest/). Check in advance how to install and use them. 
- Docker. You will need to have [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) installed. Ensure you have enough memory allocated for docker.
- A postgres GUI client. We use [Dbeaver](https://dbeaver.io/) and [pgAdmin](https://www.pgadmin.org/) but feel free to use a different one
- A tool to fire HTTP requests; if you're familiar with command-line tools such as `curl` it should be enough, but if you prefer something more complex like [Postman](https://www.postman.com/) it's OK

## How to run this code
The code is designed to be ran with docker compose. Afer executing `docker compose up` you should see something like this:

```shell
> docker-compose up              
[+] Running 4/4
 ⠿ Container fragrance_database       Started         1.7s
 ⠿ Container cms_database             Started         1.8s
 ⠿ Container smart_library_simulator  Started         3.2s
 ⠿ Container cms_simulator            Started         3.3s
```

The logs will appear and they could provide useful information.

Once working you could find:
- The CMS UI at [http://localhost:9090/docs](http://localhost:9090/docs)
- The smart library service is available at [http://localhost:9099/](http://localhost:9099/)
- The CMS database reacheable at host:`localhost` and port:`15432`
- The smart library database reacheable at host:`localhost` and port:`25432`

## Things we love

- Your ideas and the way you express them (guide us through your thoughts)
- Docstrings and documentation
- Well formatted code (following PEP8 guidelines)
- Readability of the code
- That you show us your preferred git work flow
- <ins>Testing!</ins>
- That you feel comfortable
- That you can use your preferred packages during the test
- Architecture (within a service and between services)
- And of course...emojis

## Disclaimer
**We do not expect that you finish all the tasks!** No expectations are put on the amount of tasks addressed during the session. We prefer to have a variety of tasks in case you get blocked in one you can switch to a different one that you prefer.

**We will not evaluate the amount of work but the process while producing that work**

**If you do not know terms about the domain (fragrance, endpoint, webhook, etc), please do ask**

We know everyone has limitations on how much time they can invest on a coding challenge, and we're conscious that no one
knows everything. Maybe you don't know how to implement a HTTP API. Or maybe you don't have enough time to research into
all the possible models to use on a solution. Just let us know about any possible limitations and we'll adapt

**Remember that we are humans, so imperfect and biased. Do not judge yourself or ourselves just for this test**

## Final words

Good luck! We hope you enjoy working on this task. And if you need anything at all, please feel free to reach out to us!
