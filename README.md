[//]: # (TODO: update workout name)
# Workout: WORKOUT NAME

This is a template for the Python course workout activities.
This repository is compatible with [Replit](https://replit.com/) IDE.

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
- **Do not allow bypassing the above settings**

This will protect the default branch from committing directly into it.
You may apply other protection rules, in case of need.

Create a branch protection rule.

## Providing workout materials

Please refer to the [CONTRIBUTING](.github/CONTRIBUTING.md) guide for more
details.

1. Create a new topic branch (e.g. `feature/workout`).
2. Provide the boilerplate module(s) within *src/workout* directory.
3. Provide documentation for the workout within *docs* directory.
4. Add test cases within *tests* directory (`unittest` preferably).

### Making changes invisible for VCS

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
