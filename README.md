How to enable doctors to gain real-time access to a patient’s vital signs from anywhere in the world?
=================================================================================================
                            COPYRIGHT RR INCORPORATED EST. 2021
=================================================================================================

Before running the program you must install matplotlib using the command: pip install matplotlib
This build is implemented only for x86_64 version of windows (windows 10).

The file can be run by executing "python3 hackathon.py XXX" where XXX is either "doctor" or "patient".
The executable consists of two threads, depending on the command line argument doctor/patient.
The doctor thread will need to be started before the patient thread to establish TCP based connections.

Once both threads are active on the machine(currently it is implemented on the same machine, but it is easily transferrable),
the text file that is being written to by the sensors will be read by the patient thread, encoded and sent to the doctor thread which will decode the data
and then plot the data of the sensors against time.

Functions other than afore mentioned threads:
animate: uses matlab library to plot the sensor data against time updating it in real time. We took some help in library documentation for animating the real time sensors.

We were not able to fully able to implement peer to peer encryption using private and public keys, and have commented it out.

For legal concerns contact RR Legal Division.
