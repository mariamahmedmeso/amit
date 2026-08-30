import pandas as pd
def read_data_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("file not found")
    except Exception:
        print("could not read the file")

def drop_unnecessary_features(df, cols_to_drop):
    return df.drop(columns=cols_to_drop)

def check_data_type(df):
    result = pd.DataFrame({
        "datatype": df.dtypes,
        "unique_values": df.nunique()
    })
    
    return result.T