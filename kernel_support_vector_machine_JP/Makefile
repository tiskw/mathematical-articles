# Makefile
#
# Author: Tetsuya Ishikawa <tiskw111gmail.com>
# Date  : January 20, 2020
#################################### SOURCE START ###################################

docker_image   = tiskw/latex:2020-01-19
docker_uidgid  = -u $(shell id -u):$(shell id -g)
docker_volume  = -v $(shell pwd):/workspace -w /workspace
docker_command = docker run --rm -it $(docker_uidgid) $(docker_volume) $(docker_image)
all_tex_files  = $(shell ls *.tex)

kernel_support_vector_machine:
	$(docker_command) make inside_docker

inside_docker:
	extractbb figures/*.pdf
	uplatex -halt-on-error -interaction=nonstopmode kernel_support_vector_machine
	dvipdfmx kernel_support_vector_machine

clean:
	rm -f *.aux *.dvi *.log

#################################### SOURCE FINISH ##################################
# vim: noexpandtab tabstop=4 shiftwidth=4
