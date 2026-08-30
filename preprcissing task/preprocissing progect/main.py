from preprocessing import read_data_file
from preprocessing import drop_unnecessary_features
from preprocessing import check_data_type
from config import cols_to_drop
file_path = "titanic.csv"
df = read_data_file(file_path)
if df is not None:
    print(df.head())
    user_input = input("enter columns to remove separated by comma: ")
    if user_input:
        cols_to_drop = [col.strip() for col in user_input.split(",")]
    df = drop_unnecessary_features(df, cols_to_drop)
    result = check_data_type(df)
    print(result)