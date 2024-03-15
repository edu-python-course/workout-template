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

## Set up I18N Crowdin project

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

The template repository comes with a minimal configuration file for the Crowdin
platform. It helps to automate the translations' delivery to the main project.

### Crowdin settings

The template repository is set up to look for the translation sources within
*docs/_locales/en* directory. **English (en)** locale is considered the default
one for the project.

This behavior can be changed by updating `language` variable in *docs/conf.py*
module and `source` in *crowdin.yml* config.

See also: [update translation sources](#update-translation-sources).

### Delivery the translations from Crowdin

If the integration with VCS is set up, the Crowdin platform will commit to
the translation branch. It'll also open a pull request to the source branch
(e.g. `master`) to merge the translated content.

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

## Prepare boilerplate module(s)

Source code lies in *src/workout* directory. Fill free to create as many
modules as you need to provide challenges and/or boilerplate code for the
workout.

You may provide the challenge(s) description in the module docstring, as well
as provide code definition.

E.g.
```python
# src/workout/func.py
"""
Workout functions
=================

.. autofunction:: get_sum

"""

from typing import Tuple


def get_sum(*numbers: Tuple[int, ...]) -> int:
    """
    Return a sum of given numbers
    
    """

    return sum(numbers)
```

and its variant

```python
# src/workout/func.py
"""
Workout functions
=================

.. py:function:: get_sum(*numbers: Tuple[int, ...]) -> int
    Return a sum of given numbers

"""
```

produce the same output.

See also: https://www.sphinx-doc.org/en/master/usage/domains/python.html.

## I18N

### Update translation sources

This action will create translation files, or update existing ones.

```shell
poetry run sphinx-build -b gettext docs _build/gettext
poetry run sphinx-intl --config docs/conf.py update -p _build/gettext -l en
```

> In case Crowdin project is configured using the crowdin.yml file from
> the template - output locales will be handled by the translation platform.

To generate other locales, use `-l` option with appropriate locale name.
See locales list at 
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
