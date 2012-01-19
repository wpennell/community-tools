all:
	(cd slideshow; \
	 python setup.py develop; \
	 pserve production.ini --reload)
