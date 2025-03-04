# NIEL

[![Niel Banner](static/niel-banner.svg)](https://github.com/aekasitt/niel/static/niel-banner.svg)

```sh
$ pip install niel
> ...
$ niel
> Usage: niel [OPTIONS] COMMAND [ARGS]...
>
>   niel
>
> Options:
>   --version  Show the version and exit.
>   --help     Show this message and exit.
>
> Commands:
>   auth         Start an authenticated session
>   create       Create a new rich menu
>   default      Show default rich menu identifier
>   drop         Drop rich menu identified by `menu-id`
>   image        Upload an image found by given `image-path` for the...
>   set-default  Set default rich menu identified by `menu-id`
```

Authenticate session (janky)

```sh
$ niel auth `<line-channel-access-token>`
> # Rewrites `.zshrc` or `.bashrc` with NIEL_AUTH_SESSION appended
$ source ~/.zshrc
> # OR
$ source ~/.bashrc
```

The next shell environment you open, will now have $NIEL_AUTH_SESSION
defined as your inserted line-channel-access-token.

Next step, create a RichMenu with defined YAML-file

```sh
$ niel create example.yml
> richmenu-fd5610793084b22a00a8eeb3812d5dd8
```

The YAML-file needs to follow requirements defined by RichMenu object
definitions set by LINE Messaging API documentation for RichMenu object <sup>[4]</sup>
found in the appendix. The basics of a RichMenu object definition is as such:

<details>
<summary>RichMenu Schema</summary>

```typescript
RichMenu {
  areas: [{
    action: {
      altUri.desktop?: string  // optional; utilized when action is "uri".
      clipboardText?: string  // required when action is "clipboard". (character limit: 1,000)
      data?: string // required when action is "datetimepicker", "postback", or "richmenuswitch". (character limit: 300)
      displayText?: string  // optional; utilized when action is "postback".
      initial?: string // optional; utilized when action is "datetimepicker".
      inputOption?: string  // optional; utilized when action is "postback".
      label?: string  // required when action is "camera", "cameraRoll", or "location".
      max?: string  // optional; utilized when action is "datetimepicker".
      min?: string  // optional; utilized when action is "datetimepicker".
      mode?: "date" | "datetime" | "time"  // required when action is "datetimepicker".
      richMenuAliasId?: string  // required when action is "richmenuswitch". Must be valid RichMenu identifier.
      text?: string  // required when action is "message". (character limit: 300)
      type: "camera"
        | "cameraRoll"
        | "clipboard"
        | "datetimepicker"
        | "location"
        | "message"
        | "postback"
        | "richmenuswitch"
        | "uri"
      uri?: string  // required when action is "uri".
    }
    bounds: {
      height: number
      width: number
      x: number
      y: number
    }
  }]
  size: {
    height: number
    width: number
  }
}
```

See more details on Action objects <sup>[1]</sup>, Area objects <sup>[2]</sup>,
Bounds objects <sup>[3]</sup> and RichMenu objects <sup>[4]</sup> schemas
and criteria under the appendix section.

</details>

### Upload an image for your preferred RichMenu

```sh
$ niel image default.png richmenu-fd5610793084b22a00a8eeb3812d5dd8
> True
```

### Set desired RichMenu with image uploaded as the default RichMenu

```sh
$ niel set-default richmenu-fd5610793084b22a00a8eeb3812d5dd8
> True
```

### Drop undesired RichMenu

```sh
$ niel drop richmenu-fd5610793084b22a00a8eeb3812d5dd8
> True
```

### Unable to repeatedly drop the same RichMenu identified by menu-id

```sh
$ niel drop richmenu-fd5610793084b22a00a8eeb3812d5dd8
> False
```

## Disclosures

Feel free to make an issue if any vulnerabilities are found in the project.
Also, this command-line interface relies on the following dependencies so if any
of them have been found to be vulnerable, please create an issue and clarify
as such.

* [click](https://github.com/pallets/click) - Python composable command line interface toolkit
* [httpx](https://github.com/encode/httpx) - A next generation HTTP client for Python. 🦋
* [pydantic](https://github.com/pydantic/pydantic) - Data validation using Python type hints
* [rich](https://github.com/Textualize/rich) - Rich text and beautiful formatting in the terminal
* [yaml](https://github.com/yaml/pyyaml) - Canonical source repository for PyYAML

## Contributions

Unless LINE Messaging API changes, no planned changes on the project.
But if you want to try your hand at the project, here is the recommended
set-up for your local development environment.

### Prerequisites

* [pyenv](https://github.com/pyenv/pyenv) - simple Python version management
* [uv](https://docs.astral.sh/uv) - extremely fast Python package & project manager written in Rust

### Set up local environment

The following guide walks through setting up your local working environment using `pyenv`
as Python version manager and `uv` as Python package manager. If you do not have `pyenv`
installed, run the following command.

<details>
  <summary> Install using Homebrew (Darwin) </summary>
  
  ```sh
  brew install pyenv --head
  ```
</details>

<details>
  <summary> Install using standalone installer (Darwin and Linux) </summary>
  
  ```sh
  curl https://pyenv.run | bash
  ```
</details>

If you do not have `uv` installed, run the following command.

<details>
  <summary> Install using Homebrew (Darwin) </summary>

  ```sh
  brew install uv
  ```
</details>

<details>
  <summary> Install using standalone installer (Darwin and Linux) </summary>

  ```sh
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
</details>


Once you have `pyenv` Python version manager installed, you can
install any version of Python above version 3.9 for this project.
The following commands help you set up and activate a Python virtual
environment where `uv` can download project dependencies from the `PyPI`
open-sourced registry defined under `pyproject.toml` file.

<details>
  <summary> Set up environment and synchroniz project dependencies </summary>

  ```sh
  pyenv shell 3.11.9
  uv venv  --python-preference system
  source .venv/bin/activate
  uv sync --dev
  ```
</details>

### Development dependencies

This project has two development dependencies as such:

* [mypy](https://github.com/python/mypy) - Optional static typing for Python
* [ruff](https://github.com/astral-sh/ruff) - An extremely fast Python linter and
  code formatter, written in Rust.

Recommended usage of said development dependencies.

```sh
$ mypy .
> ... # A mypy cache folder will be created on root directory under the name `.mypy_cache`
$ ruff format .
> ... # Python files will be formatted according to the rules defined in `pyproject.toml` with cache under `.ruff`
```

## Roadmap

* Add command to list richmenus as found on this documentation [section.](https://developers.line.biz/en/reference/messaging-api/#validate-rich-menu-object)
* Add command to check if given YAML-file is a valid richmenu as found on this documentation [section.](https://developers.line.biz/en/reference/messaging-api/#validate-batch-control-rich-menus-request)
* Add command to download previously uploaded RichMenu image. as found on this documentaion [section.](https://developers.line.biz/en/reference/messaging-api/#download-rich-menu-image)

## Appendix

1. [LINE Developers - Area objects](https://developers.line.biz/en/reference/messaging-api/#area-object)
2. [LINE Developers - Action objects](https://developers.line.biz/en/reference/messaging-api/#action-objects)
3. [LINE Developers - Bounds objects](https://developers.line.biz/en/reference/messaging-api/#bounds-objects)
4. [LINE Developers - Rich menu objects](https://developers.line.biz/en/reference/messaging-api/#rich-menu-object)

## License

This project is licensed under the terms of the MIT license.

