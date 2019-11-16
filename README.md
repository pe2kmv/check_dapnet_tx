# check_dapnet_tx
Python script to have Nagios check the online status of a DAPNET transmitter

## Python version
This script is based on Python 3

## Usage
### From the command line
```
python check_dapnet_tx.py -t ab0cde
```
### Within Nagios
Copy the script to the libexec directory.
Then create a new command in the file commands.cfg
```
define command {
	command_name    check_dapnet_tx
  	command_line	python3 /usr/local/nagios/libexec/check_dapnet.py -t $ARG1$
}
```
Add the status check as service of the DAPNET host by editing the file [hostname].cfg (and add parameters as you like)
```
define service {
        use                     local-service
        host_name               you_host_name
        service_description     DAPNET TX Status
        check_command           check_dapnet_tx!ab0cde
        contact_groups          admins
}
