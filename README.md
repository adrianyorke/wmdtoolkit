# Wealth Managment Data Toolkit (`wmdtoolkit`)

Wealth Management Data Toolkit library (`wmdtoolkit`) is used to implement common data engineering functions and classes.

`wmdtoolkit` is implemented technically as a Python package. 

> "You can think about a package as a toolbox filled with coding tools.
> A tool may be a function or a class. Each tool does a specific thing well."
[[1]](https://www.pyopensci.org/python-package-guide/tutorials/intro.html#python-toolbox)

> "A package in any language is more than just code.
> If you expect other people to use your package, besides yourself,
> you should consider not only writing high quality code,
> but also the various elements of a package that make it a useful community resource."
[[2]](https://www.pyopensci.org/python-package-guide/tutorials/intro.html)

## Useful links:
- [Markdown Editor](https://dillinger.io/)
- [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)
- [Python Package Guide](https://www.pyopensci.org/python-package-guide/tutorials/intro.html)

## Who will be using this toolkit?
- Wealth Management Data Engineering teams
- Other Data Engineering teams at OP who would like to leverage rapid start with Azure-based OP Data Platform (OPDP) apps.

## How will people use this toolkit?
- Typically, WM Data Tookit will be imported by Azure Catapult applications using OP Data Platform.
- Only the relevant subpackages, functions or classes will be imported - not the whole library.

## How about documentation and tests?
- This is a shared library so both documentation and tests are required.
- Target test coverage is 100%.
- Documentation should explain how to use subpackages, and also provide sample code.

## How is the tookit maintained and by whom?
- At OP, we have this concept of "Inner Source". Similar to Open Source (FOSS) but intended for development of software for our internal community.
- Initially, a base set of functionality will be provided.
- Regular maintenance and feature upgrades are expected, especially during the first 3 years, at least until 31.12.2027.
- Many Data Engineers will contribute to the toolkit and provide enhancements, support & general maintenance.
- Data Engineers outside Wealth Management are also welcome to contribute.
