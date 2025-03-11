import re
import pandas as pd

LOG_FILE = "streaming_logs.txt"

ERROR_PATTERNS = {
    "bitrate_drop": re.compile(r"WARNING Bitrate drop detected: (\d+) kbps → (\d+) kbps"),
    "buffering": re.compile(r"ERROR Buffering issue detected \(duration: (\d+)s\)"),
    "encoding": re.compile(r"ERROR Encoding failure - (.+)")
}

def analyze_logs():
    """Scans log file and summarizes detected streaming issues."""
    issues = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            timestamp = line.split("]")[0][1:]
            for issue_type, pattern in ERROR_PATTERNS.items():
                match = pattern.search(line)
                if match:
                    issues.append({"timestamp": timestamp, "issue_type": issue_type, "details": match.groups()})

    if issues:
        df = pd.DataFrame(issues)
        print("\n🔴 Detected Streaming Issues:\n", df)
    else:
        print("✅ No critical issues detected.")

if __name__ == "__main__":
    analyze_logs()
