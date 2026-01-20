from sqlalchemy import create_engine, inspect

# Using the remote URI provided by the user in config.py
uri = "mysql+pymysql://highwaysgov_desktopuser:@desktopuser@197.253.67.106/highwaysgov_db_v1"
engine = create_engine(uri)
insp = inspect(engine)
try:
    print(f"Checking database: {uri.split('@')[-1]}")
    if 'gallery' in insp.get_table_names():
        cols_gallery = [c['name'] for c in insp.get_columns('gallery')]
        print(f"Gallery columns: {cols_gallery}")
    else:
        print("Table 'gallery' does not exist.")

    if 'completed_proj' in insp.get_table_names():
        cols_completed = [c['name'] for c in insp.get_columns('completed_proj')]
        threatened = ['pay_made_to_date', 'variations', 'time_elapsed_p']
        present = [c for c in cols_completed if c in threatened]
        print(f"CompletedProj threatened columns present: {present}")
    else:
         print("Table 'completed_proj' does not exist.")
         
except Exception as e:
    print(f"Error: {e}")
