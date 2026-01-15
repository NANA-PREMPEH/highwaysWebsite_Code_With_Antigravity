from sqlalchemy import create_engine, inspect

uri = "mysql+pymysql://root:root@localhost/for_antigravity"
engine = create_engine(uri)
insp = inspect(engine)
try:
    cols_gallery = [c['name'] for c in insp.get_columns('gallery')]
    print(f"Gallery columns: {cols_gallery}")
    cols_completed = [c['name'] for c in insp.get_columns('completed_proj')]
    # Check for a few columns that were threatened to be dropped
    threatened = ['pay_made_to_date', 'variations', 'time_elapsed_p']
    present = [c for c in cols_completed if c in threatened]
    print(f"CompletedProj threatened columns present: {present}")
except Exception as e:
    print(e)
