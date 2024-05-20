print(f'made by grapes')
import os
import hashlib
import csv

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def scan_directory(directory):
    """scan"""
    print(f"scanning directory and calculating the hash(es)")
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            sha256 = calculate_sha256(file_path)
            results.append((file, sha256))
    return results


def export_to_csv(results, output_file):
    print(f"exporting")
    """export"""
    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["file name", "sha256"])
        for file_name, sha256 in results:
            writer.writerow([file_name, sha256])


if __name__ == "__main__":
    """variables"""
    # keep r string otherwise it won't scan
    directory_to_scan = r"C:\Usersraden\XXXXXXXX"  # change directory. might only work if this script is on the same drive as path
    output_csv_file = "output_sha256.csv"
    results = scan_directory(directory_to_scan)
    export_to_csv(results, output_csv_file)

    print(f"list has been exported to {output_csv_file}")
