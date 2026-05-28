def detect_ambiguity(prompt):
    
    prompt = prompt.lower().strip()

    vague_prompts = [
        "build a platform",
        "create a platform",
        "build platform",
        "create platform",

        "build an app",
        "create an app",
        "build app",
        "create app",

        "build software",
        "create software",

        "build a system",
        "create a system",

        "build a website",
        "create a website"
    ]

    if prompt in vague_prompts:

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