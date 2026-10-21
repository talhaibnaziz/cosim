import matplotlib.pyplot as plt
import re
import argparse
import numpy as np


METRICS = (
	"simulator_pflow::event count:",
	"NS3Netsim::event count:",
	"NS3Netsim::relevant event count:",
	"simulator_controller::event count:",
)

pflow_xpoints = []
pflow_ypoints = []
ns3_xpoints = []
ns3_ypoints = []
ns3_3_xpoints = []
ns3_3_ypoints = []
control_xpoints = []
control_ypoints = []

def extract_events(file_name):
    for line in open(file_name, "r").readlines():
        for metric in METRICS:
            if re.search(metric, line):
                extracted = line.split(metric)[1]
                numbers = re.findall(r'\d+', extracted)
                event_count = int(numbers[1]) - int(numbers[0])
                time = int(numbers[2])
                if (time > 40000 or time < 39800): continue
                if (metric == METRICS[0]):
                    pflow_xpoints.append(time)
                    pflow_ypoints.append(event_count)
                elif (metric == METRICS[1]):
                    ns3_xpoints.append(time)
                    ns3_ypoints.append(event_count)
                elif (metric == METRICS[2]):
                    ns3_3_xpoints.append(time)
                    ns3_3_ypoints.append(event_count)
                elif (metric == METRICS[3]):
                    control_xpoints.append(time)
                    control_ypoints.append(event_count)

def extract_events_ns(file_name, file_name_3):
    for line in open(file_name, "r").readlines():
        for metric in METRICS:
            if re.search(metric, line):
                extracted = line.split(metric)[1]
                numbers = re.findall(r'\d+', extracted)
                event_count = int(numbers[1])
                time = int(numbers[2])
                if (time > 40000 or time < 39000): continue
                if (metric == METRICS[1]):
                    ns3_xpoints.append(time)
                    ns3_ypoints.append(event_count)

    for line in open(file_name_3, "r").readlines():
            for metric in METRICS:
                if re.search(metric, line):
                    extracted = line.split(metric)[1]
                    numbers = re.findall(r'\d+', extracted)
                    event_count = int(numbers[1])
                    time = int(numbers[2])
                    if (time > 40000 or time < 39000): continue
                    if (metric == METRICS[1]):
                        ns3_3_xpoints.append(time)
                        ns3_3_ypoints.append(event_count)

def main():
    parser = argparse.ArgumentParser(description='analyze simulation results')
    parser.add_argument('--file', type=str, help='name of output file containing simulation results')
    parser.add_argument('--file3', type=str, help='second output file for ns3 stage 3 only', default=None, required=False)
    file_name = parser.parse_args().file
    file_name_3 = parser.parse_args().file3

    if file_name_3 != None:
        extract_events_ns(file_name, file_name_3)

        xpoints = np.array(ns3_xpoints)
        ypoints = np.array(ns3_ypoints)
        plt.plot(xpoints, ypoints, 'o', label='NS-3 Stage 2')

        xpoints = np.array(ns3_3_xpoints)
        ypoints = np.array(ns3_3_ypoints)
        plt.plot(xpoints, ypoints, '.', label='NS-3 Stage 3')

        plt.xlabel("Simulated Time (ms)")
        plt.ylabel("Total Events")
        plt.title("NS-3 Total Event Count vs Time")
        plt.legend()
        
        plt.savefig("ns3.pdf", format="pdf")

    else:
        extract_events(file_name)

        xpoints = np.array(pflow_xpoints)
        ypoints = np.array(pflow_ypoints)
        plt.plot(xpoints, ypoints, 'x', label='PFlow')

        xpoints = np.array(ns3_xpoints)
        ypoints = np.array(ns3_ypoints)
        plt.plot(xpoints, ypoints, 'o', label='NS-3 non-trigger')

        xpoints = np.array(ns3_3_xpoints)
        ypoints = np.array(ns3_3_ypoints)
        plt.plot(xpoints, ypoints, 'o', color='k', label='NS-3 trigger')

        xpoints = np.array(control_xpoints)
        ypoints = np.array(control_ypoints)
        plt.plot(xpoints, ypoints, '.', label='Controller')

        plt.xlabel("Simulated Time (ms)")
        plt.ylabel("Number of Events")
        plt.gca().set_ylim([0, 25])
        plt.title("Stage 2 Federate Event Count vs Time")
        plt.legend()
        
        plt.savefig("stage_2.png", format="png")


if __name__ == "__main__":
	main()
