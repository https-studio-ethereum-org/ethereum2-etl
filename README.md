# Ethereum 2.0 ETL

[![Build Status](https://travis-ci.org/blockchain-etl/ethereum2-etl.png)](https://travis-ci.org/blockchain-etl/ethereum2-etl)
[![Join the chat at https://gitter.im/ethereum-eth](https://badges.gitter.im/ethereum-etl.svg)](https://gitter.im/ethereum-etl/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Telegram](https://img.shields.io/badge/telegram-join%20chat-blue.svg)](https://t.me/joinchat/GsMpbA3mv1OJ6YMp3T5ORQ)
[![Discord](https://img.shields.io/badge/discord-join%20chat-blue.svg)](https://discord.gg/wukrezR)

Work in progress!

Ethereum 2.0 ETL lets you convert blockchain data into convenient formats like CSVs and relational databases.

*Do you just want to query Ethereum data right away? Use the [public dataset in BigQuery](https://console.cloud.google.com/bigquery?page=dataset&d=crypto_ethereum2&p=public-data-finance).*

[Full documentation available here](http://ethereum2-etl.readthedocs.io/).

## Quickstart

Install Ethereum 2.0 ETL:

```bash
pip install ethereum2-etl
```

Export beacon blocks ([Schema](docs/schema.md#beacon_blocks), [Reference](docs/commands.md#export_beacon_blocks)):

```bash
> ethereum2etl export_beacon_blocks --start-block 0 --end-block 200 \
--output-dir output \
--provider-uri https://projectid:secret@medalla.infura.io
```

Find other commands [here](https://ethereum2-etl.readthedocs.io/en/latest/commands/).

For the latest version, check out the repo and call 
```bash
> pip install -e . 
> python3 ethereumetl.py
```

## Useful Links

- [Schema](https://ethereum2-etl.readthedocs.io/en/latest/schema/)
- [Command Reference](https://ethereum2-etl.readthedocs.io/en/latest/commands/)
- [Documentation](https://ethereum2-etl.readthedocs.io/)

## Running Tests

```bash
> pip install -e .[dev,streaming]
> export ETHEREUM2_ETL_RUN_SLOW_TESTS=True
> pytest -vv
```

### Running Tox Tests

```bash
> pip install tox
> tox
```

## Running in Docker

1. Install Docker https://docs.docker.com/install/

2. Build a docker image
        
        > docker build -t ethereum2-etl:latest .
        > docker image ls
        
3. Run a container out of the image

        > docker run -v $HOME/output:/ethereum2-etl/output ethereum2-etl:latest export_beacon_blocks -s 0 -e 200 -p https://projectid:secret@medalla.infura.io
        > docker run -v $HOME/output:/ethereum2-etl/output ethereum2-etl:latest export_beacon_blocks -s 2020-08-04 -e 2020-08-05 -p https://projectid:secret@medalla.infura.io


## Projects using Ethereum ETL

* [Google](https://goo.gl/oY5BCQ) - Public BigQuery Ethereum datasets
* [Nansen](https://nansen.ai/?ref=ethereum2etl) - Blockchain analytics platform
