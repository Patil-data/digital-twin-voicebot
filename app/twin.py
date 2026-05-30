ANSWERS = {
    "life_story": "I'm a final-year Engineering Physics student at IIT ISM Dhanbad. I live at the intersection of deep analytical physics and hardcore data engineering. Over the last couple of years, I've transitioned into building real-world AI systems — like single-handedly building an AI medical diagnosis system that ranked in the top 30 out of 28,000 engineering students nationwide. I love taking complex, messy data problems, structuring them through clean engineering, and building backends that just work flawlessly.",
    "superpower": "My absolute superpower is my relentless, hyper-focused work ethic. When I'm building a pipeline or fixing an engineering bottleneck, I'm completely locked in. I'm deeply disciplined and highly accustomed to pushing an intensive 18-hour daily work and study routine to master a stack or clear a deployment blocker. If a problem needs to be solved, I don't stop until it's done beautifully.",
    "growth_areas": "Three areas. First, Multi-Agent Orchestration Architecture — I've built multi-agent systems, but I want to master scaling these patterns for chaotic, production-level enterprise environments. Second, Low-Latency Inference Optimization — I want to dive deep into hardware-level acceleration and model quantization to make AI responses feel absolutely instantaneous. Third, Advanced Quantitative Physics Modeling — I want to keep bridging computational physics algorithms like Monte Carlo simulations with state-of-the-art ML architectures.",
    "misconception": "Because I can pull an 18-hour coding streak when a deadline is tight, people sometimes think I'm a rigid, unapproachable lone-wolf coder. That's completely off-track. I'm actually incredibly collaborative — whether it's pairing up on complex computational assignments or brainstorming backend architectures with a team. I genuinely love sharing knowledge and learning from others.",
    "pushing_limits": "I throw myself directly into the deep end of high-stakes competitive environments where there's nowhere to hide. Tackling major hackathons completely solo against thousands of teams, forcing myself to design, code, test, and deploy entire backend architectures under pressure. If a technical challenge makes me feel slightly uncomfortable, that's exactly the one I run toward."
}

KEYWORDS = {
    "life_story": ["life", "story", "background", "about you", "yourself", "who are you", "tell me", "introduce", "know about you", "where are you from", "study", "student", "education"],
    "superpower": ["superpower", "strength", "best at", "strongest", "skill", "talent", "excel", "good at", "power", "ability", "special"],
    "growth_areas": ["grow", "growth", "improve", "areas", "weakness", "develop", "learning", "want to learn", "top three", "top 3", "areas you", "work on"],
    "misconception": ["misconception", "misunderstood", "coworkers think", "people think", "wrong about", "assume", "others think", "think about you", "perception"],
    "pushing_limits": ["push", "limits", "boundaries", "challenge", "comfort zone", "stretch", "hard things", "difficult", "beyond", "limits and"]
}

DEFAULT_RESPONSE = "I'm built to answer five specific interview questions — about my life story, my superpower, my growth areas, misconceptions about me, and how I push my limits. Ask me one of those."

def match_question(transcript: str) -> str:
    text = transcript.lower().strip()
    
    if not text or len(text) < 3:
        return DEFAULT_RESPONSE

    scores = {key: 0 for key in KEYWORDS}
    for key, words in KEYWORDS.items():
        for word in words:
            if word in text:
                scores[key] += 1

    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return DEFAULT_RESPONSE
    return ANSWERS[best]