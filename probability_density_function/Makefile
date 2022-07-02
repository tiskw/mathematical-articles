# Makefile
#
# Author: Tetsuya Ishikawa <tiskw111gmail.com>
# Date  : January 20, 2020
#################################### SOURCE START ###################################

docker_image   = tiskw/latex:2022-03-01
docker_uidgid  = -u $(shell id -u):$(shell id -g)
docker_volume  = -v $(shell pwd):/workspace -w /workspace
docker_command = docker run --rm -it $(docker_uidgid) $(docker_volume) $(docker_image)
all_tex_files  = $(shell ls *.tex)

random_fourier_features_for_gaussian_process.pdf: $(all_tex_files)
	$(docker_command) make inside_docker

inside_docker:
	extractbb figures/*.pdf
	uplatex -halt-on-error -interaction=nonstopmode probability_density_function
	dvipdfmx probability_density_function

clean:
	rm -f *.aux *.dvi *.log figures/*.xbb

#################################### SOURCE FINISH ##################################
# vim: noexpandtab tabstop=4 shiftwidth=4
