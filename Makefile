build:
	jupyter-book config sphinx .
	cat conf_postfix.py >> conf.py
	sphinx-build . _build -b html
rebuild:
	rm -rf _build
	jupyter-book config sphinx .
	cat conf_postfix.py >> conf.py
	sphinx-build . _build -b html
autobuild:
	jupyter-book config sphinx .
	cat conf_postfix.py >> conf.py
	sphinx-autobuild . _build -b dirhtml
autorebuild:
	rm -rf _build
	jupyter-book config sphinx .
	cat conf_postfix.py >> conf.py
	sphinx-autobuild . _build -b dirhtml
deploy: 
	jupyter-book config sphinx .
	cat conf_postfix.py >> conf.py
	ablog build
	ablog deploy
