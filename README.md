nlp-unibuc website source
=========================

Source code for generating our static website.

You need [Pelican](http://blog.getpelican.com/) and [typogrify](https://pypi.python.org/pypi/typogrify) in order to generate the pages.
In order to deploy the website, if you have commit rights to the organization,
the easy way to set up is as follows:

1. Do this step once:

   ```
   bash
   git submodule init
   git submodule update
   git remote add deploy https://github.com/nlp-unibuc/nlp-unibuc.github.io.git
   git config remote.deploy.push deploy:master
   ```
2. Make changes to files and inspect locally:
   ```
   pelican content/ -o output/ -s pelican.py

   ```
   The output directory contains the generated website.

3. Push the changes in the source repo
   ```
   git status - to see the files
   git add $FILE - to add the changes
   git commit -m "Add a message to describe your changes"
   git push origin master
   ```

4. Push the changes online:
   
   ``make github``

   or, if ``make`` is not available:

   ``./ghp-import -r deploy -b master -p output/``

5. Visit http://nlp-unibuc.github.io and enjoy your new changes!

