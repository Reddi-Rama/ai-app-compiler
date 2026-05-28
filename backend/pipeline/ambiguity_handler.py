def detect_ambiguity(prompt):
    
    prompt = prompt.lower()

    vague_keywords = [
        "platform",
        "app",
        "software",
        "system",
        "website"
    ]

    clarification_needed = False

    for word in vague_keywords:

        if prompt.strip() in [
            f"build a {word}",
            f"create a {word}",
            f"build {word}",
            f"create {word}"
        ]:

            clarification_needed = True

    if clarification_needed:

        return {
            "clarification_needed": True,
            "questions": [
                "What type of system do you want to build?",
                "What core features should the application include?"
            ]
        }

    return {
        "clarification_needed": False
    }