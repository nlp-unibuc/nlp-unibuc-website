nlp-unibuc website source
=========================

- one can simply change the markdown files, push, and the changes will be visible at nlp.unibuc.ro


## How to test changes locally

You need [Pelican](http://blog.getpelican.com/) and [typogrify](https://pypi.python.org/pypi/typogrify) in order to generate the pages.
```
   pip3 install -r requirements.txt
```
In order to deploy the website, if you have commit rights to the organization,
the easy way to set up is as follows:

1. Clone the repo:

```bash
   git clone --recurse-submodules git@github.com:nlp-unibuc/nlp-unibuc-website.git
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

## Test changes locally with docker

1. install `docker` and `docker compose`

2. run `docker compose up`

3. check your changes on [http://localhost:8000](http://localhost:8000)


## Pushing changes to the reposotory


4. Push the changes in the source repo

```bash
   git status               # to see the files
   git add $FILE            # to add the changes
   git commit -m "done!"    # add some pretty message
   git push origin master   # push to master branch
```


6. Visit http://nlp-unibuc.github.io and enjoy your new changes!

