import streamlit as st
import pandas as pd

# =========================================================
# SMARTCAREER AI
# AI-Powered Smart Career & Skill Recommendation System
# =========================================================

st.set_page_config(
    page_title="SmartCareer AI",
    page_icon="🎯",
    layout="wide"
)

# =========================================================
# CAREER DATABASE
# =========================================================

CAREERS = {

    "Software Developer": {
        "streams": ["MPC", "MEC", "CEC", "Computer Science"],
        "subjects": ["Mathematics", "Computer Science", "Physics"],
        "skills": {
            "python", "java", "javascript", "html", "css",
            "sql", "programming", "git"
        },
        "interests": {
            "programming", "technology", "software",
            "apps", "web development"
        },
        "education": {
            "computer science",
            "information technology",
            "software engineering"
        },
        "description":
            "Build software applications, websites and technology products."
    },

    "Data Scientist": {
        "streams": ["MPC", "Computer Science", "MEC"],
        "subjects": ["Mathematics", "Computer Science", "Statistics"],
        "skills": {
            "python", "machine learning", "statistics",
            "pandas", "numpy", "sql", "data analysis"
        },
        "interests": {
            "data", "artificial intelligence",
            "machine learning", "research", "analytics"
        },
        "education": {
            "computer science",
            "data science",
            "statistics",
            "mathematics"
        },
        "description":
            "Analyze data and build models to solve real-world problems."
    },

    "Machine Learning Engineer": {
        "streams": ["MPC", "Computer Science", "MEC"],
        "subjects": ["Mathematics", "Computer Science", "Physics"],
        "skills": {
            "python", "machine learning", "deep learning",
            "tensorflow", "pytorch", "sql", "git"
        },
        "interests": {
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "software",
            "research"
        },
        "education": {
            "computer science",
            "information technology",
            "artificial intelligence",
            "data science"
        },
        "description":
            "Develop machine-learning and AI systems."
    },

    "Data Analyst": {
        "streams": ["MPC", "MEC", "CEC", "Commerce"],
        "subjects": ["Mathematics", "Statistics", "Commerce"],
        "skills": {
            "excel", "sql", "python", "pandas",
            "statistics", "data analysis", "power bi"
        },
        "interests": {
            "data", "analytics", "business",
            "statistics", "visualization"
        },
        "education": {
            "data science",
            "statistics",
            "computer science",
            "business analytics",
            "information technology"
        },
        "description":
            "Turn business data into useful insights and decisions."
    },

    "Cybersecurity Analyst": {
        "streams": ["MPC", "Computer Science", "MEC"],
        "subjects": ["Computer Science", "Mathematics", "Physics"],
        "skills": {
            "networking", "linux", "cybersecurity",
            "python", "security", "ethical hacking", "sql"
        },
        "interests": {
            "cybersecurity", "security",
            "networking", "ethical hacking", "technology"
        },
        "education": {
            "computer science",
            "information technology",
            "cybersecurity",
            "network security"
        },
        "description":
            "Protect computers, networks and digital systems."
    },

    "Cloud Engineer": {
        "streams": ["MPC", "Computer Science", "MEC"],
        "subjects": ["Computer Science", "Mathematics", "Physics"],
        "skills": {
            "aws", "azure", "cloud computing",
            "linux", "docker", "kubernetes", "networking"
        },
        "interests": {
            "cloud computing", "technology",
            "networking", "devops", "infrastructure"
        },
        "education": {
            "computer science",
            "information technology",
            "cloud computing"
        },
        "description":
            "Design and manage cloud infrastructure and services."
    },

    "UI/UX Designer": {
        "streams": ["Arts/Humanities", "MPC", "CEC", "Design"],
        "subjects": ["Art", "Computer Science", "Design"],
        "skills": {
            "figma", "ui design", "ux design",
            "wireframing", "prototyping", "graphic design"
        },
        "interests": {
            "design", "creativity",
            "user experience", "art", "websites"
        },
        "education": {
            "design",
            "computer science",
            "graphic design",
            "multimedia"
        },
        "description":
            "Design user-friendly digital products and experiences."
    },

    "Business Analyst": {
        "streams": ["MEC", "CEC", "Commerce"],
        "subjects": ["Mathematics", "Commerce", "Economics"],
        "skills": {
            "excel", "sql", "data analysis",
            "power bi", "communication", "presentation"
        },
        "interests": {
            "business", "analytics",
            "management", "finance", "technology"
        },
        "education": {
            "business analytics",
            "commerce",
            "business",
            "management"
        },
        "description":
            "Use data and business knowledge to improve organizations."
    },

    "Financial Analyst": {
        "streams": ["MEC", "CEC", "Commerce"],
        "subjects": ["Mathematics", "Commerce", "Economics"],
        "skills": {
            "excel", "statistics",
            "financial analysis", "accounting",
            "data analysis"
        },
        "interests": {
            "finance", "business",
            "economics", "investment", "analytics"
        },
        "education": {
            "commerce",
            "finance",
            "business",
            "economics"
        },
        "description":
            "Analyze financial information and support financial decisions."
    },

    "Doctor / Medical Professional": {
        "streams": ["BiPC", "Science"],
        "subjects": ["Biology", "Chemistry", "Physics"],
        "skills": {
            "biology", "chemistry",
            "communication", "problem solving"
        },
        "interests": {
            "healthcare", "medicine",
            "biology", "helping people", "science"
        },
        "education": {
            "biology",
            "medical science",
            "life science"
        },
        "description":
            "Work in healthcare and help diagnose and treat patients."
    },

    "Biotechnology Researcher": {
        "streams": ["BiPC", "Science"],
        "subjects": ["Biology", "Chemistry"],
        "skills": {
            "biology", "chemistry",
            "research", "laboratory"
        },
        "interests": {
            "biology", "research",
            "science", "healthcare"
        },
        "education": {
            "biology",
            "biotechnology",
            "life science"
        },
        "description":
            "Research biological systems and develop biotechnology solutions."
    }
}


# =========================================================
# RECOMMENDATION ENGINE
# =========================================================

def calculate_match(
    stream,
    education,
    skills,
    interests,
    subjects,
    scores,
    preferred_careers
):

    results = []

    for career, info in CAREERS.items():

        score = 0
        reasons = []

        # -------------------------------------------------
        # 1. STREAM MATCH - 20%
        # -------------------------------------------------

        if stream in info["streams"]:
            score += 20
            reasons.append("Your academic stream matches this career.")

        # -------------------------------------------------
        # 2. SUBJECT MATCH - 15%
        # -------------------------------------------------

        subject_matches = set(subjects).intersection(
            set(info["subjects"])
        )

        subject_score = (
            len(subject_matches) / len(info["subjects"])
            if info["subjects"]
            else 0
        )

        score += subject_score * 15

        if subject_matches:
            reasons.append(
                "Your strong subjects are relevant to this career."
            )

        # -------------------------------------------------
        # 3. ACADEMIC SCORE - 15%
        # -------------------------------------------------

        relevant_scores = []

        for subject in info["subjects"]:
            if subject in scores:
                relevant_scores.append(scores[subject])

        if relevant_scores:
            average_score = sum(relevant_scores) / len(relevant_scores)

            # Academic contribution
            academic_score = (average_score / 100) * 15
            score += academic_score

            if average_score >= 75:
                reasons.append(
                    f"Your average score in relevant subjects is "
                    f"{average_score:.1f}%."
                )

        # -------------------------------------------------
        # 4. SKILL MATCH - 20%
        # -------------------------------------------------

        skill_matches = skills.intersection(info["skills"])

        skill_score = (
            len(skill_matches) / len(info["skills"])
            if info["skills"]
            else 0
        )

        score += skill_score * 20

        # -------------------------------------------------
        # 5. INTEREST MATCH - 20%
        # -------------------------------------------------

        interest_matches = interests.intersection(
            info["interests"]
        )

        interest_score = (
            len(interest_matches) / len(info["interests"])
            if info["interests"]
            else 0
        )

        score += interest_score * 20

        if interest_matches:
            reasons.append(
                "Your interests strongly relate to this career."
            )

        # -------------------------------------------------
        # 6. PREFERRED CAREER - 10%
        # -------------------------------------------------

        if career in preferred_careers:
            score += 10
            reasons.append(
                "You selected this as one of your preferred career paths."
            )

        # -------------------------------------------------
        # FINAL RESULT
        # -------------------------------------------------

        missing_skills = info["skills"] - skills

        results.append({
            "Career": career,
            "Score": round(min(score, 100), 1),
            "Description": info["description"],
            "Matched Skills": sorted(skill_matches),
            "Missing Skills": sorted(missing_skills),
            "Matched Interests": sorted(interest_matches),
            "Subject Matches": sorted(subject_matches),
            "Reasons": reasons
        })

    results.sort(
        key=lambda x: x["Score"],
        reverse=True
    )

    return results


# =========================================================
# HEADER
# =========================================================

st.title("🎯 SmartCareer AI")

st.subheader(
    "AI-Powered Smart Career & Skill Recommendation System"
)

st.write(
    """
    Get personalized career recommendations based on your
    academic stream, marks, subjects, skills, interests and
    preferred career paths.
    """
)

st.divider()


# =========================================================
# STUDENT PROFILE
# =========================================================

st.header("👨‍🎓 Student Profile")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "👤 Your Name",
        placeholder="Enter your name"
    )

    stream = st.selectbox(
        "🎓 Which stream are you studying?",
        [
            "MPC",
            "BiPC",
            "MEC",
            "CEC",
            "Commerce",
            "Arts/Humanities",
            "Computer Science",
            "Science",
            "Design"
        ]
    )

    education = st.selectbox(
        "🏫 Current Education",
        [
            "Class 10",
            "Class 11",
            "Class 12",
            "Diploma",
            "Undergraduate",
            "Postgraduate"
        ]
    )

with col2:

    experience = st.selectbox(
        "💼 Experience Level",
        [
            "Student",
            "Fresher",
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    subjects = st.multiselect(
        "📚 Your Strong Subjects",
        [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "Computer Science",
            "Statistics",
            "Commerce",
            "Economics",
            "Accountancy",
            "Art",
            "Design"
        ]
    )


# =========================================================
# ACADEMIC SCORES
# =========================================================

st.header("📊 Academic Performance")

st.write(
    "Enter your approximate marks for the subjects you have studied."
)

score_subjects = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "Computer Science",
    "Statistics",
    "Commerce",
    "Economics",
    "Accountancy",
    "Art",
    "Design"
]

scores = {}

score_cols = st.columns(3)

for index, subject in enumerate(score_subjects):

    with score_cols[index % 3]:

        mark = st.number_input(
            f"{subject} %",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

        if mark > 0:
            scores[subject] = mark


# =========================================================
# SKILLS
# =========================================================

st.header("💻 Your Skills")

skills_input = st.text_area(
    "Enter your skills separated by commas",
    placeholder=(
        "Example: Python, SQL, Programming, "
        "Excel, Communication"
    )
)


# =========================================================
# INTERESTS
# =========================================================

st.header("❤️ Your Interests")

interests_input = st.text_area(
    "What areas do you enjoy?",
    placeholder=(
        "Example: Artificial Intelligence, "
        "Technology, Business, Healthcare"
    )
)


# =========================================================
# PREFERRED CAREER PATHS
# =========================================================

st.header("🚀 Your Preferred Career Paths")

st.write(
    "Select up to 3 careers that you are currently interested in."
)

preferred_careers = st.multiselect(
    "Choose your preferred careers",
    list(CAREERS.keys()),
    max_selections=3
)


# =========================================================
# RECOMMENDATION BUTTON
# =========================================================

st.divider()

if st.button(
    "🚀 Analyze My Career",
    use_container_width=True
):

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not subjects:
        st.warning(
            "Please select at least one strong subject."
        )

    elif not skills_input.strip():
        st.warning(
            "Please enter at least one skill."
        )

    elif not interests_input.strip():
        st.warning(
            "Please enter at least one interest."
        )

    else:

        # -------------------------------------------------
        # PROCESS INPUT
        # -------------------------------------------------

        user_skills = {
            item.strip().lower()
            for item in skills_input.split(",")
            if item.strip()
        }

        user_interests = {
            item.strip().lower()
            for item in interests_input.split(",")
            if item.strip()
        }

        # -------------------------------------------------
        # CALCULATE
        # -------------------------------------------------

        recommendations = calculate_match(
            stream=stream,
            education=education,
            skills=user_skills,
            interests=user_interests,
            subjects=subjects,
            scores=scores,
            preferred_careers=preferred_careers
        )

        # =================================================
        # TOP 3
        # =================================================

        st.header("🏆 Your Top 3 Career Paths")

        top_three = recommendations[:3]

        for index, career in enumerate(
            top_three,
            start=1
        ):

            st.subheader(
                f"{index}. {career['Career']}"
            )

            st.progress(
                int(career["Score"])
            )

            st.write(
                f"### Match Score: {career['Score']}%"
            )

            st.info(
                career["Description"]
            )

            if career["Reasons"]:

                st.write("**Why this career suits you:**")

                for reason in career["Reasons"]:
                    st.write(
                        f"✅ {reason}"
                    )

            if career["Matched Skills"]:

                st.write(
                    "**Matching skills:** "
                    + ", ".join(
                        career["Matched Skills"]
                    )
                )

            if career["Matched Interests"]:

                st.write(
                    "**Matching interests:** "
                    + ", ".join(
                        career["Matched Interests"]
                    )
                )

            st.divider()


        # =================================================
        # BEST CAREER
        # =================================================

        best = recommendations[0]

        st.header("🎯 Recommended Career")

        st.success(
            f"Based on your complete profile, "
            f"**{best['Career']}** currently has the "
            f"highest match score of **{best['Score']}%**."
        )


        # =================================================
        # CAREER COMPARISON
        # =================================================

        st.header("📊 Career Comparison")

        comparison_data = []

        for career in top_three:

            comparison_data.append({
                "Career": career["Career"],
                "Match Score": f"{career['Score']}%",
                "Description": career["Description"]
            })

        comparison_df = pd.DataFrame(
            comparison_data
        )

        st.dataframe(
            comparison_df,
            use_container_width=True,
            hide_index=True
        )


        # =================================================
        # SKILL GAP
        # =================================================

        st.header("🧩 Skill Gap Analysis")

        missing = best["Missing Skills"]

        if missing:

            st.write(
                f"To prepare for **{best['Career']}**, "
                "you can focus on these skills:"
            )

            for skill in missing:

                st.write(
                    f"📚 {skill.title()}"
                )

        else:

            st.success(
                "🎉 You already have the core skills "
                "in our current career database."
            )


        # =================================================
        # LEARNING ROADMAP
        # =================================================

        st.header("📚 Personalized Learning Roadmap")

        if missing:

            for number, skill in enumerate(
                missing,
                start=1
            ):

                st.write(
                    f"**Step {number}:** "
                    f"Learn and practice **{skill.title()}**"
                )

            st.info(
                """
                💡 Tip: Build small projects while learning.
                Projects help you understand the skills and
                demonstrate your abilities.
                """
            )

        else:

            st.write(
                "Continue improving your existing skills "
                "through projects and practical experience."
            )


        # =================================================
        # FINAL GUIDANCE
        # =================================================

        st.header("🤖 Smart Career Guidance")

        guidance = f"""
        **Hello {name if name else "Student"}!**

        Your current strongest career recommendation is
        **{best['Career']}** with a **{best['Score']}%** match.

        This recommendation considers:

        • Your academic stream: **{stream}**
        • Your education level: **{education}**
        • Your academic subjects
        • Your academic scores
        • Your skills
        • Your interests
        • Your preferred career choices

        Your current experience level is **{experience}**.

        Use the Top 3 careers as options rather than as a
        fixed decision. Your interests and skills can change
        as you learn more.
        """

        st.info(guidance)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "SmartCareer AI | Personalized Career & Skill Recommendation System"
)