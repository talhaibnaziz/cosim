from pathlib import Path
import re
import statistics
import argparse


METRICS = (
	"simulator_pflow::finalize:total execution time =",
	"Estimator::finalize:total execution time =",
	"NS-3 Loop execution time total:",
	"NS-3 communication time:",
	"Collector::finalize:total execution time =",
	"simulation took",
)

def get_measurements(file_name):
    metrics = {}

    for line in open(file_name, "r").readlines():
        for metric in METRICS:
            if metric not in metrics.keys(): metrics[metric] = []
            if re.search(metric, line):
                number_text = re.sub(metric, "number ", line)
                metrics[metric].append(float(re.search(r"\d+\.?\d*", number_text).group()))

    return metrics

def main():
    parser = argparse.ArgumentParser(description='analyze simulation results')
    parser.add_argument('--file', type=str, help='name of output file containing simulation results')
    file_name = parser.parse_args().file
    metrics = get_measurements(file_name)

    for metric, values in metrics.items():
        if not values:
            print(f"{metric}: no values found")
            continue
        print(
			f"{metric} count={len(values)}, "
			f"average={statistics.fmean(values):.6f}, "
			f"max={max(values):.6f}, min={min(values):.6f}"
		)


if __name__ == "__main__":
	main()
