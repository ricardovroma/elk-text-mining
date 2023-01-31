# ELK Stack for Text Mining

It creates a ELK Stack using Docker to mining texts.

# Requirements
- [Docker](https://docker.com) **v20+**
- [Makefile](https://pt.wikibooks.org/wiki/Programar_em_C/Makefiles)

# Using
- Elasticsearch **v8.6** ([documentation](https://www.elastic.co/guide/en/elasticsearch/reference/8.6/install-elasticsearch.html))
- Kibana **v8.6** ([documentation](https://www.elastic.co/guide/en/kibana/8.6/install.html))
- Logstash **v8.6** ([documentation](https://www.elastic.co/guide/en/logstash/8.6/introduction.html))
- Metricbeat **v8.6.1** ([documentation](https://www.elastic.co/guide/en/beats/metricbeat/8.6/metricbeat-installation-configuration.html))

# Commands

## Run

```sh
make run
```
It'll run in an interactive mode.

## Stop
```sh
CTRL+c
```

## Cleanup
```sh
make cleanup
```