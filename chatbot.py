def get_response(user_input):
    text = user_input.lower()

    policies = {

        #SICK LEAVE POLICY
        "sick_leave": {
            "keywords": [
                "sick leave", "medical leave", "illness leave"
            ],
            "response": (
                "Employees are entitled to 12 sick leaves per year. "
                "Unused sick leave cannot be carried forward."
            )
        },

        #CASUAL LEAVE
        "casual_leave": {
            "keywords": [
                "casual leave", "cl", "leave policy"
            ],
            "response": (
                "Employees are entitled to 12 casual leaves per year. "
                "Casual leave cannot be clubbed with special leave."
            )
        },

        #WORK FROM HOME
        "wfh_policy": {
            "keywords": [
                "work from home", "wfh", "remote work", "wfh friday"
            ],
            "response": (
                "Work from home is permitted on Fridays with prior manager approval."
            )
        },

        #TRAVEL REIMBURSEMENT
        "travel_reimbursement": {
            "keywords": [
                "travel reimbursement", "travel claim", "travel expenses"
            ],
            "response": (
                "Travel reimbursement is allowed up to ₹25,000 per trip. "
                "Claims must be submitted within 7 working days."
            )
        },

        #WORKING HOURS
        "working_hours": {
            "keywords": [
                "working hours", "office timing", "work time"
            ],
            "response": (
                "Office working hours are from 9:00 AM to 6:00 PM, Monday to Friday."
            )
        },

        #SALARY CREDIT
        "salary_policy": {
            "keywords": [
                "salary", "salary date", "payment date"
            ],
            "response": (
                "Salary is credited on the 5th of every month."
            )
        },

        #MEDICAL INSURANCE
        "medical_insurance": {
            "keywords": [
                "medical insurance", "health insurance", "mediclaim"
            ],
            "response": (
                "Medical insurance coverage is provided up to ₹5,00,000 per year."
            )
        },

        #ATTENDANCE
        "attendance_policy": {
            "keywords": [
                "attendance", "biometric", "late entry"
            ],
            "response": (
                "Attendance must be marked using the biometric system. "
                "More than 3 late entries per month may lead to deduction."
            )
        },

        #MATERNITY / PATERNITY
        "parental_leave": {
            "keywords": [
                "maternity leave", "paternity leave"
            ],
            "response": (
                "Maternity leave is 26 weeks. Paternity leave is 5 working days."
            )
        },

        #INFORMATION SECURITY
        "data_security": {
            "keywords": [
                "data security", "confidential", "information security"
            ],
            "response": (
                "Sharing confidential company information externally is prohibited."
            )
        },

        #IT ASSET POLICY
        "it_assets": {
            "keywords": [
                "laptop", "it asset", "company laptop"
            ],
            "response": (
                "Company-issued laptops must be used only for official purposes."
            )
        },

        #EMAIL USAGE
        "email_policy": {
            "keywords": [
                "email usage", "official email"
            ],
            "response": (
                "Official email must be used only for business communication."
            )
        },

        #CODE OF CONDUCT
        "code_of_conduct": {
            "keywords": [
                "code of conduct", "behavior policy"
            ],
            "response": (
                "Employees are expected to maintain professional conduct at all times."
            )
        },

        #HARASSMENT POLICY
        "harassment_policy": {
            "keywords": [
                "harassment", "posh", "sexual harassment"
            ],
            "response": (
                "The organization follows a zero-tolerance policy towards harassment."
            )
        },

        #RESIGNATION NOTICE
        "notice_period": {
            "keywords": [
                "notice period", "resignation"
            ],
            "response": (
                "The standard notice period is 60 days for full-time employees."
            )
        },

        #OFFICE ACCESS
        "office_access": {
            "keywords": [
                "office access", "id card"
            ],
            "response": (
                "Employees must carry their ID cards while entering office premises."
            )
        }
    }

    for policy in policies.values():
        for keyword in policy["keywords"]:
            if keyword in text:
                return policy["response"]

    return (
        "Sorry, I couldn't find that information. "
        "Please contact HR for further clarification."
    )

