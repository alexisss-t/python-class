import time
import sys

def the_thing():
    print("Checking for system updates...")
    time.sleep(1.5)
    print("\n[!] CRITICAL ERROR: Multiple security breaches detected.")
    time.sleep(1)
    print("[!] Unauthorized access to /Users/Shared/Private_Photos")
    time.sleep(1.2)
    print("[!] Initiating remote wipe to protect data...")
    time.sleep(1.5)
    files = ["System32", "Browser_History", "Passwords"]
    for file in files:
        sys.stdout.write(f"\rDeleting {file}...")
        sys.stdout.flush()
        time.sleep(0.7)
        sys.stdout.write(f"\rDeleted {file}!   ")
        sys.stdout.flush()
        time.sleep(0.3)
    for i in range(11):
        percent = i * 10
        bar = "#" * i + " " * (10 - i)
        sys.stdout.write(f"\r[{bar}] {percent}% complete")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n\n" + "-"*30)
    print(" APRIL FOOLS! ")
    print("(Your files are fine.)")
    print("-"*30)

if __name__ == "__main__":
    the_thing()