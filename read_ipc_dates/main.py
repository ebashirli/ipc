import pandas as pd
from pathlib import Path



# 1. Define the root directory and the sheet name
root_dir = Path(r"\\DATA\DataServer\Teknik Ofis\00_SPP2 Taseron Sozlesmeleri")
target_sheet = "IPC Cover"  # Or use an index like 0 for the first sheet

my_list =   [ 
    # "011",  "014",  "030",  "030",  "031",  "031", 
    "033"
    # ,  "046",  "046",  "046",  "046",  "046",  "046",  "046",  "050",  "051",  "051",  "051",  "051",  "051",  "051",  "051",  "052",  "052",  "065",  "065",  "085",  "091",  "094",  "094",  "095",  "098",  "099",  "100",  "100",  "102",  "102",  "102",  "102",  "103",  "107",  "110",  "115",  "121",  "124",  "141",  "150",  "117",  "163",  "164",  "172",  "173",  "179",  "182",  "182" 
    ] 

all_data = []

def read_excel_files():
    # 2. Recursively find all .xlsx and .xls files
    for file_path in root_dir.rglob("*.xlsx"):
        contract_no = str(file_path)[59:62]

        if not (contract_no in my_list):
            continue
            
        try:
           contract_no_in_name = file_path.name.split("-")[0]
           print(f"contract_no_in_name: {contract_no_in_name}")
        #    if not (contract_no_in_name in my_list):
        #         continue
           
           
           print(f"Reading {file_path.name}...")
           df = pd.read_excel(file_path,sheet_name=0,usecols="J:L",skiprows=3,nrows=3,header=None)
           df['source_file'] = file_path.name
           all_data.append(df)
            
        except Exception as e:
            print(f"Could not read {file_path.name}: {e}")

    # 4. Combine everything into one big DataFrame
    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        final_df.to_excel("consolidated_ipc_dates.xlsx", index=False)
        print("Consolidation complete!")
    else:
        print("No matching files or sheets found.")

def main():
    read_excel_files()
    print("Hello from read-ipc-dates!")


if __name__ == "__main__":
    main()
