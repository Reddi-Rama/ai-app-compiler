def detect_ambiguity(prompt):

    prompt = prompt.lower()

    vague_words = [
        "app",
        "platform",
        "system",
        "website",
        "software"
    ]

    strong_keywords = [
        "login",
        "payment",
        "dashboard",
        "analytics",
        "billing",
        "records",
        "chat",
        "admin",
        "tracking",
        "delivery",
        "crm",
        "hospital",
        "ecommerce",
        "management",
        "ai",
        "subscription"
    ]

    has_strong_context = any(
        keyword in prompt
        for keyword in strong_keywords
    )

    word_count = len(prompt.split())

    if word_count <= 2 and not has_strong_context:

        return {
            "clarification_needed": True,
            "questions": [
                "What type of application do you want to build?",
                "What core features should the application include?"
            ]
        }

    if (
        any(word == prompt.strip() for word in vague_words)
        and not has_strong_context
    ):

        return {
            "clarification_needed": True,
            "questions": [
                "Can you describe the application in more detail?",
                "What main features should it contain?"
            ]
        }

    return {
        "clarification_needed": False,
        "questions": []
    }

