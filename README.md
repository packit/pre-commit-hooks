# pre-commit-hooks
Our repo for managing pre-commit hooks

### Our hooks

- `check-rebase` - Check if your branch is up to date with the upstream.
    - Specify the url of the upstream repo in `args: [git://github...]`.


### Using check-rebase with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: https://github.com/packit-service/pre-commit-hooks
        hooks:
        -   id: check-rebase
            args: [upstream_url]
