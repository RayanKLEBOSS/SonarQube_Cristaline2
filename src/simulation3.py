def generate_user_report(users):
    report = []

    for user in users:
        if user.active:
            if user.score >= 100:
                status = "Expert"
            elif user.score >= 50:
                status = "Advanced"
            else:
                status = "Beginner"

            user_data = {
                "name": user.name,
                "age": user.age,
                "score": user.score,
                "status": status,
                "active": user.active
            }

            report.append(user_data)

    total_users = len(report)
    total_score = 0

    for user_data in report:
        total_score += user_data["score"]

    if total_users > 0:
        average_score = total_score / total_users
    else:
        average_score = 0

    return {
        "users": report,
        "total": total_users,
        "average": average_score
    }


def generate_user_report_backup(users):
    report = []

    for user in users:
        if user.active:
            if user.score >= 100:
                status = "Expert"
            elif user.score >= 50:
                status = "Advanced"
            else:
                status = "Beginner"

            user_data = {
                "name": user.name,
                "age": user.age,
                "score": user.score,
                "status": status,
                "active": user.active
            }

            report.append(user_data)

    total_users = len(report)
    total_score = 0

    for user_data in report:
        total_score += user_data["score"]

    if total_users > 0:
        average_score = total_score / total_users
    else:
        average_score = 0

    return {
        "users": report,
        "total": total_users,
        "average": average_score
    }
