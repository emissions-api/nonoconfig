# Nonoconfig

*Zero configuration* configuration library.

## Installation

Install this library using:

```
%> pip install nonoconfig
```

## Usage

```python
# $ cat ~/.config.yaml
# key:
#   subkey: value
>>> import nonoconfig
# Initialize the module with a given list of possible configuration file locations
>>> nonoconfig.init("./config.yaml", "~/.config.yaml", "/etc/config.yaml")
# Get values from the first existing location with
>>> nonoconfig.config()
{'key': {'subkey': 'value'}}
# Get parts of the config
>>> nonoconfig.config("key")
{'subkey': 'value'}
>>> nonoconfig.config("key", "subkey")
'value'
# Fetch non existing key
>>> nonoconfig.config("this", "key", "does", "not", "exists")
# Returns None
