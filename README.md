# awful-cadence-populator
A bad database populator for Cadence Radio used for testing while a real populator is in development

Seriously, don't use this in production. It's worthless.

## Commandline

`python populate.py <config path> [<default config path>] <music path>`

`<config path>` is the path to a configuration file as used for [cadence-server](https://github.com/za419/cadence-server), which includes all the settings specified there as pertaining to the database.

`<music path>` is the path to the root of a directory containing music files which can be served by Liquidsoap - In other words, the path to the root of the directory to be searched for music with which to populate the database.

If passed, `<default config path>` is the path to a configuration file as used for [cadence-server](https://github.com/za419/cadence-server), which serves as a default file which the file pointed to by `<config path>` overrides.
