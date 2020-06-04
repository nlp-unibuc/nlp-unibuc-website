nlp-unibuc website source
=========================

Source code for generating our static website.

You need [Pelican](http://blog.getpelican.com/) and [typogrify](https://pypi.python.org/pypi/typogrify) in order to generate the pages.
```
   pip3 install -r requirements.txt
```
In order to deploy the website, if you have commit rights to the organization,
the easy way to set up is as follows:

1. Do this step once:

```bash
   git submodule init
   git submodule update
   git remote add deploy https://github.com/nlp-unibuc/nlp-unibuc.github.io.git
   git config remote.deploy.push deploy:master
```

2. Generate the website locally:

```bash
   python3 -m pelican content/ -o output/ -s pelican.py

   # or if make is available:
   make html
```
The output directory contains the generated website.

3. Check your changes on localhost:8000

```bash
   cd output && python3 -m http.server

   # or if make is available:
   make serve
```


4. Push the changes in the source repo

```bash
   git status               # to see the files
   git add $FILE            # to add the changes
   git commit -m "done!"    # add some pretty message
   git push origin master   # push to master branch
```

5. Push the changes online:

```bash
   python3 -m ghp_import -r deploy -b master -p output/

   # if make is available
   make github
```

6. Visit http://nlp-unibuc.github.io and enjoy your new changes!

