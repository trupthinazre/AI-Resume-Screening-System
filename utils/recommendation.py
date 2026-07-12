def get_recommendation(score):

    if score >= 26:
        return "⭐ Highly Recommended"

    elif score >= 20:
        return "✅ Recommended"

    elif score >= 10:
        return "🟡 Consider"

    else:
        return "❌ Not Recommended"