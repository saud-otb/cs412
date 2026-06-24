# File: ai.py
# Author: Saud Alotaibi
# Description: Helper that summarizes a game's reviews using the Gemini API.

try:
    import truststore
    truststore.inject_into_ssl()
except Exception:
    pass

from django.conf import settings
from google import genai


def summarize_reviews(game, reviews):
    '''Return an AI-generated overview of the given reviews for a game.

    Returns an empty string if there are no reviews. Raises on API errors so
    the caller can decide how to handle failures.'''

    if not reviews:
        return ""

    # Build the list of formatted review lines to include in the prompt
    lines = []
    for review in reviews:
        recommended = "Recommended" if review.recommended else "Not recommended"
        lines.append(
            f"- Rating {review.rating}/10 ({recommended}): "
            f"{review.review_title} - {review.review_text}"
        )

    # Compute the average rating to prepend to the AI response
    sum = 0
    for review in reviews:
        sum += review.rating

    average_rating = sum / len(reviews)

    # Build the prompt instructing Gemini to summarize based only on the provided reviews
    prompt = (
        f"You are summarizing player reviews for the video game '{game.title}'.\n"
        f"Write a short overview (3-5 sentences), then a 'The Good' bullet list and a "
        f"'The Bad' bullet list, based ONLY on the reviews below. Do not invent details.\n\n"
        f"Reviews:\n" + "\n".join(lines)
    )

    # Call the Gemini API and return the response with the average rating prepended
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return f"Average Rating: {average_rating:.1f}/10\n\n" + response.text
