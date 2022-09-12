The YouTube talk is [here](https://www.youtube.com/watch?v=crKNBSpO2_I).

There are lots of links [here](https://lichess.org/source).

# Clients

## Web (lichess.org)

- TypeScript + Snabbdom

## Mobile

- TypeScript + CapacitorJS (native apps)

## Public Web API

- 2.5 million requests/day

# CDN

- Cloudflare (images, JS, sounds, stylesheets)

# Back End

## manta: primary server

- nginx
  - HTTP + websockets
  - TLS offloading
	- rate limiting
	- logging
	- rewrite HTTP headers
	- pass requests -> `lila`

## lila (lichess in Scala)

- Scala + Play

### websockets

- realtime events
- chat
- chess moves
		- low latency is important, e.g. in "UltraBullet" (15 seconds for the entire game)
- 100,000+ concurrent websocket connections
- used to be a single server

## lila-ws service on `starr` server

- receives and records chess moves
- publishes moves to a redis pub/sub in `manta`

## hyper service on `hyper` server

- responds to leaderboard requests
- publishes leaderboard to redis pub/sub in `manta`

# db

## mongoDB

- distributed across a replica set with seven nodes
- read-write to one node
- four secondaries read-only
- two secondaries for backups (one-hour delay, 24-hour delay) 

When they ran into synchronization problems, they split the various types of data into their own databases:
- puzzles
- studies
- analysis
- YOLO (data we're not so concerned about, which can be re-generated if need be)
- reduced the load by 50%

## Elastic Search
- search players, teams, games
- all games are indexed
- they maxed it out (2.1b games)
		- distributed it over five shards

# Other
- image resizing
		- user profile pics, blog thumbnails (Go)
- analysis
		- opening analysis (Rust)
- table-based service
  - fewer than seven pieces on each side, it'll tell you the winning and losing trajectories
- GIF service (Rust)
  - generate a GIF from any game
- push notifications
- FishNet (Rust, used to be Python)
		- evaluation of a game
		- uses Stockfish
    - it partly runs on volunteers' machines

# Anti-Cheating

## irwin (neural network, Python + TensorFlow)
- the more you play like an engine, the more suspicious you are: you'll be flagged accordingly

## paladin (neural network, Python + TensorFlow)
- uses chess statistics over a long period of time
		- 50 useful metrics which can be used to distinguish people who play honestly and those who don't.

## CRBot (Rust)
- also compares moves against engine

## Sandbag Bot
- sandbaggers lose on purpose to lower their rating
  - to get easier opponents
	- to join easier tournaments

# Monitoring

- `cayman` instruments all the Scala services
  - sends application metrics to InfluxDB and Prometheus
- non-Scala services use a local Telegraph agent on every server, which sends it to InfluxDB + Prometheus
- alerts in Prometheus, PagerDuty for notifying people of time-sensitive things
  - two people on-call
- key metrics: number of moves, HTTP traffic, HTTP traffic latency
- Grafana for visualizing the data

# In-Memory Caching
- 1,000 caches in `lila`
		- hit rate
