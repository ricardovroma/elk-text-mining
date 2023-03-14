SHELL:=/bin/bash

VERBOSE=1

PODMANAGER=docker

CURRENT_DIR=${shell pwd}
STORE=${CURRENT_DIR}/.store

cleanup:
	@${PODMANAGER} compose down
	@rm -r ${STORE}

run:
	@${PODMANAGER} compose down --remove-orphans
	@${PODMANAGER} compose up --build