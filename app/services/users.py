from app.store import USERS


def contact_card(user_id: str) -> dict:
    user = USERS[user_id]
    return {
        "name": user["name"],
        "email": user["email"],
        "phone": user["phone"].replace(" ", ""),
    }
