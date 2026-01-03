def enhance_prompt(user_prompt: str, domain: str):
    domain_prompts = {
        "human": "realistic human anatomy, anatomical accuracy, neutral pose, 3D model",
        "mechanical": "detailed mechanical parts, engineering design, CAD style 3D model",
        "furniture": "modern furniture design, realistic materials, 3D object",
        "architecture": "architectural structure, realistic building design, 3D model"
    }

    return f"{user_prompt}, {domain_prompts.get(domain, '')}"
