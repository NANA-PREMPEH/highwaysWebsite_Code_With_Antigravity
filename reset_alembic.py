from sqlalchemy import create_engine, text

uri = "mysql+pymysql://root:root@localhost/for_antigravity"
engine = create_engine(uri)
with engine.connect() as conn:
    print("Dropping alembic_version table...")
    try:
        conn.execute(text("DROP TABLE alembic_version"))
        print("Dropped.")
    except Exception as e:
        print(f"Error (maybe table didn't exist): {e}")
