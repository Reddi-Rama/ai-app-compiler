def detect_ambiguity(prompt):
    
    prompt = prompt.lower().strip()

    vague_keywords = [
        "app",
        "platform",
        "software",
        "system",
        "website"
    ]

    vague_starters = [
        "build",
        "create",
        "make",
        "develop"
    ]

    for starter in vague_starters:

        for keyword in vague_keywords:

            if starter in prompt and keyword in prompt:

                word_count = len(prompt.split())

                # Only trigger if prompt is too short/vague
                if word_count <= 4:

                    return {
                        "clarification_needed": True,
                        "questions": [
                            "What type of application do you want to build?",
                            "What main features should the system include?"
                        ]
                    }

    return {
        "clarification_needed": False
    }