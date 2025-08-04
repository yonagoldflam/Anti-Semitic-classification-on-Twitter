import json
import pandas as pd

class WriteDataFiles:
    def write_to_json_file(dict, filename):
        with open(f'../data/{filename}', 'w') as f:
            json.dump(dict, f)

    def write_to_csv_file(df, filename):
        df.to_csv(f'../data/{filename}', index=False)
