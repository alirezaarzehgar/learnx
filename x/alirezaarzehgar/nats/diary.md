# Diary

## 2026-08-30

Today I just started this project and added two skills and then used the origin-finder skill
and opencode. Also I created developer-profiles.md in this directory, using origin-finder skill.
It provides and collects a reasonable range of information about the NATs maintainer.
It's not too much but is ok for now. I will learn more about NATs maintainer, send connections to them
today if there is adequate time.

I wanna send connection requests to some of NATS.io maintainers via following request template

```plaintext
Hey {NAME},

I'm Alireza, Go developer here. Really impressed with your NATS work on GitHub. Would be great to connect.

Thanks.
```

List of maintainers I wanna send request on linkedin and check their career:
- Ivan Kozlovic

## 2026-08-31

Today I sent connection to mentioned maintainers on linkedin, talk to Ali Assar a Go developer who
has relations with Synadia people and check its posts on linkedin.

I have a good idea. Next step for me in roadmap is figuring out the initial idea behind nats. Why Derek
started developing NATS. What is the actual intention to creating it. What problem NATS solved in the
initial phase of its development ? These questions will help to finding reason to use this technology.

My first fun plan is reading first commits of project to see what Derek considered in the initial
development phases. But after that I should search and even ask Derek from the real history and intentions
behind NATS.

## 2026-09-1

Now I'm written an script on `./tools/git-next-commit` using bash script on this project. The goal is
moving to next commit messages when I'm checked out to first commit message.

First version is simple as following script:
```bash
#!/usr/bin/env bash
DEFAULT_BRANCH=$(git branch --contains origin | head -n 1)
BRANCH=${BRANCH:-$DEFAULT_BRANCH}
CURRENT_COMMIT=$(git show --format=format:"%h" --no-patch)
NEXT_COMMIT=$(git log --format=format:"%h" ${CURRENT_COMMIT}..${BRANCH} --reverse  | head -n 1)

git checkout ${NEXT_COMMIT}
```

I will extend and improve it using Claude Sonnet 5 because I believe you should tell to LLMs what actually
you want. I wanna add some features to this idea. I wanna move n commits forward and select between branches better.


I'm asking Claude for story and it was amaizing. I put references here:

**1. RedMonk Conversation — "the Forrest Gump of Messaging" (Feb 2025)**
https://redmonk.com/blog/2025/02/10/rmc-derek-collison-the-forrest-gump-of-messaging/

This is the richest source — a long-form interview where Derek walks through the whole history in his own words: his TIBCO years building Rendezvous and EMS, joining VMware to build Cloud Foundry, the RabbitMQ lockup that triggered the weekend rewrite, and the "Not Another TIBCO Server" name origin. Nearly everything in my summary about the Friday outage, the weekend build, the four original features, and the "blender/electric unit" analogy comes from this transcript.

**2. Changelog Podcast #641 — "NATS and the CNCF kerfuffle with Derek Collison"** (May 2025)
https://changelog.com/podcast/641

Derek confirms here that NATS was built specifically to power subsystems in Cloud Foundry, and that he had no desire to do anything more than that at the time. Also covers the 2017 founding of Synadia and the VMware open-source backstory.

**3. GOTO Copenhagen 2022 speaker bio**
https://gotocph.com/2022/speakers/2056/derek-collison

Confirms his broader career arc — TIBCO, Google's AJAX APIs group, architecting Cloud Foundry at VMware, then founding Apcera, and after its sale to Ericsson, taking the NATS messaging tech he'd designed to found Synadia.

**4. Beyond Exclamation profile** (Feb 2021)
https://beyondexclamation.com/derek-collison-a-technology-entrepreneur-challenging-the-way-our-digital-world-connects/

States plainly that NATS was created in 2010 during his time at VMware as a solution to a problem he personally faced — not a broader market initiative at the outset.

**5. Synadia blog — "Looking Ahead with Clarity and Purpose for NATS.io"** (Apr 2025)
https://www.synadia.com/blog/synadia-response-to-cncf

Derek's own words: nearly 15 years ago he created NATS as an open-source project, calling it "a labor of love." More about the recent CNCF governance dispute than origins, but confirms the timeline in his own voice.

**6. NATS.io SCALE 15x sponsor page**
https://www.socallinuxexpo.org/scale/15x/sponsor/natsio/

The official framing: NATS was created by Derek Collison in response to a market need for a simple, high-performance messaging solution, later adopted by VMware, CloudFoundry, Baidu, Siemens, and GE. This is more the "post-hoc marketing" version than the ground-level engineering story.

---

Now I'm starting looking at source code. From story and summary of interview I'm grasped initial version of NATS is very simple.

I studied gnats untill fd4612fab021659cd42be70d3c0938d620a09b73 commit message :))) It was awkward. Derek started with development
of a 32-bit hash algorithm package. After that developed a package for hashmap. Then developed something to keep a sublist for future
uses on pub/sub model. Then he developed and enhanced tests and after a commit he added gnatsd.go that contains `main()` function.
As everyone expect this commit should work, because it implemented a wierd PUB/SUB model but it doesn't worked anymore.
That codebase was fun and bugs walk through even an small code! In some commits he added locking using mutex, add atomic operation,
enabling caching, add logs, add tracing, enhance argument parsing, and so on.

When I saw PUB/SUB implementation in source code, I was expected it should work perfectly because codebase is small and everything is simple.
But it doesn't worked and it was funny. It have lots of bug. Even after 40 commits Derek fixed bugs on hashmap package!
After some commits Derek get rid of that bug and in fd4612fab021659cd42be70d3c0938d620a09b73 you can build project run a super simple pub/sub
scenario.

Check output:


NATS Server
```shell
> go build ./gnatsd.go
> ./gnatsd -DV
[{Host:0.0.0.0 Port:4222 Trace:true Debug:true Logtime:false MaxConn:65536}]
["DEBUG is on"]
["TRACE is on"]
["Starting nats-server version go 0.1.0.alpha.1 on port 4222"]
["Client connection created", [127.0.0.1, 57322], 1]
[["SUB OP", "SUB greeting 1"], "c: 1"]
["Client connection created", [127.0.0.1, 44500], 2]
[["PUB OP", "PUB greeting 13"], "c: 2"]
"], "c: 2"]ng msg: 1", "greeting", "", "Hello, World

```

NATS Consumer:
```shell
> telnet 127.0.0.1 4222
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
INFO {"server_id":"a4dcfe50969734eaaad2cfb1c71ce47c","version":"go 0.1.0.alpha.1","host":"0.0.0.0","port":4222,"auth_required":false,"ssl_required":false,"max_payload":1048576}
SUB greeting 1
MSG greeting 1  13
Hello, World
```

NATS producer:
```shell
> telnet 127.0.0.1 4222
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
INFO {"server_id":"a4dcfe50969734eaaad2cfb1c71ce47c","version":"go 0.1.0.alpha.1","host":"0.0.0.0","port":4222,"auth_required":false,"ssl_required":false,"max_payload":1048576}
PUB greeting 13
Hello, World
```

## 2026-09-02

Today I'm understand the nats-server in the fd4612fab021659cd42be70d3c0938d620a09b73 commit.
I have a big switch case on `(c *client) parse(buf []byte) error` and I found it is Finite State Machine. Before learning
about its model I was shocked that why this method used and why it is awkward as is. But it is a zero-copy mechanism and
is suitable for parsing message protocols in queue.

I learned and understand core business logic of it and then I should play with it.
