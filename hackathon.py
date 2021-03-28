import sys
import socket
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# import rsa
# import numpy as np
import time
import threading
import random


fig, axes = plt.subplots(2, 2)

ax1 = axes[0, 0]
ax2 = axes[0, 1]
ax3 = axes[1, 0]


def patient():
    soc = socket.socket()
    soc.connect(("localhost", 20006))
    # pubkey = int(soc.recv(1024).decode("utf-8"))
    # pubkey = (pubkey, int(soc.recv(1024).decode("utf-8")))

    curr_time = 0
    pulse = 72

    temperature = 96
    spO2 = 95

    while True:
        _ = random.SystemRandom()

        vitals = [(curr_time, temperature, curr_time, pulse, curr_time, spO2)]
        for i in vitals:
            print("sending data")
            i = str(i)
            i = removeParentheses(i)
            time.sleep(1)
            # i = rsa.encrypt(i.encode("utf-8"), pubkey)
            soc.send(i.encode("utf-8"))

        curr_time += 1
        pulse += random.uniform(-5, 5)
        temperature += random.uniform(-3, 3)
        spO2 += random.uniform(-0.5, 0.5)

        if spO2 > 100:
            spO2 = 100


def removeParentheses(initial):
    final = ""
    for i in range(len(initial)):
        if initial[i] != ")" and initial[i] != "(":
            # if i % 2 == 0:
            #     final += " "
            final += initial[i]

    return final


def animate(i):
    filedata = open("patient_abc.txt", "r").read()
    datalist = filedata.split('\n')
    xa = []
    ya = []
    for eachLine in datalist:
        # time.sleep(1)
        if len(eachLine) > 1:
            # print("eachLine:    ", eachLine)
            x, y, _, _, _, _ = eachLine.split(',')
            # print("X:", x)
            # print("Y:", y)
            xa.append(float(x))
            ya.append(float(y))

    xa2 = []
    ya2 = []

    for eachLine in datalist:
        # time.sleep(1)
        if len(eachLine) > 1:
            # print("eachLine:    ", eachLine)
            _, _, x, y, _, _ = eachLine.split(',')
            # print("X:", x)
            # print("Y:", y)
            xa2.append(float(x))
            ya2.append(float(y))

    xa3 = []
    ya3 = []

    for eachLine in datalist:
        # time.sleep(1)
        if len(eachLine) > 1:
            # print("eachLine:    ", eachLine)
            _, _, _, _, x, y = eachLine.split(',')
            # print("X:", x)
            # print("Y:", y)
            xa3.append(float(x))
            ya3.append(float(y))

    ax1.clear()
    ax1.set_title("Temp vs time")
    ax1.set(xlabel="time (s)", ylabel="temperature (F)")
    ax1.plot(xa, ya)

    ax2.clear()
    ax2.set_title("Pulse vs time")
    ax2.set(xlabel="time (s)", ylabel="pulse (BPM)")
    ax2.plot(xa2, ya2)

    ax3.clear()
    ax3.set_title("SpO2 vs time")
    ax3.set(xlabel="time (s)", ylabel="SpO2 (%)")
    ax3.plot(xa3, ya3)


# [(heart rate sys, heart rate dia), pulse, spO2, temperature]


def doctor():
    # (pubkey, privkey) = rsa.newkeys(512)
    f = open("patient_abc.txt", "w")
    f.write("0, 0, 0, 0, 0, 0")
    f.write('\n')
    f.close()

    threading.Thread(target=doctorThread).start()
    doctorApi()


def doctorThread():
    soc = socket.socket()
    soc.bind(("localhost", 20006))
    soc.listen()
    client_skt, _ = soc.accept()
    # print(pubkey)
    # print(type(pubkey))
    # soc.send(str(pubkey[0]).encode("utf-8"))
    # soc.send(str(pubkey[1]).encode("utf-8"))

    while True:
        message = client_skt.recv(1024)
        # message = rsa.decrypt(message, privkey)
        message = message.decode("utf-8")
        print("recieving data")
        # print(message)
        f = open("patient_abc.txt", "a")
        f.write(message)
        f.write('\n')
        f.close()


def doctorApi():
    # fig, ax = plt.subplots(4)
    _ = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()
    # return ""


def main():
    working_mode = sys.argv[1]  # can be doctor or patient
    print(working_mode)
    if working_mode == "doctor":
        doctor()
    elif working_mode == "patient":
        patient()
    else:
        print("Incorrect working mode. Program exited")


main()
