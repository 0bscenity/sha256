print('made by grapes🍇')
import os,hashlib,csv
directory_2_scan = input('please input FULL directory path, DO NOT INCLUDE "⧵" AT THE END OF THE PATH OR IT WILL NOT WORK!: ')
csv_out = input('name of the output file (ex, sha256.csv): ')

if not csv_out.endswith('.csv'):
    csv_out += '.csv'

def calc_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()


def scan_dir(directory):
    print(f'scanning {directory} and calculating the hash(es)')
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            sha256 = calc_sha256(file_path)
            results.append((file, sha256))
    return results


def export_2_csv(results, output_file):
    print('exporting')
    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['file name', 'sha256'])
        for file_name, sha256 in results:
            writer.writerow([file_name, sha256])

if __name__ == '__main__':
#     uncomment if you want to remove the user choise of output file name. csv_out = 'output_sha256.csv'
    results = scan_dir(directory_2_scan)
    export_2_csv(results, csv_out)

    print(f'list has been exported to {csv_out}')
