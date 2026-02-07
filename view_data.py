import sqlite3
import os

def view_all_calls():
    # Find health.sqlite - it's stored in the Frontend folder
    # This works from any starting directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check if we're in the root, look in Frontend folder
    db_path = os.path.join(script_dir, "Front-End (IVR system)", "health.sqlite")
    
    # If not found and we're in Frontend, look in current directory
    if not os.path.exists(db_path):
        alt_path = os.path.join(script_dir, "health.sqlite")
        if os.path.exists(alt_path):
            db_path = alt_path
    
    if not os.path.exists(db_path):
        print(f"Error: health.sqlite not found.")
        print(f"Searched in:")
        print(f"  - {os.path.join(script_dir, 'Front-End (IVR system)', 'health.sqlite')}")
        print(f"  - {os.path.join(script_dir, 'health.sqlite')}")
        print(f"\nMake sure you run the IVR app first: python \"Front-End (IVR system)/main.py\"")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM ivr_calls ORDER BY id DESC")
        rows = cursor.fetchall()
        
        if not rows:
            print("No records found in the database.")
            return
        
        # Get column names
        cursor.execute("PRAGMA table_info(ivr_calls)")
        columns = [col[1] for col in cursor.fetchall()]
        
        print("\n" + "="*160)
        print("IVR CALL RECORDS".center(160))
        print("="*160)
        
        for i, row in enumerate(rows, 1):
            print(f"\n[Record {i}]")
            for col, val in zip(columns, row):
                if col == "past_surgery":
                    val = "Yes" if val == 1 else "No"
                print(f"  {col:20s}: {val}")
        
        print("\n" + "="*160)
        print(f"Total Records: {len(rows)}".center(160))
        print("="*160 + "\n")
        
    except Exception as e:
        print(f"Error reading database: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    view_all_calls()