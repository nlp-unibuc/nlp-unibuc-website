nlp-unibuc website source
=========================

Source code for generating our static website.

You need [Pelican](http://blog.getpelican.com/) in order to generate the pages.
In order to deploy the website, if you have commit rights to the organization,
the easy way to set up is as follows:

1. Do this step once:

   ```bash
   git submodule init
   git submodule update
   git remote add deploy git@github.com:nlp-unibuc/nlp-unibuc.github.io.git
   git fetch deploy
   git checkout -b deploy -t deploy/master
   git config remote.deploy.push deploy:master
   ```
2. Do this when you want to update the website, after changing or adding content:

   ``make github``

   or, if ``make`` is not available:

   ``ghp-import -r deploy -b master -p output/``

3. Visit http://nlp-unibuc.github.io and enjoy your new changes!

