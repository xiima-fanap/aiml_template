# Contributing

A document regarding the workflow that each developer must take in order to contribute to this project


## How to contribute?

1. Create a new branch from the dev branch
    ```bash
    git checkout -b [branch_name]

    # Sample branch names
    feature/[feature_name]
    bug/[bug_name]
    refactor/[refactor_theme]
    ```
2. Apply your changes. Make sure to **micro-commit** each change with a informing commit message
    ```bash
    git add [changed file]
    git commit -m "[Your informing message]"
    ```
3. Update the package version in `setup.py` according to **semantic versioning** guidlines
4. Update `CHANGELOG.md` similar to this template format
5. Push your commits
    ```bash
    git push origin -u [branch name]
    ```
6. Create a `Merge Request(MR)` or `Pull Request(PR)` to merge your branch with dev branch
7. Review comments on your request and take the necessary actions (Your merge request got accepted :)
8. Add a `tag` to your version
9. Push your module to a `pypi cache server`