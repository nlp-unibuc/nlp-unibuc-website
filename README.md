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
2. Make changes to files and add changes:
```
   git status - to see the files
   git add $FILE - to add the changes
```

Generate the website locally:
```bash
   python3 -m pelican content/ -o output/ -s pelican.py
```
The output directory contains the generated website.

3. Push the changes in the source repo
```bash
   git commit -m "Add a message to describe your changes"
   git push origin master
```

4. Push the changes online:
```bash
   make github
```
or, if `make` is not available:

```bash
   ./ghp-import -r deploy -b master -p output/
```

5. Visit http://nlp-unibuc.github.io and enjoy your new changes!

