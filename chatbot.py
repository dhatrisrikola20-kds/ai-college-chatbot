
COLLEGE_WEBSITE = "https://sjcit.ac.in/"

SCHEME_URL = "https://sjcit.ac.in/scheme-and-syllabus/"

DEPARTMENTS = {
    "Artificial Intelligence and Data Science (AI & DS)": "AI & DS",
    "Computer Science and Engineering (CSE)": "CSE",
    "Information Science and Engineering (ISE)": "ISE",
    "Electronics and Communication Engineering (ECE)": "ECE",
    "Electrical and Electronics Engineering (EEE)": "EEE",
    "Mechanical Engineering": "ME",
    "Civil Engineering": "CE",
    "Computer Science and Engineering (AI & ML)": "AI & ML",
    "Computer Science and Engineering (Data Science)": "CSE (DS)"
}

MENU_OPTIONS = {
    "1. Courses and syllabus": "syllabus",
    "2. Fee structure": "fees",
    "3. Examination details": "exams",
    "4. Faculty information": "faculty",
    "5. Placement information": "placements",
    "6. College website": "website"
}


def get_menu_response(choice, department):
    topic = MENU_OPTIONS.get(choice)

    if topic:
        return get_response(topic, department)

    return "Please select a valid information option."


def get_response(question, department):
    q = question.lower().strip()
    dept = department

    # Greetings
    if any(word in q for word in ["hello", "hi", "hey", "good morning",
                                  "good afternoon", "good evening"]):
        return (
            f"Hello! Welcome to the SJCIT AI College Chatbot. "
            f"You selected {dept}. How can I help you?"
        )

    # Thank you
    if any(word in q for word in ["thank you", "thanks", "thank u"]):
        return "You're welcome! Feel free to ask me anything about SJCIT."

    # Goodbye
    if any(word in q for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day. Visit again!"

    # Placement
    if any(word in q for word in ["placement", "placements", "job",
                                  "recruitment", "companies", "package"]):
        return (
            "SJCIT students can check placement training, eligibility, "
            "recruitment drives and company updates through the placement cell. "
            "For current placement details, visit the official college website: "
            + COLLEGE_WEBSITE
        )

    # Fees
    if any(word in q for word in ["fee", "fees", "tuition",
                                  "payment", "scholarship"]):
        return (
            "Fee details may vary by course and admission category. "
            "Please contact the college admissions office for the latest "
            "verified fee information: " + COLLEGE_WEBSITE
        )

    # Syllabus
    if any(word in q for word in ["syllabus", "scheme", "subjects",
                                  "course", "courses", "curriculum"]):
        return (
            f"Here you can find the scheme and syllabus information "
            f"for {dept}. Visit: {SCHEME_URL}"
        )

    # Exams
    if any(word in q for word in ["exam", "examination", "timetable",
                                  "results", "internal", "cie"]):
        return (
            "For examination timetables, results and academic updates, "
            "please check the official college website or examination section: "
            + COLLEGE_WEBSITE
        )

    # Faculty
    if any(word in q for word in ["faculty", "professor", "lecturer",
                                  "hod", "staff"]):
        return (
            f"For verified faculty and department information about {dept}, "
            f"please visit the official SJCIT website: {COLLEGE_WEBSITE}"
        )

    # Department
    if any(word in q for word in ["department", "branch", "stream"]):
        return (
            f"You have selected {dept}. Ask me about its syllabus, "
            "courses, exams or placements."
        )

    # College information
    if any(word in q for word in ["college", "sjcit", "website",
                                  "location", "address"]):
        return (
            "SJC Institute of Technology is located in Chickballapur, "
            "Karnataka. Visit the official website: " + COLLEGE_WEBSITE
        )

    # Help
    if any(word in q for word in ["help", "what can you do", "options"]):
        return (
            "I can help you with SJCIT syllabus, fees, examinations, "
            "faculty, placements and college information. What would "
            "you like to know?"
        )

    return (
        f"Sorry, I don't have a verified answer for that yet. "
        f"You can ask me about {dept}, syllabus, fees, exams or placements. "
        f"For official information, visit {COLLEGE_WEBSITE}"
    )
