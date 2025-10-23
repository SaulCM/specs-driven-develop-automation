import time

def run_with_retry(agent_func, *args, max_retries=3, delay=10):
    for attempt in range(max_retries):
        try:
            return agent_func(*args)
        except Exception as e:
            print(f"Error: {e} (attempt {attempt+1}/{max_retries})")
            time.sleep(delay)
    raise RuntimeError("Max retries exceeded")