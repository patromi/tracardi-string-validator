# Tracardi plugin: String Validator


The purpose of this plugin is valide data. We need to specify a type of regex. We can choose from:

* email - for example example@mail.com
* url - for example tracardi.com
* ipv4 for example 192.168.1.1
* date for example 01.01.1900
* time for example 01:01
* int for example 3
* float for example 3.4
* number_phone for example +48123456789


# Configuration

This node require configuration.

* validate_regex - Choose a validate regex. 

* data - Here is data what we want to validate

# Examples
```json
  {"validate_regex" : "url",
  "data" : "tracardi.com"}
```
It will return True on output
```json
  {"validate_regex" : "email",
  "data" : "12341232"}
```
It will return False on output

# Input payload

This node does not process input payload.

# Output

This is two output True and False.
