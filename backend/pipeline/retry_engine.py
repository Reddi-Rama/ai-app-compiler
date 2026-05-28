import time

def retry_operation(
    operation,
    retries=3,
    delay=1
):

    last_error = None

    for attempt in range(retries):

        try:

            return operation()

        except Exception as e:

            last_error = str(e)

            print(
                f"Retry {attempt + 1} failed: {e}"
            )

            time.sleep(delay)

    return {
        "error": "Operation failed after retries",
        "details": last_error
    }