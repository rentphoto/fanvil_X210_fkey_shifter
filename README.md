# fanvil_X210_fkey_shifter
This Python program is written to shift the function keys (fkey) on the side panel of the IP phone Fanvil X210. For example, there is a panel with the page number 1, and fkeys from 1 to 31 are filled on it. You want to move all 31 fkeys to the end of the page, and write a new contact to the first fkey. Through the web interface, this is done for a long time and the probability of an error is high. I suggest downloading the phone's configuration file in XML format, making changes to it using a script, and getting the file with the fkeys shifted at the output. In our example, when starting the program:
- input the fkey number 1, from which we start the shift
- input the fkey number 31, which will move last
- the page number of the panel on which the shift will be made
- the name of the file with the phone's original configuration. 

The output file will not contain fkey 1, and there will be two fkeys with the number 32. You need to manually add the first fkey, and remove the extra one with the number 32.
