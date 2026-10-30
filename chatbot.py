
# SJCIT AI COLLEGE CHATBOT
# Chatbot logic for the website

COLLEGE_WEBSITE = "https://sjcit.ac.in/"

DEPARTMENTS = {
    "1": "Computer Science and Engineering (CSE)",
    "2": "Artificial Intelligence and Machine Learning (AI & ML)",
    "3": "Artificial Intelligence and Data Science (AI & DS)",
    "4": "Electronics and Communication Engineering (ECE)",
    "5": "Aerospace Engineering",
    "6": "Aeronautical Engineering",
    "7": "Mechanical Engineering",
    "8": "Civil Engineering",
    "9": "Information Science and Engineering (ISE)"
}

MENU_OPTIONS = {
    "1": "Courses and syllabus",
    "2": "Fee structure",
    "3": "Exams and timetable",
    "4": "Faculty information",
    "5": "Placements and careers",
    "6": "Department website",
    "7": "Ask a question"
}


def get_menu_response(choice, department):

    responses = {
        "1": (
            f"Explore courses and subjects for {department}.\n"
            "Check the official syllabus:\n"
            "https://sjcit.ac.in/scheme-and-syllabus/"
        ),

        "2": (
            "Fees depend on the course and admission category.\n"
            "Please verify the latest details with the college:\n"
            + COLLEGE_WEBSITE
        ),

        "3": (
            "Check official exam notices and academic calendars:\n"
            "https://sjcit.ac.in/academic-information/"
        ),

        "4": (
            f"Find faculty information for {department} "
            "through the official college website:\n"
            + COLLEGE_WEBSITE
        ),

        "5": (
            "Contact the placement cell for training, "
            "company visits and eligibility information:\n"
            + COLLEGE_WEBSITE
        ),

        "6": (
            "Official SJCIT website:\n" + COLLEGE_WEBSITE
        )
    }

    if choice in responses:
        return responses[choice]

    return "Please select a valid option."


def get_response(question, department):

    question = question.lower().strip()

    if not question:
        return "Please type a question."

    if any(word in question for word in
           ["hello", "hi", "hey"]):
        return f"Hello! How can I help you with {department}?"

    if any(word in question for word in
           ["academic calendar", "academic calender",
            "college calendar"]):
        return (
            "Find the official academic calendar here:\n"
            "https://sjcit.ac.in/academic-information/"
        )

    if "data science" in question or "about ai" in question:
        return (
            "AI and Data Science combines computing, "
            "statistics, data analysis and artificial intelligence.\n"
            "Learn more:\n"
            "https://sjcit.ac.in/artificial-intelligence-and-data-science/"
        )

    if any(word in question for word in
           ["fee", "fees", "payment", "pay", "cost"]):
        return (
            "Fees depend on the course and admission quota. "
            "Please verify the current details:\n"
            + COLLEGE_WEBSITE
        )

    if any(word in question for word in
           ["exam", "exams", "test", "timetable", "schedule"]):
        return (
            "Check official college notices for examination dates "
            "and timetables:\n"
            "https://sjcit.ac.in/academic-information/"
        )

    if any(word in question for word in
           ["course", "courses", "syllabus", "subject",
            "subjects", "study materials"]):
        return (
            f"Check course and syllabus information for {department}:\n"
            "https://sjcit.ac.in/scheme-and-syllabus/"
        )

    if any(word in question for word in
           ["faculty", "teacher", "teachers", "professor"]):
        return (
            f"Find faculty details for {department} here:\n"
            + COLLEGE_WEBSITE
        )

    if any(word in question for word in
           ["placement", "placements", "job", "jobs",
            "career", "company", "companies"]):
        return (
            "Contact the placement cell for training, "
            "eligibility and company updates:\n"
            + COLLEGE_WEBSITE
        )

    if any(word in question for word in
           ["website", "link", "official site", "college site"]):
        return "Official SJCIT website:\n" + COLLEGE_WEBSITE

    return (
        "Sorry, I don't have a verified answer to that question yet.\n"
        f"Selected department: {department}\n"
        "Please check the official website:\n"
        + COLLEGE_WEBSITE
    )
