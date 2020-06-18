# virl-MGMT

Python script to add OOBM VRF and interface config on device configurations from INE github V5 labs.  There is a buch of stuff hardcoded
and I didn't follow pep8 rules.

Read all files contained in the topologies subdirectory from where the script is run.  I also have a utils.py file that contains some 
functions I use in my lab load script.  This script relies on the deviceip function in utils to populate the ip address for gig0/0 from hostname(derived from filename)

Open the device configs.
* Adds a MGMT VRF
* Creates a gig0/0 interface and puts it in MGMT VRF
* Creates a default route in MGMT VRF
* Configures http client interface as gig0/0(used to download configs from lab script)
* add no cdp log mismatch duplex to prevent the annoying console messages on GNS3\
* updates VTY 0 4
  * priv level 15
  * password password
  * login
  * transport input all
Then save the file with the same filename.
The script will check if the above configs exist, and not update if exists.
If any of the stops fail, it will catch the exeption and the filename and operation to console so the file can be manually edited.

