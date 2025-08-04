import json

class WriteDataFiles:
    def write_to_json_file(dict, anlyzed_data_url):
        with open(anlyzed_data_url, 'w') as f:
            json.dump(dict, f)

    def write_to_csv_file(df, cleaned_data_url):
        df.to_csv(cleaned_data_url, index=False)
