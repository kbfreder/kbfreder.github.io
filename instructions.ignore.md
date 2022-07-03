
# WTF is going on here?
You are using Pelican as your static-site generator
https://docs.getpelican.com/

It's a python package.

An old version (v3.7?) is installed in your base conda env (b/c you had bad env habits back in 2018). The newest (as of July 2022) version (v4.7.2) is installed in the conda env `webs`. (The new version is incompatible with another package (`disutils`) in your base env.)

## BOTTOM LINE
When going to develop & deploy your website, first switch to your `webs` conda env:
> `conda activate webs`


# Nomenclature
- "settings file" = `pelicanconf.py`


# Publishing
We must specify the output folder to match the folder that GitHub pages expects (`/docs`):

`pelican -w docs/sagemaker.html -o docs/ content/`
- `-w` = `--write-selected`


# Folder structure / setup notes
- "output" folder renamed to "docs", to make it compatible with GitHub Pages
    - GHP only allows the option to serve the site from the root of the repository, or from the `docs/` folder
    - https://github.com/kbfreder/kbfreder.github.io/settings/pages
    - https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site


# Plugins
Only one, to render Jupyter notebooks
currently using `ipynb`: (I think this is it): https://github.com/fredcallaway/pelican-ipynb

This appears to be a newer, and more recently-maintained alternative:
https://github.com/danielfrg/pelican-jupyter

In both, see notes about updating settings file, which has already been done.