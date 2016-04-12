# door

shorts pin `17` to ground when status code `200` received from `<endpoint>`.


## Setup
```
# apt-get install git python3-pip python3-gpiozero
# pip3 install requests
```


## Usage
```
$ python3 door.py <endpoint> <user-id>
```

An HTTP POST request will be sent to `<endpoint>` containing JSON in the form of:
```
{
  'userId' : <user-id>
}
```

If the wrong number of command line args are supplied the script will exit with code 1, else code 0.


## License
Copyright 2016 Rhodey Orbits
Licensed under the GPLv3: http://www.gnu.org/licenses/gpl-3.0.html

