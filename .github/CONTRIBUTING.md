# CONTRIBUTING GUIDE

This guide is for educators and developers who want to create their own workout
using the template repository.

## Set up new workout repository

To create a new repository from the template:

1. Press `Use this template` button
2. Select `Create a new repository` option from the dropdown menu

Proceed with common repository creation dialog at GitHub.

This will prepare a boilerplate repository.

For the repositories located within
[Python course](https://github.com/edu-python-course/)
organization use *workout* name prefix.

### Protect master branch

It's important not to work within the default branch. So, ensure noone can
commit directly into `master`. In **Settings** navigate to **Branches** under
the **Code and automation** section. Press `Add branch protection rule` button.

Provide branch name pattern and check following options:

- **Require a pull request before merging**
- **Do not allow bypassing the above settings**

This will protect the default branch from committing directly into it.
You may apply other protection rules, in case of need.

Create a branch protection rule.

### Set up I18N Crowdin project

It supposed you will use [Crowdin](https://crowdin.com) platform to manage
translations. Otherwise, skip this section.

Create a new project at Crowdin platform, or request one to be created 
(`shorodilov` at https://crowdin.com). 
The best practice is to use the same name both for the GitHub repo and
the Crowdin project.

Update the *crowdin.yml* file by providing the project id. Set up the VCS
integration to fetch the files for translation from the `master` branch.
The complete instructions are available 
[here](https://support.crowdin.com/github-integration/).

## Documentation

The [Sphinx](https://www.sphinx-doc.org) documentation generator is used to
prepare documentation for the workout. The documentation root is the *docs*
directory. The master document is *index*.

Source suffixes mappings are defined as:

```python
source_suffix = {
    ".txt": "restructuredtext",
    ".rst": "restructuredtext",
    ".md": "markdown",
}
```

The documentation build and deployment is a part of CI/CD. The documentation
from the `master` branch will be deployed to GitHub Pages.

### Write documentation

All documentation related content should be located in *docs* directory.
Static files, like images, should be located at *docs/_static* directory.

The documentation generator is configured to proces sources provided in
[Markdown](https://daringfireball.net/projects/markdown/) or
[reStructuredText](https://docutils.sourceforge.io/rst.html) format.
*txt* documents are treated as **reStructuredText**.

Create new documents and include them to the `toctree` in the master doc.
E.g. to include documents named **foo.txt** and **bar.md**:

```text
.. toctree::
    :name: master_toc

    foo
    bar
```

#### Generating documentation from the source code

Documentation can be generated from the `doctstring` using `sphinx.ext.autodoc`
extension. Please, see
[autodoc](https://www.sphinx-doc.org/en/master/usage/quickstart.html#autodoc)
documentation to get more information.

### Build documentation

The dependencies to build the documentation are optional and grouped under
`docs`. To install them run:

```shell
poetry install --with docs
```

To build the documentation run:

```shell
poetry run sphinx-build -b html docs _build
```

This will build the documentation in *_build* directory. The default language
is **English (en)**. To build documentation in additional languages pass the
`-D language=<locale>` option to the command run. Refer to [i18n](#i18n) for
additional information.

## I18N
