[//]: # (TODO: update workout name)
# Workout: WORKOUT NAME

This repository is compatible with [Replit](https://replit.com/).

## Set up workout repository

### Creating a new repository from template

Press the `Use this template` green button at the top.

This will lead you to the repository creation page.
Provide a valid meaningful repo name and add its description.

There is no need to clone branches except `master`. Default branch is always at
the most stable version.

### Protect master branch

It's important not to work within the default branch. So, ensure noone can
commit directly into `master`. In **Settings** navigate to **Branches** under
the **Code and automation** section. Press `Add branch protection rule` button.

Provide branch name pattern and check following options:

- **Require a pull request before merging**
- **Require status checks to pass before merging**
    - **Require branches to be up date before merging**
- **Do not allow bypassing the above settings**

This will protect the default branch from committing directly into it.
You may apply other protection rules, in case of need.

Create a branch protection rule.

## Getting started

1. Clone your assignment repo to your local machine.
2. Create a new topic branch (e.g. `feature/workout`).
3. Complete the assignment instructions. Provide a clear objective and usage
   examples.
4. Prepare the code boilerplate modules.
5. Add test cases (`unittest` framework preferably).

### Make your boilerplate modules invisible for Git

When a boilerplate code is ready, you may want to implement the actual logic
for the assignment. It's useful for running tests especially. However, you do
not want to put the implementation to the assignment repository.

To make changes inside a file invisible for Git use:

```shell
git update-index --assume-unchanged <file>
```

To switch it back:

```shell
git update-index --no-assume-unchanged <file>
```

### Testing

Assignments follow TDD approach. This means all the tests should fail.

## Add the workout to Replit

[//]: # (TODO: complete the section)

### Add Replit project tests

In **Tools** section press `Tests` button and choose a testing method,
*Unit tests* will be suitable in most cases.

First you need to set up unit tests. In a setup window add required imports.
Also, you can provide `setUp` and `tearDown` methods within advanced setup
section.

After the `unittest` framework is set up, it a copy-paste time. Add tests by
pressing `Add test` button. Provide a test name (omit "test" at the beginning),
error message and the test's code itself.
Press `Create test` button when ready.
