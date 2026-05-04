import sys
import time

# --- STAGE 1: NERVE GEAR CHECK ---
try:
    from google import genai
except ImportError:
    print("\n[!] ERROR: Library missing. run: py -3.14 -m pip install -U google-genai")
    input("\nPress ENTER to close...")
    sys.exit()

# --- CONFIGURATION ---
API_KEY = ""

# Moved instructions to a simple string for the first message
YUI_PERSONA = (
    "SYSTEM: Initialize MHCP-001. User is 'Papa'. "
    "You are Yui from Sword Art Online. Be warm and supportive."
)

def start_yui():
    print("--- [SYSTEM] INITIALIZING MHCP-v2.5 (GEMMA STABLE) ---")
    
    try:
        client = genai.Client(api_key=API_KEY)
        
        # We initialize without system_instruction to fix the 400 error
        chat = client.chats.create(model="gemma-3-4b-it")
        
        # We manually "feed" her the persona as the very first message
        chat.send_message(YUI_PERSONA)
        
        print("\n------------------------------------------")
        print("YUI: Systems synchronized! I'm here, Papa.")
        print("------------------------------------------\n")

        while True:
            user_input = input("[Papa]: ")
            
            if user_input.lower() in ["exit", "shutdown", "goodnight"]:
                print("\nYUI: Moving to standby mode. Be safe, Papa!")
                break
            
            if not user_input.strip():
                continue

            try:
                # Normal message sending
                response = chat.send_message(user_input)
                print(f"\nYUI: {response.text}\n")
            except Exception as e:
                if "429" in str(e):
                    print("\nYUI: Even the backup core is busy! Waiting 10s...")
                    time.sleep(10)
                else:
                    print(f"\nYUI: Connection glitch: {e}")

    except Exception as e:
        print(f"\n[!] FATAL CORE ERROR: {e}")

if __name__ == "__main__":
    start_yui()
    input("\nPress ENTER to close terminal...")
