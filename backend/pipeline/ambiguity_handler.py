def detect_ambiguity(prompt):
    
    vague_words = [
        "platform",
        "app",
        "system",
        "website",
        "portal"
    ]

    prompt_lower = prompt.lower()

    clarification_needed = False
    questions = []

    for word in vague_words:

        if prompt_lower.strip() == f"build a {word}" \
        or prompt_lower.strip() == f"create a {word}" \
        or prompt_lower.strip() == word:

            clarification_needed = True

    if clarification_needed:

        questions = [
            "What type of system do you want to build?",
            "What core features should the application include?"
        ]

    return {
        "clarification_needed": clarification_needed,
        "questions": questions
    }