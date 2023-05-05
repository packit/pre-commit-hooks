# pre-commit-hooks
Our repo for managing pre-commit hooks

### Our hooks

- `check-rebase` - Check if your branch is up-to-date with the upstream.
    - Specify the url of the upstream repo in `args: [git://github...]`.
- `validate-config` - Validate a [package config for Packit](https://packit.dev/docs/configuration).
  - Requires `bash`.
  - Runs the validation if there's a `packit` binary present.
  - Passes if `packit` is not installed; this is useful if you can't install `packit` in the CI but still want to run the hook at least locally.
- `validate-config-in-container` - Validate a [package config for Packit](https://packit.dev/docs/configuration).
  - Uses [packit image](https://quay.io/repository/packit/packit) to run packit in a container.
  - Requires `docker` binary to be present, which can be a problem for example in [pre-commit.ci](https://github.com/pre-commit-ci/issues/issues/11)

### Using check-rebase with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: https://github.com/packit/pre-commit-hooks
        rev: v1.2.0
        hooks:
          - id: check-rebase
            args: [upstream_url]

### Using validate-config with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: https://github.com/packit/pre-commit-hooks
        rev: v1.2.0
        hooks:
          - id: validate-config

or

    -   repo: https://github.com/packit/pre-commit-hooks
        rev: v1.2.0
        hooks:
          - id: validate-config-in-container
