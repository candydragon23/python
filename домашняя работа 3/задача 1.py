ping = input()
received = 0
mini = 1000000
maxi = 0
average = 0


def packets (packet):
    if packet == "Time out":
        return 0
    else:
        return 1


for _ in range(4):
    packet = input()
    received += packets(packet)
    if packets(packet):
       mini = min(mini, int(packet[packet.find("=") + 1:]))
       maxi = max(maxi, int(packet[packet.find("=") + 1:]))
       average += int(packet[packet.find("=") + 1:])
print("Ping statistics for " + ping[5:] + ":")
print("Packets: Sent = 4 Received = " + str(received) + " Lost = " + str(4 - received) + " (" + str((4 - received) * 25) + "% loss)")
if received > 0:
    print("Approximate round trip times:")
    print("Minimum = " + str(mini) + " Maximum = " + str(maxi) + " Average = " + str((average + 2) // received))